
from states.state import State
import pygame,os

class Cat(State):
    def __init__(self,game):
        State.__init__(self, game)
        self.state = self.game.get_State()
        self.load_cat_sprites()
        self.cat_rect = self.cat_walk[0].get_rect(midbottom = (0,150))
        self.current_cat_image = self.cat_walk[0]
        self.cat_state = "walking"
        self.cat_index = 0 
    

    def display_animation(self):
        if self.state == "Title Menu":

            if self.cat_state == "walking":

                self.cat_index = (self.cat_index + 1) % len(self.cat_walk)
                self.current_cat_image = self.cat_walk[self.cat_index]

                if self.cat_rect.x == 334:
                    self.cat_state = "sitting"
                    self.cat_index = 0
                    self.cat_rect = self.cat_walk[0].get_rect(midbottom = (350,150))
                    self.current_cat_image = self.cat_sit[0]
           
            elif self.cat_state == "sitting":
                
                self.cat_index = (self.cat_index + 1) % len(self.cat_sit)
                self.current_cat_image = self.cat_sit[self.cat_index]

        if self.state == "Info Menu":
             self.cat_state = "paw"
             self.cat_rect = self.cat_paw[0].get_rect(midbottom = (80,150))
             self.current_cat_image = self.cat_paw[0]
             pygame.time.wait(40) # slows down cat animation
             self.cat_index = (self.cat_index + 1) % len(self.cat_paw)
             self.current_cat_image = self.cat_paw[self.cat_index]

    def update(self, actions):
        if self.cat_state == "walking":
            self.cat_rect.x += 10

        self.display_animation()
        

    def render(self, display):
        display.blit(pygame.transform.scale(self.current_cat_image, (100,100)), self.cat_rect)

    def load_cat_sprites(self):
        self.cat_sit = [pygame.image.load(os.path.join(self.game.assets_graphics_dir,"catSprite","sitting1.png")).convert_alpha(), 
        pygame.image.load(os.path.join(self.game.assets_graphics_dir,"catSprite","sitting2.png")).convert_alpha(),pygame.image.load(os.path.join(self.game.assets_graphics_dir,"catSprite","sitting3.png")).convert_alpha(),
        pygame.image.load(os.path.join(self.game.assets_graphics_dir,"catSprite","sitting4.png")).convert_alpha()]
        
        self.cat_walk =[pygame.image.load(os.path.join(self.game.assets_graphics_dir,"catSprite","running1.png")).convert_alpha(), 
        pygame.image.load(os.path.join(self.game.assets_graphics_dir,"catSprite","running2.png")).convert_alpha(),pygame.image.load(os.path.join(self.game.assets_graphics_dir,"catSprite","running3.png")).convert_alpha(),
        pygame.image.load(os.path.join(self.game.assets_graphics_dir,"catSprite","running4.png")).convert_alpha(),pygame.image.load(os.path.join(self.game.assets_graphics_dir,"catSprite","running5.png")).convert_alpha(),
        pygame.image.load(os.path.join(self.game.assets_graphics_dir,"catSprite","running6.png")).convert_alpha()]

        self.cat_paw =[pygame.image.load(os.path.join(self.game.assets_graphics_dir,"catSprite","paw1.png")).convert_alpha(), 
        pygame.image.load(os.path.join(self.game.assets_graphics_dir,"catSprite","paw2.png")).convert_alpha(),pygame.image.load(os.path.join(self.game.assets_graphics_dir,"catSprite","paw3.png")).convert_alpha(),
        pygame.image.load(os.path.join(self.game.assets_graphics_dir,"catSprite","paw4.png")).convert_alpha(),pygame.image.load(os.path.join(self.game.assets_graphics_dir,"catSprite","paw5.png")).convert_alpha(),
        pygame.image.load(os.path.join(self.game.assets_graphics_dir,"catSprite","paw6.png")).convert_alpha()]
        
    

