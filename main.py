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

    class Ball(pygame.sprite.Sprite):
    #spawns the ball into the game
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.images = []
            ballimg = pygame.image.load(os.path.join("_assets", "ball.png")).convert()
            self.images.append(ballimg)
            self.image = self.images[0]
            self.rect = self.image.get_rect()

    class Paddle(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.images = []
            paddleimg = pygame.image.load(os.path.join("_assets", "paddle.png")).convert()
            self.images.append(paddleimg)
            self.image = self.images[0]
            self.rect = self.image.get_rect()

    class SideWalls(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.images = []
            sidewallimg = pygame.image.load(os.path.join("_assets", "sideWallTile.png")).convert()
            self.images.append(sidewallimg)
            self.images = self.images[0]
            self.rect = self.image.get_rect()

    background = pygame.image.load(os.path.join("_assets", "background.png")).convert()
    screen.blit(background, (0,0))        

    ball = Ball()
    ball.rect.x = 0
    ball.rect.y = 0
    ball_list = pygame.sprite.Group()
    ball_list.add(ball)
    #screen.blit(ball, (ball.rect.x, ball.rect.y))
    ball_list.draw(screen)

    paddle = Paddle()
    paddle.rect.x = 294
    paddle.rect.y = 420
    paddle_list = pygame.sprite.Group()
    paddle_list.add(paddle)
    #screen.blit(paddle, (paddle.rect.x, paddle.rect.y))
    paddle_list.draw(screen)

    pygame.display.flip()

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


