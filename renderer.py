import attrs
import tcod.context
from tcod.console import Console
from tcod.context import Context
from gamemap import GameMap


@attrs.define
class Renderer:
    game_map : GameMap
    context : "Context" = None
    console : "Console" = None

    def __attrs_post_init__(self):
        self.context = None
        self.console = None

    def master_render():
        #game_map_render()
        pass


    def fullmap_render(self):
        self.game_map.render(self.console)
        self.context.present(self.console)
        self.console.clear()