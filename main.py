import pygame
#imports pygame so it can be used
import os
#import os controls so they can be used

def main(): #main function
    pygame.init()
    #initializes all pygame modules

    pygame.display.set_caption("breakout")
    screen = pygame.display.set_mode((640, 480))
    #sets up the window. default resolution is 480p

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                os._exit(1)
                running = False

if __name__ == "__main__":
    main()
