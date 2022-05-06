from turtle import backward
from background import Background
from entity import *
from options import *
import pygame as pg
from os import path


class Room(Entity):
    def __init__(self, parent, data) -> None:
        super().__init__(parent, data)
        cfg = data['cfg']
        self.loop_w = cfg['loop_w']
        self.loop_h = cfg['loop_h']
        # mod background
        bg_list = self.parent.get_enteties_by_type('BG')
        self.set_loop_image(bg_list)
        # mod camera 
        camera = self.parent.get_camera()
        self.set_camera_loop(camera)
        
        # mod player pos
        player = self.parent.get_player()
        player.pos = self.set_correct_loop_pos(player.pos)
        # camera.jump_to(player.pos)
        

    def update(self):
        
        
        return super().update()
    
    def set_loop_image(self, bg_list):
        for bg in bg_list:
            image_rect = pg.Rect((0,0), NATIVE_WIN_SIZE)
            new_image_rect = image_rect.inflate(image_rect.w, image_rect.h)
            new_image_rect.topleft = (0,0)
            new_surf = pg.surface.Surface(new_image_rect.size, flags=pg.SRCALPHA)
            new_surf.fill(pg.Color('black'))
            new_surf.blit(bg.image, (0,0))
            new_surf.blit(bg.image, (image_rect.w,0))
            new_surf.blit(bg.image, (0,image_rect.h))
            new_surf.blit(bg.image, (image_rect.w,image_rect.h))
            bg.image = new_surf

    def set_camera_loop(self, camera):
        #  set move_to loop coord 
        camera._pos = self.set_correct_loop_pos(camera._pos)
        camera.dest_pos = self.set_correct_loop_pos(camera.dest_pos)
        # camera.pos = self.set_correct_loop_pos(camera.pos)
        

    def set_correct_loop_pos(self, pos):
        if pos[0]<=SCREEN_HALV_W:
            pos[0]=SCREEN_W+pos[0]
        elif pos[0]>SCREEN_HALV_W+SCREEN_W:
            pos[0]=SCREEN_HALV_W
        if pos[1]<=SCREEN_HALV_H:
            pos[1]=SCREEN_H+pos[1]
        elif pos[1]>SCREEN_HALV_H+SCREEN_H:
            pos[1]=SCREEN_HALV_H  
            
        return pos          