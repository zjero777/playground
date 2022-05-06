from entity import *
from options import *
import pygame as pg
from os import path


class Background(Entity):
    def __init__(self, parent, data) -> None:
        super().__init__(parent, data)
        self.layer = LAYER_BG
        cfg = data['cfg']
        self.image = pg.image.load(path.join(img_dir, cfg['image']))
        self.rect = pg.Rect((0,0), NATIVE_WIN_SIZE)

    def draw(self, screen, pos):
        super().draw(screen, pos)
