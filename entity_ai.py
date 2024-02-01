#entityai.py
#this will serve as the collection for all ai methods and classes
#on starting a turn I need a list of all entities and will iterate through it
#it will check each entity to see if the player is in LOS
#if player in LOS entity will path to player and attempt to attack player

import attrs
from typing import TYPE_CHECKING
from gamemap import GameMap
from tcod.map import compute_fov
import tcod
from entities import Entity
from tcod import *
from time import sleep
from tcod.console import Console
from renderer import Renderer

if TYPE_CHECKING:
    from engine import Engine

@attrs.define
class AIController:
    gamemap : GameMap
    player : Entity
    renderer : Renderer = None

    
    def enemy_turn(self):
        enemy_list = self.gamemap.entities
        for entity in enemy_list:
            in_fov = self.enemy_fov_check(entity)
            if in_fov is not None:
                entity.action_pool = entity.action_max
                graph = tcod.path.SimpleGraph(cost=self.gamemap.cost_map, cardinal=1, diagonal=0)
                pathfinder = tcod.path.Pathfinder(graph)
                pathfinder.add_root((entity.x,entity.y))
                pathfinder.resolve()
                path_to_target = pathfinder.path_to(in_fov).tolist()
                self.enemy_move(entity, path_to_target,self.gamemap)
        


    def enemy_fov_check(self,entity):#returns playerx,playery or None
        enemy_fov = compute_fov(
            self.gamemap.tiles["transparent"],
            (entity.x, entity.y),
            radius = 8,
            algorithm=tcod.FOV_BASIC
        )
        if enemy_fov[self.player.x, self.player.y]:
            return self.player.x, self.player.y
        else:
            return None

    def enemy_move(self,entity, path_to_target,gamemap)->None:
        if len(path_to_target) > 1:
            while entity.action_pool > 0 and len(path_to_target) > 2:
                path_to_target.pop(0)
                entity.x , entity.y = path_to_target[0][0], path_to_target[0][1] 
                entity.action_pool -= 1
                #try to create an event here
                self.renderer.fullmap_render()
                sleep(5/len(gamemap.entities))
            if len(path_to_target) == 2:
                self.enemy_attack(entity)
                print("attacking!!!")

    def enemy_attack(self,entity):
        entity.damage(self.player,1)