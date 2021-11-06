from states.state import State
import pygame,os,requests
import states.titleMenu 
import states.loading
from states.cat_sprite import Cat
import io

class Win(State):
    def __init__(self, game, artist, song, img):
        pygame.mixer.music.pause()
        self.game = game
        State.__init__(self, game)
        self.game.state = "Win"
        self.win_menu = pygame.image.load(os.path.join(self.game.assets_graphics_dir,"background", "winlosemenu.png"))
        self.artist_name = artist
        self.song_name = song
        img_request = requests.get(img)
        img_bytes = io.BytesIO(img_request.content)
        self.song_img = pygame.image.load(img_bytes)
        pygame.mixer.Sound.play(self.game.win_sound)

    def update(self, actions):
        if actions["title"]:
            pygame.mixer.music.unpause()
            self.prev_state.hide_gui_elements()
            new_state = states.titleMenu.Title(self.game)
            new_state.enter_state()

        if actions["play"]:
            pygame.mixer.music.unpause()
            self.prev_state.hide_gui_elements()
            new_state = states.loading.Loading(self.game)
            new_state.enter_state()

        self.game.reset_keys()

    def render(self, display):
        self.prev_state.render(display)
        display.blit(pygame.transform.scale(self.win_menu, (218,160)),  (130,63))
        display.blit(pygame.transform.scale(self.song_img, (65,65)), (200,105))
        self.game.draw_text(display, "You got it Right!",(51,102,204),238,78,25,"AvenuePixel-Regular.ttf")
        self.game.draw_text(display, "+10 Points", (153,0,76),230,95,18,"AvenuePixel-Regular.ttf")
        self.game.draw_text(display, "Song Name: {}".format(self.song_name), (0,0,0),233,177,14,"AvenuePixel-Regular.ttf")
        self.game.draw_text(display, "Artist: {}".format(self.artist_name), (0,0,0),233,197,14,"AvenuePixel-Regular.ttf")
    

   