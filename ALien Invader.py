import sys
import pygame
class Ship():
    def __init__(self, ai_image):
        #Set starting position
        self.screen = ai_image.screen
        self.screen_rect= ai_image.screen.get_rect()
        #Set on the screen and get its rectangular
        self.image=pygame.image.load('ship.bmp')
        self.rect =self.image.get_rect()
        #Set the ship at bottom
        self.rect.midbottom = self.screen_rect.midbottom
        self.Moving_Right = False
        self.Moving_Left = False
    def update_position(self):
        #Add flag for moving
        if self.Moving_Right:
            self.rect.x += 1
        if self.Moving_Left:
            self.rect.x -= 1
         #Show the ship to screen
    def blitme(self):
        self.screen.blit(self.image, self.rect)
     
   

class AlienInvasion():
    #The class for the game

    def __init__(self):
        #Make the screen
        pygame.init()
        self.screen = pygame.display.set_mode((1366, 768))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        #Change bg color
        self.bg_color= (230,1,210)
    def run_game(self):
        #Start the mainloop for the game lol
        while True:
            self._check_event()
            self.ship.update_position()
            self._update_screen()
            
    def _check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.Moving_Right=True
                if event.key == pygame.K_LEFT:
                    self.ship.Moving_Left=True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.Moving_Right=False
                if event.key == pygame.K_LEFT:
                    self.ship.Moving_Left=False   
                 
                    
    def _update_screen(self):
        #Add new color everytime refresh the screen
            self.screen.fill(self.bg_color)
        #Add ship
            self.ship.blitme()
        #Refresh the screen
            pygame.display.flip()
if __name__ == "__main__":
    AI= AlienInvasion()
    AI.run_game()
    
            

