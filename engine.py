#Engine.py
from typing import Set,Iterable,Any
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


@attrs.define
class Engine:
    entities : set[Entity]
    event_handler : EventHandler
    game_map : GameMap
    player : Entity
    
    def __attrs_post_init__(self):
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

    def render(self,console:Console,context:Context):
        self.game_map.render(console)

        for entity in self.entities:
            if self.game_map.visible[entity.x, entity.y]:
                console.print(entity.x, entity.y, entity.char,fg = entity.color)

        context.present(console)
        console.clear()
