#Main thod Roguelikeish Project by Okdef Started 1/11/2024
#This project is a roguelike game built in python using libtcod python
# Library Documentation: https://python-tcod.readthedocs.io/en/latest/

from __future__ import annotations
import tcod.context#window manager
import tcod.tileset#tileset manager
import tcod.event
import tcod.console
import attrs #this is like datatypes
from entities import *
from typing import Optional
from actions import *
from input_handlers import *

#Main 
def main() -> None:
    #load tileset
    tileset = tcod.tileset.load_tilesheet(
        "data/Alloy_curses_12x12.png", columns = 16, rows = 16, charmap = tcod.tileset.CHARMAP_CP437
    )
    #res_specs
    res_width, res_height = 720, 480
    res_flags = tcod.context.SDL_WINDOW_RESIZABLE | tcod.context.SDL_WINDOW_MAXIMIZED
    game_active = True
    tcod.tileset.procedural_block_elements(tileset=tileset)
    console = tcod.console.Console(80,50)
    player = entities.Entity(console.width //2, console.height //2, char="@", color="WHITE")
    event_handler = EventHandler()


    with tcod.context.new(width=res_width, height=res_height, sdl_window_flags=res_flags, tileset=tileset, title="roguelikeish") as context:
        while game_active:
            console = context.new_console(order="F")
            console.clear() #clear console before drawing
            console.print(player.x,player.y,player.char)
            context.present(console,integer_scaling=True) #present to console
            context.present(console) #this renders the console to the window
            for event in tcod.event.wait(): #this waits until pending events 'exist'
                action = event_handler.dispatch(event)
                
                if action is None:
                    continue
                    
                if isinstance(action,MovementAction):
                    player.x += action.dx
                    player.y += action.dy
                
                elif isinstance(action,EscapeAction):
                    raise SystemExit()


if __name__ == "__main__":
    main()
