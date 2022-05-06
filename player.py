from math import sqrt
import math
from random import randint
from camera import Camera
from entity import *
from options import *
import pygame as pg
from os import path


class Player(Entity):
    def __init__(self, parent, data) -> None:
        super().__init__(parent, data)
        self.layer = LAYER_ACT_SPRITE
        
        cfg = data['cfg']
        self.image = pg.image.load(path.join(img_dir, cfg['image'])).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.bottomright = (self.rect.w*3, self.rect.h*3)
        self.image = pg.transform.scale(self.image, self.rect.bottomright)
        
        self.pos = pg.Vector2((400,400))

    def draw(self, screen, pos):
        super().draw(screen, pos)

    def update(self):
        keystate = pg.key.get_pressed()
        dx = 0
        dy = 0
        if keystate[pg.K_a]:
            dx = -1
        if keystate[pg.K_d]:
            dx = 1
        if keystate[pg.K_w]:
            dy = -1
        if keystate[pg.K_s]:
            dy = 1
        self.pos = pg.Vector2((self.pos[0]+dx*4, self.pos[1]+dy*4))

        camera = self.parent.get_camera()
        if camera:
            camera.move_to((self.pos[0]+dx*SCREEN_HALV_W, self.pos[1]+dy*SCREEN_HALV_H), 200)
        
        return super().update()

