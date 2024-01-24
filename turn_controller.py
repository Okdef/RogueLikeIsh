#turn_controller
import attrs
from entities import Entity


@attrs.define
class TurnController:
    control_mode : int = 1

    def __attrs_post_init__(self):
       self.control_mode = 1 
    

    def action_check(self, entity: Entity, cost:int = 1):
        entity.action_pool -= cost
        print("ACTION")
        if entity.action_pool == 0:
            self.next_turn()
        return

    def next_turn(self):
        if self.control_mode ==1:
            self.control_mode = 2
        elif self.control_mode == 2:
            self.control_mode = 1
            engine.player.action_pool = engine.player.action_max
        return