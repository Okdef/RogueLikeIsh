from __future__ import annotations

import attrs
import tcod.console
import tcod.context
import tcod.event
import tcod.tileset

@attrs.define(eq = False)
class Entity:
    x : int
    y : int
    char : str
    color : str

    def move(self, dx:int, dy:int) -> None:
        self.x += dx
        self.y += dy
    