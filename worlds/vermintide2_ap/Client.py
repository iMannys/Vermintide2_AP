import asyncio
import json
from pathlib import Path

from CommonClient import ClientCommandProcessor, CommonContext, logger, \
    get_base_parser, server_loop, gui_enabled


class Vermintide2CommandProcessor(ClientCommandProcessor):
    def _cmd_check(self, location_name: str):
        """Manually check a location by name - used for testing"""
        if location_name in self.ctx.location_names:
            self.ctx.checked_locations.add(self.ctx.location_names[location_name])

class Vermintide2Context(CommonContext):
    game = "Warhammer: Vermintide 2"
    command_processor = Vermintide2CommandProcessor
    items_handling = 0b111 # receive all items

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super().server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    def on_package(self, cmd: str, args: dict):
        if cmd == "Connected":
            logger.info("Connected to Archipelago server")
        if cmd == "ReceivedItems":
            # items the server is sending to the player
            for item in args["items"]:
                logger.info(f"Received item: {self.item_names[item.item]}")


async def game_watcher(ctx: Vermintide2Context):
    checked_file = Path("checked_locations.json")
    last_checked = set()

    while not ctx.exit_event.is_set():
        if checked_file.exists():
            with open(checked_file) as f:
                data = json.load(f)

            newly_checked = set(data["checked_locations"]) - last_checked
            if newly_checked:
                # convert names to IDs and send to server
                location_ids = [
                    ctx.location_names.lookup_in_game(name)
                    for name in newly_checked
                    if name in ctx.location_names
                ]
                await ctx.send_msgs([{
                    "cmd": "LocationChecks",
                    "locations": location_ids
                }])
                last_checked = set(data["checked_locations"])

        await asyncio.sleep(1)

def main():
    parser = get_base_parser()
    args = parser.parse_args()

    async def _main():
        ctx = Vermintide2Context(args.connect, args.password)
        ctx.server_task = asyncio.ensure_future(server_loop(ctx))
        asyncio.ensure_future(game_watcher(ctx))

        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()

        await ctx.exit_event.wait()
        await ctx.shutdown()

    import colorama
    colorama.init()
    asyncio.run(_main())


if __name__ == "__main__":
    main()