from collections import deque
import pygame_gui as gui
import pygame as pg
from background import Background
from camera import Camera
from options import *
import json

from player import Player
from room import Room

class Console:
    def __init__(self, manager) -> None:
        self.hight = 0
        self.visible = False
        self.one_pressed = False
        self.command = deque()
        self.input = gui.elements.UITextEntryLine(
            pg.Rect(0, NATIVE_WIN_SIZE[1]-CONSOLE_HIGHT,
                    NATIVE_WIN_SIZE[0], CONSOLE_HIGHT),
            manager,
            visible=self.visible,
            object_id='wnd_console'
        )
        self.input.set_forbidden_characters(['`'])
        self.output = gui.elements.UITextBox('',
                                             pg.Rect(
                                                 0, 0, NATIVE_WIN_SIZE[0], NATIVE_WIN_SIZE[1]-CONSOLE_HIGHT),
                                             manager,
                                             visible=self.visible,
                                             object_id='wnd_console'
                                             )
        self.input.focus()

    def process_events(self, event):
        # check for closing window
        if event.type == pg.KEYDOWN:
            if not self.one_pressed:
                if event.key == pg.K_BACKQUOTE:
                    one_pressed = True
                    if not self.visible:
                        self.open()
                    else:
                        self.close()
                if event.key == pg.K_RETURN:
                    one_pressed = True
                    if self.input.get_text():
                        # self.command = self.input.get_text()
                        self.run(self.input.get_text())
                        self.input.set_text('')
                        # self.print(f'{self.command}<br>')

        if event.type == pg.KEYUP:
            one_pressed = False

    def update(self):
        if not self.command:
            return
        cmd = self.command.popleft()
        return(cmd)

    def open(self):
        self.visible = True
        self.input.show()
        self.output.show()

    def close(self):
        self.visible = False
        self.input.hide()
        self.output.hide()

    def print(self, arg):
        self.output.append_html_text(arg)

    def run(self, cmd):
        self.print(f'{cmd}<br>')
        self.command.append(cmd)

    def create_from_file(self, filename, parent):
        entity = None
        with open(filename, "r") as read_file:
            data = json.load(read_file)
            cfg = data['cfg']
            self.print(f'{data}<br>')
            if data['type']=='BG':
                entity = Background(parent, data)
            if data['type']=='CAM':
                entity = Camera(parent, data)
            if data['type']=='PL':
                entity = Player(parent, data)
            if data['type']=='TS':
                if data['class']=='room':
                    entity = Room(parent, data)
                
            return(entity)                    
            
