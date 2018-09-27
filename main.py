import pygame
#imports pygame so it can be used
import os
import sys
#import os controls so they can be used

def main(): #main function
    pygame.init()
    #initializes all pygame modules

    pygame.display.set_caption("breakout")
    w = 640
    h = 480
    screen = pygame.display.set_mode((w, h))
    #sets up the window. default resolution is 480p

    logo = pygame.image.load("_assets/breakout.jpg")
    pygame.display.set_icon(logo)
    #sets the logo as the designated logo

    class Background(pygame.sprite.Sprite):
        def __init(self):
            pygame.sprite.Sprite.__init__(self)
            self.images = []
            img = pygame.image.load(os.path.join("_assets", "background.png")).convert()
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()


    class Ball(pygame.sprite.Sprite):
    #spawns the ball into the game
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.images = []
            img = pygame.image.load(os.path.join("_assets", "ball.png")).convert()
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()

    ball = Ball()
    ball.rect.x = 0
    ball.rect.y = 0
    ball_list = pygame.sprite.Group()
    ball_list.add(ball)

    #background = Background()
    #background.rect.x = 0
    #background.rect.y = 0
    #background_list = pygame.sprite.Group()
    #background_list.add(background)

    #backdrop.blit(backdrop, backdropbox)
    #ball_list.draw(screen)
    #pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                os._exit(1)
                running = False

    
    #main run loop

if __name__ == "__main__":
    main()


