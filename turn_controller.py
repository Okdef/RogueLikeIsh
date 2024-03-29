#turn_controller
import attrs
from entities import Entity
from typing import TYPE_CHECKING
from entity_ai import AIController
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from entities import Entity


@attrs.define
class TurnController:
    aicontroller : AIController
    player : Entity
    control_mode : int = 1

    def __attrs_post_init__(self):
       self.control_mode = 1 
    

    def action_check(self, entity: Entity, cost:int = 1):
        ##TEMPORARY
        #self.aicontroller.enemy_turn()
        ##TEMPORARY

        entity.action_pool -= cost
        #print(entity.action_pool)
        if entity.action_pool == 0:
            self.next_turn()
        return

    def next_turn(self):
        if self.control_mode == 1:
            self.control_mode = 2
            self.aicontroller.enemy_turn()
            self.control_mode = 1
            self.player.action_pool = self.player.action_max
        return

    def get_control_mode(self) -> None:
        return self.control_mode

    def set_control_mode(self,value:int) -> None:
        self.control_mode = value