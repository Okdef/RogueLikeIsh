#actions
from __future__ import annotations
import attrs
from typing import TYPE_CHECKING
import entities

if TYPE_CHECKING:
    from engine import Engine
    from entities import Entity

@attrs.define
class Action:
    def perform(self, engine: Engine, entity : Entity) -> None:
        raise NotImplementedError()
        

@attrs.define
class EscapeAction(Action):
    action : Action

    def perform(self, engine:Engine, entity: Entity) -> None:
        raise SystemExit()



@attrs.define
class MovementAction(Action):
    dx : int
    dy : int
    
    def perform(self,engine:Engine,entity:Entity) -> None:
        dest_x = entity.x + self.dx
        dest_y = entity.y + self.dy

        if not engine.game_map.in_bounds(dest_x,dest_y):
            return
        if not engine.game_map.tiles["walkable"][dest_x,dest_y]:
            return

        entity.move(self.dx,self.dy)
