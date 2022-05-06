from math import sqrt
import math
from random import randint
from entity import *
from options import *
import pygame as pg
from os import path


class Trigger_timer:
    def __init__(self, response_time) -> None:
        self.response_time = response_time
        self.time = 0
        self._worked = False
        self._start()

    def _start(self):
        self._worked = False
        self.time = pg.time.get_ticks()

    def _update(self):
        if pg.time.get_ticks()-self.time >= self.response_time:
            self._worked = True

    @property
    def worked(self) -> bool:
        self._update()
        if self._worked:
            self._start()
            return(True)


class Camera(Entity):
    def __init__(self, parent, data) -> None:
        super().__init__(parent, data)
        self.pos = pg.Vector2((SCREEN_HALV_W, SCREEN_HALV_H))
        self._pos = pg.Vector2((0.0, 0.0))
        self.parent.begin_pos = (
            round(-self.pos[0]+SCREEN_HALV_W), round(-self.pos[1]+SCREEN_HALV_H))

        self.dest_pos = None
        self.start_time = None
        self.arryval_time = None
        self.dest_reach = True
        
        # триггер на сработку каждую секунду
        self.trigger_timer = Trigger_timer(3000)

    def draw(self, screen, pos):
        super().draw(screen)

    def update(self):
        # if self.trigger_timer.worked:
        # self.jump_to((randint(0,1920), randint(0,1080)))
        # buttons = pg.mouse.get_pressed()
        # if buttons[0]:
        #     go_pos = (self.pos[0] + pg.mouse.get_pos()[0]-SCREEN_HALV_W,
        #               self.pos[1] + pg.mouse.get_pos()[1]-SCREEN_HALV_H)
        #     self.move_to(go_pos, 500)

        # self.move_to_update()
        # self.jump_to((SCREEN_HALV_W,SCREEN_HALV_H))

        self.move_to_update()
            
        return super().update()

    def jump_to(self, dest_pos):
        self.arryval_time = 0
        self.pos = pg.Vector2(dest_pos)
        self.parent.begin_pos = (-self.pos[0] +
                                 SCREEN_HALV_W, -self.pos[1]+SCREEN_HALV_H)

    def _InOutErp(self, n):
        return -0.5 * (math.cos(math.pi * n) - 1)

    def _distance(self, p1, p2):
        return round(sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2)))
    
    def move_to_update(self):
        # if not self._distance(self.pos, self.dest_pos):
        #     self.dest_reach = True
        

        if not self.arryval_time:
            return
        dt = pg.time.get_ticks() - self.start_time
        if dt > self.arryval_time:
            dt = self.arryval_time

        # dist = self._InOutErp(dt / self.arryval_time)
        dist = dt / self.arryval_time

        if dist > 1:
            dist2 = 1.0
            
        elif dist < 0:
            dist2 = 0.0
        else:
            dist2 = dist

        self.pos = pg.Vector2.lerp(self._pos, self.dest_pos, dist2)


        self.parent.begin_pos = (
            round(-self.pos[0]+SCREEN_HALV_W), round(-self.pos[1]+SCREEN_HALV_H))
        
        
    def move_to(self, dest_pos, speed):
        # if self.dest_reach:
        self._pos = pg.Vector2(self.pos)
        self.dest_pos = pg.Vector2(dest_pos)
        self.start_time = pg.time.get_ticks()
        self.arryval_time = (self._distance(
            self._pos, self.dest_pos) / (speed/1000))
        # self.dest_reach = False

