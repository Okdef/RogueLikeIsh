import attrs
from tcod.console import Console
from tcod.context import Context
from gamemap import GameMap
from entities import Entity
from inventory import Inventory
import tcod


@attrs.define
class Renderer:
    game_map : GameMap
    context : "Context" = None
    console : "Console" = None
    inventory_render_status : bool = False
    player : Entity = None

    def __attrs_post_init__(self):
        self.context = None
        self.console = None
        self.inventory_render_status = False
        self.player = None

    def master_render():
        #game_map_render()
        pass


    def fullmap_render(self):
        self.game_map.render(self.console)
        if self.inventory_render_status == True:
            self.inventory_render()
        self.status_render()
        self.context.present(self.console)
        self.console.clear()

    def render_toggle_inventory(self):
        if self.inventory_render_status == False:
            self.inventory_render_status = True
        else:
            self.inventory_render_status = False
        
    
    def status_render(self):
        hearts = " <3" * self.player.hp_current
        actionsleft = " =" * self.player.action_pool
        self.console.print(0,0,f"\n{hearts}\n{actionsleft}")



    def inventory_render(self):
        bag_string = ""
        for i in self.player.bag:
            bag_string += f"{i.name}\n"
        self.console.print_box(0,20,8,20,bag_string,fg = [255,255,255])
        