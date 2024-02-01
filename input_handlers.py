#inputhandler.py
from typing import Optional
import attrs
import tcod.event
from actions import Action, BumpAction, EscapeAction, OpenMenu, CloseMenu, MenuMove
from turn_controller import TurnController

@attrs.define 
class EventHandler(tcod.event.EventDispatch[Action]):
    turn_controller : TurnController = None

    def __attrs_post_init__(self):
        self.turn_controller = None
    
    def ev_quit(self,event : tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()
        
    def ev_keydown(self, event : tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None

        key = event.sym

        if self.turn_controller.control_mode == 1:#World_Controls
            match key:
                case tcod.event.K_UP:
                    action = BumpAction(dx = 0, dy = -1)
                case tcod.event.K_DOWN:
                    action = BumpAction(dx = 0, dy = 1)
                case tcod.event.K_LEFT:
                    action = BumpAction(dx = -1, dy = 0)
                case tcod.event.K_RIGHT:
                    action = BumpAction(dx = 1, dy = 0)
                case tcod.event.K_i:
                    self.turn_controller.control_mode = 3
                    action = OpenMenu()
                case tcod.event.K_ESCAPE: #EscapeAction
                    action = EscapeAction()

        elif self.turn_controller.control_mode == 3:#inventory_controls
            match key:
                case tcod.event.K_UP:
                    action = MenuMove(dx = 0, dy = 1)
                case tcod.event.K_DOWN:
                    action = MenuMove(dx = 0, dy = -1)
                case tcod.event.K_i:
                    self.turn_controller.control_mode = 1
                    action = CloseMenu()
                case tcod.event.K_ESCAPE: #EscapeAction
                    self.turn_controller.control_mode = 1
                    action = CloseMenu()

            #if none pressed
        return action

    