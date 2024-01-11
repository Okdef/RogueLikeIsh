from __future__ import annotations

import attrs
import tcod.console
import tcod.context
import tcod.event
import tcod.tileset

@attrs (eq = False)
class Game_State:
    player_pos_x : int
    player_pos_y : int

    def on_draw(self, console:tcod.console.Console) -> None:
        console.print(self.player_pos_x, self.player_pos_y, "@")