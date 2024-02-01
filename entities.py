from __future__ import annotations

import copy
from typing import Tuple, TypeVar, TYPE_CHECKING
import attrs
import tcod.console
import tcod.context
import tcod.event
import tcod.tileset
from random import randrange
from inventory import Inventory

if TYPE_CHECKING:
    from gamemap import GameMap

T = TypeVar("T", bound="Entity")

class Entity:
    def __init__(
        self,
        x: int = 0,
        y: int = 0,
        char: str = "?",
        color: Tuple[int,int,int] = (255,255,255),
        name: str = "<Unnamed>",
        blocks_movement: bool = False,
        hp_most: int = 0, #these are used for the hp pool generation, not used in gameplay
        hp_least: int = 0,
        action_max: int = 3,
        bag : Inventory = []
    ):
        self.x = x 
        self.y = y
        self.char = char
        self.color = color
        self.name = name
        self.blocks_movement = blocks_movement
        self.hp_most = hp_most
        self.hp_least = hp_least
        self.hp_current = 0
        self.map = None
        self.action_max = action_max
        self.action_pool = self.action_max

        
        

    def spawn(self: T, gamemap: GameMap, x: int, y: int) -> T:
        clone = copy.deepcopy(self)
        clone.x = x
        clone.y = y
        clone.map = gamemap
        if clone.hp_most != 0:
            clone.hp_current = randrange(clone.hp_least,clone.hp_most)
        gamemap.entities.add(clone)
        return clone


    def move(self, dx:int, dy:int) -> None:
        self.x += dx
        self.y += dy
    
    def damage(self, target:Entity, damage=0):
        if target.hp_current > 0:
            target.hp_current -= damage
            print(f"{self.name} attacks dealing {damage} damage to {target.name}")
            if target.hp_current <= 0:
                target.death()
    

    def death(self):
        print(f"{self.name} has died")
        self.map.entities.remove(self)
        