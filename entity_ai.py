#entityai.py
#this will serve as the collection for all ai methods and classes
#on starting a turn I need a list of all entities and will iterate through it
#it will check each entity to see if the player is in LOS
#if player in LOS entity will path to player and attempt to attack player

import attrs
from typing import TYPE_CHECKING
from gamemap import GameMap


if TYPE_CHECKING:
    from engine import Engine

@attrs.define
class AIController:
    gamemap : GameMap
    
    def enemy_turn(self):
        enemy_list = self.gamemap.entities
        for entity in enemy_list:
            print(entity)