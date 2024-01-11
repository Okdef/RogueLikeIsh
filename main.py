#Main Method Roguelikeish Project by Okdef Started 1/11/2024
#This project is a roguelike game built in python using libtcod python
# Library Documentation: https://python-tcod.readthedocs.io/en/latest/

from __future__ import annotations
import tcod.context#window manager
import tcod.tileset#tileset manager
import tcod.event
import tcod.console
import attrs #this is like datatypes
from entity import Game_State

#Main 
def main() -> None:
    #load tileset
    tileset = tcod.tileset.load_tilesheet(
        "data/Alloy_curses_12x12.png", columns = 16, rows = 16, charmap = tcod.tileset.CHARMAP_CP437
    )


    game_active = True
        #tcod.context is the window manager for the tcod package
    tcod.tileset.procedural_block_elements(tileset=tileset)
    console = tcod.console.Console(80,50)
    state = Game_State(player_pos_x = console.width //2, player_pos_y = console.height // 2)
    with tcod.context.new(console = console, tileset=tileset) as context:
        while game_active:
            console.clear() #clear console before drawing
            state.on_draw(console) #draw current state
            context.present(console) #present to console
            context.present(console) #this renders the console to the window
            for event in tcod.event.wait(): #this waits until pending events 'exist'
                print(event)
                if isinstance(event, tcod.event.Quit):
                    raise SystemExit()








if __name__ == "__main__":
    main()
