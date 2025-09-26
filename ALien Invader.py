import sys
import pygame

class AlienInvasion(self):
    #The class for the game

    def __init__(self):
        #Make the screen
        pygame.init()
        self.screen = pygame.display.set.mode((1920, 1080))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        #Start the mainloop for the game lol
        while True:
            for event in pygame.event.get():
                if event.type == pygame.quit:
                    sys.exit()
        #Refresh the screen
            pygame.display.flip()

if __name__ == "__main__":
    AI= AlienInvasion()
    AI.run_game()
    
            

