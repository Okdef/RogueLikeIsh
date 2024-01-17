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
from gamemap import GameMap
from engine import Engine

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
    map_width = 60
    map_height = 40
    tcod.tileset.procedural_block_elements(tileset=tileset)
    console = tcod.console.Console(80,50)
    player = Entity(console.width //2, console.height //2, char="@", color=(255,255,255))
    npc = Entity(console.width//2 - 5, console.height//2 , "@", color = (255,255,0))
    entities = {npc,player}
    game_map = GameMap(map_width,map_height)

    event_handler = EventHandler()
    engine = Engine(entities=entities, event_handler=event_handler, game_map=game_map, player=player)


    with tcod.context.new(width=res_width, height=res_height, sdl_window_flags=res_flags, tileset=tileset, title="roguelikeish") as context:
        while game_active:
            console = context.new_console(order="F")
            console.clear() #clear console before drawing
            engine.render(console=console,context=context)
            events=tcod.event.wait()
            engine.handle_events(events)
            #context.present(console,integer_scaling=True) #present to console
            #context.present(console) #this renders the console to the window
            

if __name__ == "__main__":
    main()
