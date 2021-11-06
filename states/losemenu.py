from states.state import State
import pygame,os,requests
import states.titleMenu 
import states.loading
from states.cat_sprite import Cat
import io

class Lose(State):
    def __init__(self, game, artist, song, img):
        pygame.mixer.music.pause()
        self.game = game
        State.__init__(self, game)
        self.game.state = "Lose"
        
        self.lose_menu = pygame.image.load(os.path.join(self.game.assets_graphics_dir,"background", "winlosemenu.png"))
        
        self.artist_name = artist
        self.song_name = song
        img_request = requests.get(img)
        img_bytes = io.BytesIO(img_request.content)
        self.song_img = pygame.image.load(img_bytes)
    
        pygame.mixer.Sound.play(self.game.lose_sound)

    def update(self, actions):
        if actions["title"]:
            pygame.mixer.music.unpause()
            new_state = states.titleMenu.Title(self.game)
            new_state.enter_state()

        if actions["restart"]:
            pygame.mixer.music.unpause()    
            new_state = states.loading.Loading(self.game)
            new_state.enter_state()

        self.game.reset_keys()

    def render(self, display):
        self.prev_state.render(display)
        display.blit(pygame.transform.scale(self.lose_menu, (218,160)),  (130,63))
        display.blit(pygame.transform.scale(self.song_img, (65,65)), (200,105))
        self.game.draw_text(display, "Game Over!",(153,0,76),238,78,26,"AvenuePixel-Regular.ttf")

        self.game.draw_text(display, "Score:", (51,102,204),155,95,20,"AvenuePixel-Regular.ttf")
        self.game.draw_text(display, str(self.game.current_score), (0,0,0),180,96,20,"AvenuePixel-Regular.ttf")
        self.game.draw_text(display, "High Score:", (51,102,204),255,95,20,"AvenuePixel-Regular.ttf")
        self.game.draw_text(display, str(self.game.high_score), (0,0,0),295,96,20,"AvenuePixel-Regular.ttf")
       
        
        
        self.game.draw_text(display, "Song Name: {}".format(self.song_name), (0,0,0),233,177,14,"AvenuePixel-Regular.ttf")
        self.game.draw_text(display, "Artist: {}".format(self.artist_name), (0,0,0),233,197,14,"AvenuePixel-Regular.ttf")