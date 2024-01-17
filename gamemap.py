#gamemap class
import numpy as np
import attrs
from tcod.console import Console
import tile_types


class GameMap:
    width : int
    def __init__(self,width:int,height:int):
        self.width = width 
        self.height = height
        self.tiles = np.full((width, height) , fill_value=tile_types.floor, order="F")
        
        self.tiles[30:33, 22] = tile_types.wall


    def in_bounds(self, x:int, y:int) -> bool:
        #returns true of x,y are inside map bounds
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, console:Console) -> None:
        console.tiles_rgb[0:self.width, 0:self.height] = self.tiles["dark"]

