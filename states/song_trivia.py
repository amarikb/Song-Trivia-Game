from states.state import State
import states.titleMenu
from states.cat_sprite import Cat
import pygame,os,pygame_gui

class Song_Game(State):
    def __init__(self, game,lyrics,artist_name,song_name):
        State.__init__(self, game)
        self.game.state = "Play Game"
        self.lyrics = lyrics
        self.song_title = song_name
        self.artist = artist_name 
        self.load_lyric_box()       

    def update(self, actions):
        """TODO: DELETE STATE TO TITLE AND ADD WIN AND LOSE STATE HERE"""
        if actions["title"]:
            self.lyrics_container.hide()
            new_state = states.titleMenu.Title(self.game)
            new_state.enter_state()
            
        self.game.reset_keys()

    def render(self, display):
      
        background = pygame.image.load(os.path.join(self.game.assets_graphics_dir,"background", "PixelSky1.png")).convert_alpha()
        background = pygame.transform.scale(background, (540,300))
        display.blit(background, (0, 0)) 
        self.game.draw_text(display, "High Score: ", (0,0,0),320,10,30,"AvenuePixel-Regular.ttf")
        self.game.draw_text(display, "Score: ", (0,0,0),50,10,30,"AvenuePixel-Regular.ttf")
     
        
    
    def load_lyric_box(self):
           self.text = '<font size=5 font color=#E784A2><b>           Lyrics: </b><br><br></font><font>' + self.lyrics + "</font>"
           self.lyrics_container = pygame_gui.elements.UITextBox(self.text,
                             pygame.Rect(self.game.GAME_W/2-10  , self.game.GAME_H/2-10, 400, 280),
                             manager=self.game.manager)
    
     
    def display_score(self):
          pass

    def display_high_score():
          pass