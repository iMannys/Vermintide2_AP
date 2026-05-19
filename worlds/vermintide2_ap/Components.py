from worlds.LauncherComponents import Component, Type, components, launch

def run_client(*args: str) -> None:
    from .Client import launch_vermintide_client
    launch(launch_vermintide_client, name="Vermintide 2 Client", args=args)

components.append(
    Component(
        "Vermintide 2 Client",
        func=run_client,
        game_name="Warhammer: Vermintide 2",
        component_type=Type.CLIENT,
        supports_uri=True,
    )
)