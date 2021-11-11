from states.state import State
import pygame,os
import states.titleMenu 

class Pause(State):
    def __init__(self, game):
        """
             A state class to represent a menu when the game is paused.
             displays buttons to navigate throughtout the game.
        """
        pygame.mixer.music.pause()
        self.game = game
        State.__init__(self, game)
        self.game.state = "Pause"
        self.pause_menu = pygame.image.load(os.path.join(self.game.assets_graphics_dir,"background", "pausemenu.png"))
        self.pause_menu_rect = self.pause_menu.get_rect()
        self.pause_menu_rect.center = (self.game.GAME_W*.80, self.game.GAME_H*.4)

    def update(self, actions):
        if actions["title"]:
            self.prev_state.hide_gui_elements()
            pygame.mixer.music.unpause()
            new_state = states.titleMenu.Title(self.game)
            new_state.enter_state()

        if actions["unpause"]:
            pygame.mixer.music.unpause()
            self.game.state = 'Play Game'
            self.exit_state()

        if actions['restart']:
            pygame.mixer.music.unpause()    
            new_state = states.loading.Loading(self.game)
            new_state.enter_state()
            
        self.game.reset_keys()

    def render(self, display):
        self.prev_state.render(display)
        display.blit(pygame.transform.scale(self.pause_menu, (130,150)), self.pause_menu_rect)
        self.game.draw_text(display, "Paused",(0,0,0),self.game.GAME_W*.82, self.game.GAME_H*.29,30,"AvenuePixel-Regular.ttf")
        
    