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


class ActionWithDirection:
    def __init__(self,dx:int, dy:int):
        super().__init__()

        self.dx = dx
        self.dy = dy

class MeleeAction(ActionWithDirection):#This function finds the target in the movement direction and if it is a valid target calls the damage function
    def perform(self,engine:Engine, entity:Entity) -> None:
        dest_x = entity.x + self.dx
        dest_y = entity.y + self.dy
        target = engine.game_map.get_blocking_entity_at_location(dest_x, dest_y)
        if not target:
            return
        entity.damage(target, 1)
        engine.turncontroller.action_check(entity)

def perform(self, engine:Engine, entity:Entity) -> None:
    raise NotImplementedError()    


class MovementAction(ActionWithDirection):    
    
    def perform(self,engine:Engine,entity:Entity) -> None:
        dest_x = entity.x + self.dx
        dest_y = entity.y + self.dy

        if not engine.game_map.in_bounds(dest_x,dest_y):
            return
        if not engine.game_map.tiles["walkable"][dest_x,dest_y]:
            return
        if engine.game_map.get_blocking_entity_at_location(dest_x,dest_y):
            return#

        entity.move(self.dx,self.dy)
        engine.turncontroller.action_check(entity)



class BumpAction(ActionWithDirection):
    def perform(self,engine:Engine, entity:Entity) -> None:
        dest_x = entity.x + self.dx
        dest_y = entity.y + self.dy

        if engine.game_map.get_blocking_entity_at_location(dest_x,dest_y):
            return MeleeAction(self.dx, self.dy).perform(engine,entity)

        else:
            return MovementAction(self.dx,self.dy).perform(engine,entity)

class MenuMove(ActionWithDirection):
    def perform(self, engine: Engine, entity:Entity) -> None:
        print(f"MenuMove: Selection moved to NULL")

@attrs.define
class OpenMenu(Action):
    def perform(self, engine: Engine,entity:Entity) -> None:
        print("OpenMenu: Menu opened")
        engine.renderer.render_toggle_inventory()
        # Add your menu opening logic here


@attrs.define
class CloseMenu(Action):
    def perform(self, engine:Engine,entity:Entity) -> None:
        engine.renderer.render_toggle_inventory()
        print("CloseMenu: Menu closed")