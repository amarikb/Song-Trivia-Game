from states.state import State
import states.titleMenu
from states.cat_sprite import Cat
import pygame,os

class Song_Game(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.game.state = "Play Game"
         

    def update(self, actions):
        """
        if actions["title"]:
            new_state = states.titleMenu.Title(self.game)
            new_state.enter_state()
        """
            
        self.game.reset_keys()

    def render(self, display):
    
        background = pygame.image.load(os.path.join(self.game.assets_graphics_dir,"background", "PixelSky1.png")).convert_alpha()
        background = pygame.transform.scale(background, (540,300))
        display.blit(background, (0, 0)) 
        self.game.draw_text(display, "Game Page", (0,0,0), self.game.GAME_W/2, self.game.GAME_H/2 )
