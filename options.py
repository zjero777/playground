import os
import pygame as pg
from os import path

img_dir = path.join(path.dirname(__file__), 'img')
data_dir = path.join(path.dirname(__file__), 'data')
fonts_dir = path.join(path.dirname(__file__), 'fonts')
ntt_dir = path.join(path.dirname(__file__), 'ntt')

datadir = 'data'

CONSOLE_HIGHT = 32

LAYER_BG = 0 # bg
LAYER_ACT_BG = 1 # active refresh background layer
LAYER_ST_MESH = 2 # static mesh layer
LAYER_ACT_SPRITE = 3 # active sprite layer
LAYER_DYN_HUD = 4 # dynamic hud - info layer
LAYER_ST_HUD = 5 # static hud layer
LAYER_INTERFACE = 6 # interface layer



if __name__ == 'options':
    pg.init()
    vidinfo = pg.display.Info()
    NATIVE_WIN_SIZE = (vidinfo.current_w, vidinfo.current_h)
    SCREEN_W = vidinfo.current_w
    SCREEN_H = vidinfo.current_h
    SCREEN_HALV_W = vidinfo.current_w // 2
    SCREEN_HALV_H = vidinfo.current_h // 2
