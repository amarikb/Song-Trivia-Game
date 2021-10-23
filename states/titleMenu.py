from states.song_trivia import Song_Game
from states.state import State
from states.cat_sprite import Cat
import pygame,os
from states.info_menu import Info


class Title(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.game.state = "Title Menu"
        self.cat = Cat(self.game)
        

    def update(self, actions):
        if actions["info"]:
            new_state = Info(self.game)
            new_state.enter_state()

        if actions["play"]:
            new_state = Song_Game(self.game)
            new_state.enter_state()

        self.cat.update(actions)
        self.game.reset_keys()

    def render(self, display):
    
        sky = pygame.image.load(os.path.join(self.game.assets_graphics_dir,"background", "PixelSky44.png")).convert_alpha()
        sky = pygame.transform.scale(sky, (540,300))

        floor = pygame.image.load(os.path.join(self.game.assets_graphics_dir,"background", "PixelSky34.png")).convert_alpha()
        floor = pygame.transform.scale(floor, (540,300))

        display.blit(sky, (0,0))
        display.blit(floor, (0, 5)) 
        self.game.draw_text(display, "Song", (64,64,64), self.game.GAME_W/2  , self.game.GAME_H/2 - 70)
        self.game.draw_text(display, "Trivia", (64,64,64), self.game.GAME_W/2, self.game.GAME_H/2) 
        self.game.draw_text(display, "Game", (64,64,64), self.game.GAME_W/2, self.game.GAME_H/2 + 70)
        self.game.draw_text(display, "High Score: ", (255,255,102),320,10,30,"AvenuePixel-Regular.ttf")
        self.cat.render(display)


