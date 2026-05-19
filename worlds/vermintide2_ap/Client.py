import sys
import json
import re
import asyncio
from typing import Dict, Type

import colorama
import kvui

from pathlib import Path
from CommonClient import (
    ClientCommandProcessor,
    CommonContext,
    logger,
    get_base_parser,
    handle_url_arg,
    server_loop,
    gui_enabled
)


def parse_sjson(raw_text: str) -> dict:
    """Sanitizes Stingray SJSON format into standard compliant JSON using built-in regex."""
    text = re.sub(r'//.*', '', raw_text)  # Remove comments
    text = re.sub(r'([a-zA-Z_][a-zA-Z0-9_]*)\s*=', r'"\1" =',
                  text)  # Quote keys
    text = text.replace('=', ':')  # Convert assignments to colons
    text = re.sub(r',\s*([]}])', r'\1', text)  # Strip trailing commas
    try:
        return json.loads(text)
    except Exception:
        return {}


class Vermintide2CommandProcessor(ClientCommandProcessor):
    def _cmd_check(self, location_name: str) -> None:
        loc_lookup = self.ctx.location_names[self.ctx.game]
        loc_id = next(
            (id for id, name in loc_lookup.items() if name == location_name),
            None)

        if isinstance(loc_id, int):
            self.ctx.locations_checked.add(loc_id)
            logger.info(f"Manually marked {location_name} as checked.")
        else:
            logger.error(f"Unknown location name: {location_name}")

class Vermintide2Context(CommonContext):
    game = "Warhammer: Vermintide 2"
    command_processor = Vermintide2CommandProcessor
    items_handling = 0b111
    highest_processed_item_index = 0

    async def server_auth(self, password_requested: bool = False) -> None:
        if password_requested and not self.password:
            await super().server_auth(password_requested)
        await self.get_username()
        await self.send_connect(game=self.game)

    def on_package(self, cmd: str, args: dict) -> None:
        if cmd == "Connected":
            logger.info("Connected to Archipelago server successfully!")
            self.highest_processed_item_index = 0

    def make_gui(self) -> Type["kvui.GameManager"]:
        from kivy.config import Config
        Config.set('kivy', 'window_title', 'Vermintide 2 Client')

        import kvui
        return kvui.GameManager

    async def vermintide_loop(self) -> None:
        while not self.exit_event.is_set():
            new_items = self.items_received[self.highest_processed_item_index:]
            for item in new_items:
                self.highest_processed_item_index += 1
                logger.info(
                    f"Received item from server: {self.item_names.get(item.item)}")
            await asyncio.sleep(0.1)


async def game_watcher(ctx: Vermintide2Context) -> None:
    v2_save_path = Path.home() / "AppData/Roaming/Fatshark/Vermintide 2/save_data.sav"
    last_mtime = 0.0
    last_processed_checks = set()

    while not ctx.exit_event.is_set():
        if v2_save_path.exists():
            try:
                current_mtime = v2_save_path.stat().st_mtime
                if current_mtime > last_mtime:
                    last_mtime = current_mtime
                    raw_bytes = v2_save_path.read_bytes()
                    header_offset = raw_bytes.find(b'{')

                    if header_offset != -1:
                        sjson_string = raw_bytes[header_offset:].decode('utf-8',
                                                                        errors='ignore')
                        save_data = parse_sjson(
                            sjson_string)  # Clean standard parsing

                        ap_mod_table = save_data.get("vermintide_ap", {})
                        pending_checks = ap_mod_table.get("pending_checks", [])

                        current_checks_set = set(pending_checks)
                        newly_found = current_checks_set - last_processed_checks

                        if newly_found and ctx.game:
                            loc_lookup = ctx.location_names[ctx.game]
                            name_to_id: Dict[str, int] = {name: id for id, name
                                                          in loc_lookup.items()}
                            location_ids = {name_to_id[c] for c in newly_found
                                            if c in name_to_id}
                            if location_ids:
                                await ctx.check_locations(location_ids)
                                logger.info(
                                    f"Sent checked locations to server: {list(newly_found)}")
                            last_processed_checks = current_checks_set
            except Exception as e:
                logger.error(f"Error reading save file: {e}")
        await asyncio.sleep(1.0)


def launch_vermintide_client(*args: str) -> None:
    parser = get_base_parser()
    parser.add_argument("--name", default=None)
    parser.add_argument("url", nargs="?")
    launch_args = handle_url_arg(parser.parse_args(args))

    async def _main() -> None:
        ctx = Vermintide2Context(launch_args.connect, launch_args.password)
        if launch_args.name:
            ctx.auth = launch_args.name

        ctx.server_task = asyncio.create_task(server_loop(ctx))
        asyncio.create_task(game_watcher(ctx))
        asyncio.create_task(ctx.vermintide_loop())

        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()
        await ctx.exit_event.wait()
        await ctx.shutdown()

    colorama.just_fix_windows_console()
    asyncio.run(_main())