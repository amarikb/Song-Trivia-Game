from states.state import State
import states.titleMenu
from states.cat_sprite import Cat
import pygame,os,pygame_gui

class Info(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.game.state = "Info Menu"
        self.cat = Cat(self.game) 
        self.load_text_box()

    def update(self, actions):

        if actions["title"]:
            self.text_box.hide()
            new_state = states.titleMenu.Title(self.game)
            new_state.enter_state()
        
        self.cat.update(actions)    
        self.game.reset_keys()

    def render(self, display):
       
        background = pygame.image.load(os.path.join(self.game.assets_graphics_dir,"background", "PixelSky2.png")).convert_alpha()
        background = pygame.transform.scale(background, (540,300))

        
        display.blit(background, (0, 0)) 
       
        self.game.draw_text(display, "Song Trivia Game", (0,51,102), self.game.GAME_W/2 + 5, self.game.GAME_H/2 - 100, 30,"NicoClean-Regular.ttf")
        
        self.cat.render(display)
        

    def load_text_box(self):
       
         self.text_box = pygame_gui.elements.UITextBox('<font size=5 font color=#331900>♫<b>Welcome to the Song Trivia Game!♫</b></font><br>'
                             '<font size=4><b><br>           Objective of the game:</b><br>'
                              '<br><br>'
                              '                                                *The game will give you a lyric snippet from a random song. <br>'
                             '<br>                                                    *You have have three tries to guess the song name <br><br>'
                             '<br><br>' 
                             '                                               *If you guess wrong, the game will end.<br>'
                             '                                               *Every game, you can earn points by getting the correct song name and advance to the next song.'
                             '<br><br>' 
                             '<font size=5 font color=#331900>'
                             ' '
                             '  '
                             '      '
                             '♫♪Good Luck!♫♪<br><br>'
                              '</font><font><b>                                          **Warning:</b> There is a delay starting the game as the lyrics take time to load from api. Also some songs may not have lyrics so the game/next level will not start.</font>',
                              pygame.Rect(self.game.GAME_W/2 + 20, self.game.GAME_H/2 - 30, 450, 360),
                             manager=self.game.manager)
            
        
      
        
        
        

    
