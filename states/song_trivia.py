from states.state import State
from states.pausemenu import Pause
from states.winmenu import Win
from states.losemenu import Lose
import pygame,os,pygame_gui

class Song_Game(State):
    """
    A state class to represent the guessing game page.
    displays game info to play the game and guess the song name after loading.
    """
    def __init__(self, game,lyrics,artist_name,song_name,song_img):
        State.__init__(self, game)
        self.game.state = "Play Game"
        self.tries_left = 3
        
        self.lyrics = lyrics.strip().replace("\n", ". ")
        self.song_title = song_name.strip().lower() 
        self.artist = artist_name 
        self.img = song_img
        
        self.load_lyric_containers()  
       

    def update(self, actions):

        self.play_game(actions)
        if actions["pause"]:
            new_state = Pause(self.game)
            new_state.enter_state()

        if actions["win"]:
            self.lyrics_container.hide()
            new_state = Win(self.game,self.artist,self.song_title,self.img)
            new_state.enter_state()
        
        if actions["lose"]:
            self.hide_gui_elements()
            new_state = Lose(self.game,self.artist,self.song_title,self.img)
            new_state.enter_state()

        self.game.reset_keys()

    def render(self, display):
        background = pygame.image.load(os.path.join(self.game.assets_graphics_dir,"background", "PixelSky1.png")).convert_alpha()
        background = pygame.transform.scale(background, (540,300))
        display.blit(background, (0, 0)) 

        if(self.game.state != "Lose"):
            self.game.draw_text(display, "High Score: ", (0,0,0),300,10,30,"AvenuePixel-Regular.ttf")
            self.game.draw_text(display, str(self.game.high_score), (0,0,0),355,12,30,"AvenuePixel-Regular.ttf")
            self.game.draw_text(display, "Score: ", (0,0,0),50,10,30,"AvenuePixel-Regular.ttf")
            self.game.draw_text(display, str(self.game.current_score), (0,0,0),85,12,30,"AvenuePixel-Regular.ttf")
        self.game.draw_text(display, "Tries Left: ", (0,76,153),163,50,20,"NicoPups-Regular.ttf")
        self.game.draw_text(display,str(self.tries_left),(0,0,0),215,50,20,"NicoPups-Regular.ttf")
     
        
    
    def load_lyric_containers(self):
           """
            Displays all the required game gui for guessing the song name (lyrics, text box, guess button)
           """
           self.text = '<font size=6 font color=#E784A2><b>         Lyrics: </b><br><br></font><font>' + self.lyrics + "</font>"

           self.lyrics_container = pygame_gui.elements.UITextBox(self.text,
                             pygame.Rect(self.game.GAME_W/2-10  , self.game.GAME_H/2-10, 400, 280),
                             manager=self.game.manager)
            
           self.text_box = pygame_gui.elements.UITextEntryLine(pygame.Rect((self.game.GAME_W/2 + 40  , 450),
                                                                          (300, 50)),
                                                              manager=self.game.manager)
           self.guess_label = pygame_gui.elements.UILabel(pygame.Rect((self.text_box.rect.width - 55,
                                                                    452), (50,self.text_box.rect.height -3.8)),
                                                        "Guess:",
                                                        manager=self.game.manager)
           self.submit_guess_button = pygame_gui.elements.UIButton(pygame.Rect((584, 450),
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
        """
          Implements guessing game and gets user's guess and determines if it matches song name/
          User loses if number of tries reaches 0 or wins if guess is correct.
        """
        guess = ""
        if(self.submit_guess_button.check_pressed()):
            guess = self.text_box.get_text()
            if guess == "":
                pass
            else:
               if guess.strip().lower() == self.song_title:
                   self.add_score()
                   self.check_high_score()
                   actions["win"] = True
                
               else:
                   self.tries_left -= 1
    
        if self.tries_left == 0:
         self.check_high_score()
         actions["lose"] = True

    
    def add_score(self):
        self.game.current_score +=10

    def check_high_score(self):
        if self.game.current_score > self.game.high_score:
            self.game.high_score = self.game.current_score

