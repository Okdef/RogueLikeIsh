from entities import Entity

player = Entity(char="@", color=(255,255,255), name="Player", blocks_movement=True)

orc = Entity(char="o", color=(63,127,63), name="Orc",blocks_movement=True, hp_least=1,hp_most=2)
troll = Entity(char="T", color=(0,127,0),name="Troll",blocks_movement=True,hp_least=2, hp_most=3)