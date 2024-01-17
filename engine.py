#Engine.py
from typing import Set,Iterable,Any
import attrs
from tcod.context import Context
from tcod.console import Console
from tcod import event
import tcod
from input_handlers import EventHandler

from actions import EscapeAction, MovementAction
from entities import Entity
from gamemap import GameMap
from input_handlers import EventHandler


@attrs.define
class Engine:
    entities : set[Entity]
    event_handler : EventHandler
    game_map : GameMap
    player : Entity

    def handle_events(self, events:Iterable[Any]) ->None:
        for event in tcod.event.wait(): #this waits until pending events 'exist'
            action = self.event_handler.dispatch(event)
            
            if action is None:
                continue
                
            if isinstance(action,MovementAction):
                if self.game_map.tiles["walkable"][self.player.x + action.dx, self.player.y + action.dy]:
                    self.player.move(dx=action.dx, dy=action.dy)

            elif isinstance(action,EscapeAction):
                raise SystemExit()

    def render(self,console:Console,context:Context):
        self.game_map.render(console)

        for entity in self.entities:
            console.print(entity.x,entity.y,entity.char,fg = entity.color)

        context.present(console)
        console.clear()
