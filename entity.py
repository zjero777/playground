from os import path
from options import *



"""
visual
[BG]bg - bg all, changer bg... 
[PL] - player
[SSP]static sprites - wood, wall and etc
[MSP]motion sprites - obj, bullet and etc
[HUD]hud - interface, info hp bars and etc

non visual
[CAM]camera 
[PR]property - HP, STR, DMG, DEF, coords
[EV]event - triggers, condition and etc
[CTR]controls - player, ai and etc
[SND]sound
[TS]task - code, script and etc
"""


class Entity:
    def __init__(self, parent, data) -> None:
        self.parent = parent #ref to root entity
        self.image = None
        self.layer = None
        self.etype = data['type']
        self.pos = (0,0)
        
        self.after_mod_execute = None
        self.post_mod_execute = None

        
    def update(self):
        pass
    
    def draw(self, screen, pos):
        draw_pos = (pos[0]+self.pos[0], pos[1]+self.pos[1])
        if self.image:
            screen.blit(self.image, draw_pos)        
    

        
    