#actions
import attrs
import entities

@attrs.define
class Action:
    pass

@attrs.define
class EscapeAction(Action):
    action : Action

@attrs.define
class MovementAction(Action):
    dx : int
    dy : int
    
