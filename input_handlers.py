#inputhandler.py
from typing import Optional
import attrs
import tcod.event
from actions import Action, EscapeAction, MovementAction

@attrs.define 
class EventHandler(tcod.event.EventDispatch[Action]):
    
    def ev_quit(self,event : tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()
        
    def ev_keydown(self, event : tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None

        key = event.sym

        match key:
            case tcod.event.K_UP:
                action = MovementAction(dx = 0, dy = -1)
            case tcod.event.K_DOWN:
                action = MovementAction(dx = 0, dy = 1)
            case tcod.event.K_LEFT:
                action = MovementAction(dx = -1, dy = 0)
            case tcod.event.K_RIGHT:
                action = MovementAction(dx = 1, dy = 0)

            case tcod.event.K_ESCAPE: #EscapeAction
                action = EscapeAction()

            #if none pressed
        return action