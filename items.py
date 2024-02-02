import attrs
from entities import Entity
import copy


@attrs.define
class Item:
    name: str = "<UnnamedItem>"
    location: list = None
    ability: callable = lambda: None #this is the functionality of the item when it is activated
    equippable: bool = False

    def spawn(self):
        clone = copy.deepcopy(self)
        return clone

    def healing(self, user:Entity, hp_restored:int = 1):
        if user.hp_current < user.hp_most:
            user.hp_current += 1

    def use(self, location):
        location.remove(self)
