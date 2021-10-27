from states.state import State
import states.titleMenu
from states.cat_sprite import Cat
import pygame,os,pygame_gui

class Song_Game(State):
    def __init__(self, game,lyrics,artist_name,song_name):
        State.__init__(self, game)
        self.game.state = "Play Game"
        self.num_of_guesses = 0
        self.tries_left = 3
        self.lyrics = lyrics.strip().replace("\n", ". ")
        self.song_title = song_name
        self.artist = artist_name 
        self.load_lyric_containers()       

    def update(self, actions):
        """TODO: DELETE STATE TO TITLE AND ADD WIN AND LOSE STATE HERE"""
        self.play_game(actions)
        if actions["title"]:
            self.hide_gui_elements()
            new_state = states.titleMenu.Title(self.game)
            new_state.enter_state()

        if actions["win"]:
            self.hide_gui_elements()
            #ADD WAY TO GO TO WIN STATE HERE
        
        if actions["lose"]:
            self.hide_gui_elements()
           #ADD WAY TO GO TO LOSE STATE HERE
        self.game.reset_keys()

    def render(self, display):
      
        background = pygame.image.load(os.path.join(self.game.assets_graphics_dir,"background", "PixelSky1.png")).convert_alpha()
        background = pygame.transform.scale(background, (540,300))
        display.blit(background, (0, 0)) 
        self.game.draw_text(display, "High Score: ", (0,0,0),320,10,30,"AvenuePixel-Regular.ttf")
        self.game.draw_text(display, str(self.game.high_score), (0,0,0),370,12,30,"AvenuePixel-Regular.ttf")
        self.game.draw_text(display, "Score: ", (0,0,0),50,10,30,"AvenuePixel-Regular.ttf")
        self.game.draw_text(display, str(self.game.current_score), (0,0,0),85,12,30,"AvenuePixel-Regular.ttf")
        self.game.draw_text(display, "Tries Left: ", (0,76,153),163,50,20,"NicoPups-Regular.ttf")
        self.game.draw_text(display,str(self.tries_left),(0,0,0),215,50,20,"NicoPups-Regular.ttf")
     
        
    
    def load_lyric_containers(self):
           self.text = '<font size=5 font color=#E784A2><b>           Lyrics: </b><br><br></font>' + self.lyrics 
        
           self.lyrics_container = pygame_gui.elements.UITextBox(self.lyrics,
                             pygame.Rect(self.game.GAME_W/2-10  , self.game.GAME_H/2-10, 400, 280),
                             manager=self.game.manager)
            
           self.text_box = pygame_gui.elements.UITextEntryLine(pygame.Rect((self.game.GAME_W/2 + 45  , 450),
                                                                          (300, 50)),
                                                              manager=self.game.manager)
           self.guess_label = pygame_gui.elements.UILabel(pygame.Rect((self.text_box.rect.width - 50,
                                                                    452), (50,self.text_box.rect.height -3)),
                                                        "Guess:",
                                                        manager=self.game.manager)
           self.submit_guess_button = pygame_gui.elements.UIButton(pygame.Rect((589, 450),
                                                                    (75, self.text_box.rect.height)),
                                                        'submit',
                                                        manager=self.game.manager,
                                                        object_id='#game_button')

    def hide_gui_elements(self):
         self.lyrics_container.hide()
         self.text_box.hide()
         self.guess_label.hide()
         self.submit_guess_button.hide()
        

    def play_game(self,actions):
    
        if(self.submit_guess_button.check_pressed()):
            if self.text_box.get_text() == "":
                pass

            else:
               if self.text_box.get_text() == self.song_title:
                   self.add_score()
                   actions["win"] = True
                
               else:
                    self.tries_left -= 1
    
        if self.tries_left == 0:
         actions["lose"] = True
    

    def add_score(self):
        self.game.current_score +=10

