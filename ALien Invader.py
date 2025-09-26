import sys
import pygame
class Ship():
    def __init__(self, ai_image):
        #Set starting position
        self.screen = ai_image
        self.screen_rect= ai_image.screen.get_rect()
        #Set on the screen and get its rectangular
        self.image=pygame.image.load('ship.bmp')
        self.rect =self.image.get_rect()
        #Set the ship at bottom
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        
class AlienInvasion():
    #The class for the game

    def __init__(self):
        #Make the screen
        pygame.init()
        self.screen = pygame.display.set_mode((1366, 768))
        pygame.display.set_caption("Alien Invasion")
        #Change bg color
        self.bg_color= (230,1,210)
    def run_game(self):
        #Start the mainloop for the game lol
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
        #Refresh the screen
            pygame.display.flip()
        #Add new color everytime refresh the screen
            self.screen.fill(self.bg_color)

if __name__ == "__main__":
    AI= AlienInvasion()
    AI.run_game()
    
            

