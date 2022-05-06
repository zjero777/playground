import pygame as pg
from console import Console
from options import *

from playground import Playground
import pygame_gui

# init app
# init playground
# init graphic mode
# load assets
# run sequence command for create enviroment


class App:
    def __init__(self) -> None:
        self.is_runing = True
        pg.init()
        self.screen = pg.display.set_mode(NATIVE_WIN_SIZE, pg.SRCALPHA)
        self.manager = pygame_gui.UIManager(NATIVE_WIN_SIZE, path.join(data_dir, 'theme.json'))
        self.console = Console(self.manager)
        self.playground = Playground(self.screen)
        self.playground.append_console(self.console)
        # self.console.run('load auto.seq')
        self.console.run('add background')
        self.console.run('add camera')
        self.console.run('add player')
        self.console.run('add room')
        
        

    def run(self):
        while self.is_runing:
            # dt = self.clock.tick(FPS)/1000
            for event in pg.event.get():
                # check for closing window
                if event.type == pg.QUIT:
                    self.is_runing = False

                # if event.type == pg.USEREVENT:
                #     if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                #         if event.ui_element == 'panel.panel_info.button':
                #             print('Hello World!')
                # self.mouse.process_events(event)
                self.console.process_events(event)
                self.manager.process_events(event)

            dt = pg.time.Clock().tick(60)/1000.0
            self.manager.update(dt)
            self.update()
            self.draw()
            # fps = self.clock.get_fps()
            # self.info.debug((0,0), f'FPS:{int(fps)}')
            pg.display.update()

    def update(self):
        self.playground.update()
        cmd = self.console.update()
        if cmd:
            self.playground.command(cmd)

    def draw(self):
        self.screen.fill(pg.Color(0))
        self.playground.draw()
        self.manager.draw_ui(self.screen)

if __name__ == '__main__':
    app = App()
    app.run()
