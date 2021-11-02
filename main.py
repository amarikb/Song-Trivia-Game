import os,pygame,pygame_gui
from states.titleMenu import Title

"""
"Pygame Game States Tutorial: Creating an In-game Menu using States", ChristianD37
source: https://www.youtube.com/watch?v=b_DkQrJxpck
Ideas for the implementation of the pygame game states (Game class)
Retrieved 10-19-2021  
"""
class Game():
        def __init__(self):
            pygame.mixer.pre_init(44100, 16, 2, 4096) 
            pygame.init()
            self.GAME_W,self.GAME_H = 500, 270
            self.SCREEN_WIDTH,self.SCREEN_HEIGHT = 960, 540
            self.game_canvas = pygame.Surface((self.GAME_W,self.GAME_H))
            self.screen = pygame.display.set_mode((self.SCREEN_WIDTH,self.SCREEN_HEIGHT))
            pygame.transform.scale(self.screen, (960,540))

            pygame.display.set_caption("Song Trivia Game")
            musicNote = pygame.image.load("assets/graphics/note1.png")
            pygame.display.set_icon(musicNote)
            self.manager = pygame_gui.UIManager((960, 540),os.path.join("assets","theme.json"))
            self.clock = pygame.time.Clock()

            self.state = "Title Menu"
            self.running, self.playing = True, True
            self.actions = {"play": False, "info" : False, "title" : False, "pause" : False , "win": False, "lose": False}
            self.state_stack = []
            self.songs_done = []
            self.clock = pygame.time.Clock()
            self.time_delta = 0
            self.current_score = 0
            self.high_score = 0
         
            self.load_buttons()
            self.load_assets()
            self.load_states()
           
            self.win_sound = pygame.mixer.Sound(os.path.join(self.assets_dir,"music", "win.wav"))
            self.lose_sound = pygame.mixer.Sound(os.path.join(self.assets_dir,"music", "lose.wav"))
            pygame.mixer.music.load(os.path.join(self.assets_dir,"music", "field_theme_1.wav"))
            pygame.mixer.music.play(-1)

        def game_loop(self):
            while self.playing:
                self.time_delta = self.clock.tick(60)/1000
                self.get_events()
                self.update()
                self.render()
                self.clock.tick(60)

        def get_events(self):
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.playing = False
                    self.running = False
                    self.songs_done.clear() 

                if (event.type == pygame.USEREVENT and event.user_type == pygame_gui.UI_BUTTON_PRESSED):
                        if event.ui_element == self.info_button:
                            self.actions['info'] = True
                            
                        if event.ui_element == self.info_to_title_button:
                                self.actions['title'] = True

                        if event.ui_element == self.pause_button:
                                #self.songs_done.clear() 
                                self.actions['pause'] = True

                        if event.ui_element == self.play_game_button or event.ui_element == self.keep_playing_button:
                                self.actions['play'] = True

                        if event.ui_element == self.quit_button:
                                self.current_score = 0
                                self.songs_done.clear() 
                                self.actions['title'] = True

                        if event.ui_element == self.stop_music_button:
                                pygame.mixer.music.pause()
                                self.play_music_button.show()
                                self.stop_music_button.hide()
                               
                        
                        
                        if event.ui_element == self.play_music_button:
                                pygame.mixer.music.unpause()
                                self.stop_music_button.show()
                                self.play_music_button.hide()


                        
            
                self.manager.process_events(event)

        def update(self):
            if self.state == "Title Menu":
                self.info_button.show()
                self.play_game_button.show()
                self.info_to_title_button.hide()
                self.pause_button.hide()
                self.keep_playing_button.hide()
                self.quit_button.hide()

            if self.state == "Loading Menu":
                self.info_button.hide()
                self.play_game_button.hide()
                self.keep_playing_button.hide()
                self.quit_button.hide()
                self.pause_button.hide()
                
            if(self.state == "Info Menu"):
                self.info_to_title_button.show()
                self.info_button.hide()
                self.play_game_button.hide()
            
            if(self.state == "Play Game"):
                self.info_button.hide()
                self.play_game_button.hide()
                self.keep_playing_button.hide()
                self.quit_button.hide()
                self.pause_button.show()

            
            if(self.state == "Win"):
               self.keep_playing_button.show()
               self.quit_button.show()



            self.manager.update(self.time_delta)
            self.state_stack[-1].update(self.actions)

        
        def render(self):
            self.state_stack[-1].render(self.game_canvas)
            # Render current state to the screen
            self.screen.blit(pygame.transform.scale(self.game_canvas,(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)), (0,0))
            self.manager.draw_ui(self.screen)
            pygame.display.flip() 

        def draw_text(self, surface, text, color, x, y , fontSize = 50, fontType ="NicoBold-Regular.ttf"):
            self.font = pygame.font.Font(os.path.join(self.font_dir,fontType), fontSize)
            text_surface = self.font.render(text, True, color)
            text_rect = text_surface.get_rect()
            text_rect.center = (x, y)
            surface.blit(text_surface, text_rect)

        def load_buttons(self):
            self.info_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 275), (120, 50)),
                                            text='Info',
                                             manager=self.manager)
            self.play_game_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 175), (120, 50)),
                                            text='Play',
                                             manager=self.manager)

            self.info_to_title_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((30, 30), (135, 50)),
                                            text='Main Menu',
                                             manager=self.manager)
            
            self.pause_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((780, 3), (100, 50)),
                                            text='Pause',
                                             manager=self.manager)

        
            self.quit_button =  pygame_gui.elements.UIButton(relative_rect=pygame.Rect((355, 405), (60, 40)),
                                            text='Quit',
                                             manager=self.manager,
                                            object_id='#win_button')
        
            self.keep_playing_button =  pygame_gui.elements.UIButton(relative_rect=pygame.Rect((460, 405), (90, 40)),
                                            text='Keep Going',
                                             manager=self.manager,
                                            object_id='#win_button')

            self.play_music_button =  pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, 450), (90, 40)),
                                            text='music on',
                                             manager=self.manager,
                                            object_id='#win_button')
            
            self.stop_music_button =  pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, 450), (90, 40)),
                                            text='music off',
                                             manager=self.manager,
                                            object_id='#win_button')

            
                                             

        def load_assets(self):
            self.assets_dir = os.path.join("assets")
            self.assets_graphics_dir = os.path.join(self.assets_dir,"graphics")
            self.font_dir = os.path.join(self.assets_dir, "fonts")
            self.font = pygame.font.Font(os.path.join(self.font_dir,"NicoBold-Regular.ttf"), 50)

        def load_states(self):
            self.title_screen = Title(self)
            self.state_stack.append(self.title_screen)        

        def reset_keys(self):
            for action in self.actions:
                self.actions[action] = False


if __name__ == "__main__":
    g = Game()
    while g.running:
        g.game_loop()