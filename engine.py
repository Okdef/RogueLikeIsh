#Engine.py
from typing import Iterable,Any
import attrs
from tcod.context import Context
from tcod.console import Console
from tcod import event
import tcod
from tcod.map import compute_fov
from input_handlers import EventHandler
from entities import Entity
from gamemap import GameMap
from input_handlers import EventHandler
from turn_controller import TurnController
from entity_ai import AIController
from gamemap import GameMap
from renderer import Renderer

@attrs.define
class Engine:
    event_handler : EventHandler
    game_map : GameMap
    player : Entity
    aicontroller : AIController = None
    turncontroller : TurnController = None
    renderer : Renderer = None

    def __attrs_post_init__(self):
        self.renderer = Renderer(self.game_map)
        self.aicontroller = AIController(gamemap = self.game_map,player = self.player) if self.aicontroller is None else self.aicontroller
        self.aicontroller.renderer = self.renderer
        self.turncontroller = TurnController(aicontroller = self.aicontroller , player=self.player) if self.turncontroller is None else self.turncontroller
        self.update_fov()
        
    

    def handle_events(self, events:Iterable[Any]) ->None:
        for event in events: #this waits until pending events 'exist'
            action = self.event_handler.dispatch(event)
            
            if action is None:
                continue
                
            action.perform(self, self.player)
            self.update_fov()
    
    def update_fov(self) -> None:
        self.game_map.visible[:] = compute_fov(
            self.game_map.tiles["transparent"],
            (self.player.x, self.player.y),
            radius = 8,
        )
        self.game_map.explored |= self.game_map.visible

      #def render(self,console:Console,context:Context):
        #self.game_map.render(console)
        #context.present(console)
        #console.clear()
 
    