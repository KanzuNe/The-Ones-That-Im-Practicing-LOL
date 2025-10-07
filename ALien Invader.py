import sys
import pygame
from pygame.sprite import Sprite
from time import sleep

class GameStats:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        ai_game.settings = Setting()
        self.reset_stats()
    
    def reset_stats(self):
        self.ship_left=self.settings.ship_limit
        


class Setting:
    def __init__(self):
        self.width_res = 1366
        self.height_res = 768
        self.resolution = (self.width_res, self.height_res)
        self.backg_color = (250, 250, 250)
        self.ship_speed = 0.5
        #Bullet
        self.bullet_speed = 1
        self.bullet_width= 3
        self.bullet_height =15
        self.bullet_color = (50,50,50)
        self.bullet_allowed = 5
        self.alien_moving_speed_horri= 0.3
        self.alien_moving_speed_verti = 10
        self.alien_direction = 1.0 #Moving left = -1,. right = 1
        self.ship_limit = 3

class Bullet(Sprite):
        def __init__(self, ai_image):
            super().__init__()
            self.settings = Setting()
            
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
        
class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        #Set the image up
        self.image = pygame.image.load('alien.bmp')
        self.rect = self.image.get_rect()
        #Start at safe position (will be repositioned in create_alien)
        self.rect.x = 0
        self.rect.y = 0

        #Assin the float
        self.x = float(self.rect.x)
    def update(self):
        self.x += self.settings.alien_moving_speed_horri * self.settings.alien_direction
        self.rect.x = self.x
        
    def check_edge(self):
        screen_rect= self.screen.get_rect()
        #Check the edge and return true
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
        return False
    

    
        
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
        # Store position as float for smooth movement
        self.x = float(self.rect.x)
    def update_position(self):
        #Add flag for moving
        if self.Moving_Right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.Moving_Left and self.x > 0:
            self.x -= self.settings.ship_speed
        # Update rect position from float
        self.rect.x = self.x
        
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
        self.aliens= pygame.sprite.Group()
        self.create_fleet()
        self.stats=GameStats(self)
        self.gama_active=True

    def check_alien_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self.ship_hit()
                break
    

    def ship_hit(self):
        if self.stats.ship_left >=0:
            self.stats.ship_left -= 1
            self.aliens.empty()
            self.bullet.empty()
            self.ship.rect.center
            sleep(0.5)
            print(self.stats.ship_left)
        else:
            self.gama_active = False

    def create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space = self.settings.width_res -(2*alien_width)
        number_of_aliens = available_space // (2*alien_width)
        #For the row
        self.ship_height = self.ship.rect.height
        available_space_y = self.settings.height_res - (3*alien_width) - self.ship_height
        number_of_row = available_space_y // (2*alien_height)
        for num_row in range(number_of_row):
            for alien_num in range(number_of_aliens):
                self.create_alien(alien_num, num_row)

    def _check_alien_edge(self):
        for alien in self.aliens.sprites():
            if alien.check_edge():
                print(f"Edge detected! Alien at x={alien.rect.x}, y={alien.rect.y}, screen_width={self.screen.get_rect().width}")
                print(f"Alien rect: left={alien.rect.left}, right={alien.rect.right}")
                self._change_alien_direction()
                break

    def _change_alien_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.alien_moving_speed_verti
        self.settings.alien_direction *= -1

    def create_alien(self, alien_num, num_row):
            
            alien = Alien(self)
            alien_width = alien.rect.width
            alien_height = alien.rect.height
            alien_x = alien_width + 2*alien_width*alien_num
            alien_y= alien_height + 2*alien_height*num_row
            alien.rect.x = alien_x
            alien.rect.y = alien_y
            alien.x = float(alien.rect.x)  # Initialize the float position
            self.aliens.add(alien)

    def update_alien(self):
        self._check_alien_edge()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self.ship_hit()
        self.check_alien_bottom()


            

    def run_game(self):
        #Start the mainloop for the game lol
        while True:
            self._check_event()
            if self.gama_active:
                self.ship.update_position()
                self.bullet.update()
                self.update_bullet()
                self.update_alien()
            self._update_screen()
            
            #remove bullet
    def update_bullet(self):
            for bullet in self.bullet.copy():
                if bullet.rect.bottom<=0:
                    self.bullet.remove(bullet)
            collisions= pygame.sprite.groupcollide(self.bullet, self.aliens, True, True)
            if not self.aliens:
                self.bullet.empty()
                self.create_fleet()
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
        #Update the alien
            self.aliens.draw(self.screen)
        #Refresh the screen
            pygame.display.flip()
        
        

if __name__ == "__main__":
    AI= AlienInvasion()
    AI.run_game()
    
            

