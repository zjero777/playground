import pygame as pg
from background import *
from camera import Camera
from options import *
from player import Player

class Playground:
    def __init__(self, screen):
        self.console = None
        self.screen = screen
        self.entities = []
        self.begin_pos = (0,0)
    
    def append_console(self, console):
        self.console = console
    
    def update(self):
        for ntt in self.entities:
            ntt.update()
    
    def draw(self):

        # background layer
        for ntt in self.entities:
            if ntt.layer == LAYER_BG:
                ntt.draw(self.screen, self.begin_pos)
                
                
            # active refresh background layer
            # static mesh layer
            
            # active sprite layer
        for ntt in self.entities:
            if ntt.layer == LAYER_ACT_SPRITE:
                ntt.draw(self.screen, self.begin_pos)
            
            # dynamic hud - info layer
            
            # static hud layer
            
            # interface layer
        # pg.draw.line(self.screen, pg.Color('#FF0000'), (0,0), (1000,1000), 4)

    def command(self, cmd):
        entity = None
        command = cmd.split(" ")
        match command:
            case 'load', param:
                self.console.print(f'loading {param}...<br>')
                self.console.print('done.<br>')
            case 'add', param:
                self.console.print(f'adding {param}...<br>')
                filename = os.path.abspath(os.path.join(ntt_dir, param+'.json'))
                entity = self.console.create_from_file(filename, self)
            case 'adasd':
                pass
            case _:
                self.console.print(f'Неизвестная команда<br>')  
                
        cmd = ''       
        
        if entity:
            self.entities.append(entity)
            self.console.print('done.<br>')
        else:
            self.console.print('Enetety not be append.<br>')
            
    def get_player(self) -> Player:
        for ntt in self.entities:
            if ntt.etype == 'PL':
                return ntt
        
    def get_camera(self) -> Camera:
        for ntt in self.entities:
            if ntt.etype == 'CAM':
                return ntt
            
    def get_enteties_by_type(self, entity_type):
        result = []
        for ntt in self.entities:
            if ntt.etype == entity_type:
                result.append(ntt)
        return result
        
        