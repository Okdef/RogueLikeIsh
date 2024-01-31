#This file controls the tile types for world generation

import attrs
from typing import Tuple

import numpy as np

graphic_dt = np.dtype(
    [
        ("ch",np.int32),
        ("fg","3B"),
        ("bg","3B"),
    ]
)

tile_dt = np.dtype(
[
    ("walkable",bool),
    ("transparent",bool),
    ("dark", graphic_dt),#Tile not in FOV
    ("light", graphic_dt),#tile in FOV
    ("cost", int)
]
)

def new_tile(
    *,
    walkable:int,
    transparent:int,
    dark:Tuple[int,Tuple[int,int,int],Tuple[int,int,int]],
    light:Tuple[int,Tuple[int,int,int],Tuple[int,int,int]],
    cost: int = 0,
)->np.ndarray:
        return np.array((walkable, transparent, dark, light, cost), dtype=tile_dt)

SHROUD = np.array((ord(" "), (255,255,255), (0,0,0)), dtype=graphic_dt)

floor = new_tile(
    walkable=True,
    transparent=True,
    dark=(ord(" "), (255,255,255),(50,50,150)),
    light=(ord(" "), (255,255,255), (200,180,50)),
    cost=1
)
wall = new_tile(
    walkable=False,
    transparent=False,
    dark=(ord(" "), (255,255,255),(0,0,100)),
    light=(ord(" "), (255,255,55), (130,110,50)),
    cost = 0,
)

