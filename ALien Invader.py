import sys
import pygame
from pygame.sprite import Sprite


class Setting:
    def __init__(self):
        self.width_res = 1366
        self.height_res = 768
        self.resolution = (self.width_res, self.height_res)
        self.backg_color = (250, 250, 250)
        self.ship_speed = 3
        #Bullet
        self.bullet_speed = 1
        self.bullet_width= 3
        self.bullet_height =15
        self.bullet_color = (50,50,50)
        self.bullet_allowed = 5
class Bullet(Sprite):
        def __init__(self, ai_image):
            super().__init__()
            self.settings = Setting()
            self.ship = Ship(ai_image)
            
            self.screen = ai_image.screen
            self.color = self.settings.bullet_color

          #Get a bullet rect at 00
            self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
            self.rect.midtop = ai_image.ship.rect.midtop
          #Get position as decimal
            self.y = float(self.rect.y)
        def update(self):
            self.y -= self.settings.bullet_speed
            self.rect.y=self.y
            #draw the bullet
        def draw_bullet(self):
          pygame.draw.rect(self.screen, self.color, self.rect)
        
class Ship:
    def __init__(self, ai_image):
        #Set starting position
        self.screen = ai_image.screen
        self.screen_rect= ai_image.screen.get_rect()
        #Set on the screen and get its rectangular
        self.image=pygame.image.load('ship.bmp')
        self.rect =self.image.get_rect()
        #Set the ship at bottom
        self.rect.midbottom = self.screen_rect.midbottom
        #Moving FLags
        self.Moving_Right = False
        self.Moving_Left = False
        self.settings= Setting()
    def update_position(self):
        self.x = float(self.rect.x)
        self.rect.x = self.x
        #Add flag for moving
        if self.Moving_Right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed
        if self.Moving_Left and self.rect.x > 0:
            self.rect.x -= self.settings.ship_speed
        
         #Show the ship to screen
    def blitme(self):
        self.screen.blit(self.image, self.rect)
     
   

class AlienInvasion:
    #The class for the game

    def __init__(self):
        #Make the screen
        self.settings = Setting()
        pygame.init()
        self.screen = pygame.display.set_mode((self.settings.resolution))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullet = pygame.sprite.Group()
        #Change bg color
        self.bg_color= (self.settings.backg_color)
    def run_game(self):
        #Start the mainloop for the game lol
        while True:
            self._check_event()
            self.ship.update_position()
            self.bullet.update()
            self._update_screen()
        
            #remove bullet
           
            for bullet in self.bullet.copy():
                if bullet.rect.bottom<=0:
                    self.bullet.remove(bullet)
            
            
    def _check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                 self._check_event_keydown(event)
            elif event.type == pygame.KEYUP:
                 self._check_event_keyup(event)

    def fire_bullet(self):
        if len(self.bullet) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullet.add(new_bullet)  

    def _check_event_keydown(self, event):
            
                if event.key == pygame.K_RIGHT:
                    self.ship.Moving_Right=True
                if event.key == pygame.K_LEFT:
                    self.ship.Moving_Left=True
                elif event.key ==pygame.K_q:
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                     self.fire_bullet()
                     
    def _check_event_keyup(self, event):
            
                if event.key == pygame.K_RIGHT:
                    self.ship.Moving_Right=False
                if event.key == pygame.K_LEFT:
                    self.ship.Moving_Left=False   
                 
                    
    def _update_screen(self):
        #Add new color everytime refresh the screen
            self.screen.fill(self.bg_color)
        #Add ship
            self.ship.blitme()
        #Update the decimal number of bullet
            for bullet in self.bullet.sprites():
                 bullet.draw_bullet()
        #Refresh the screen
            pygame.display.flip()
        
        

if __name__ == "__main__":
    AI= AlienInvasion()
    AI.run_game()
    
            

