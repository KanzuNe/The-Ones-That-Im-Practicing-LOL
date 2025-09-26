import sys
import pygame

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
    
            

