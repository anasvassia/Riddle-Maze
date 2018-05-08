# http://www.101computing.net/creating-sprites-using-pygame/
# http://www.101computing.net/pygame-how-to-control-your-sprite/
# https://stackoverflow.com/questions/28098738/changing-size-of-image
# https://stackoverflow.com/questions/31570527/how-to-get-the-color-value-of-a-pixel-in-pygame

# a maze game where in order to get through the end, the player must answer riddles
# at the moment, there is only one riddle per game

from starter import *
from riddles import *
import pygame
pygame.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (20, 255, 140)
GREY = (210, 210 ,210)


SPRITEWIDTH = 20
SPRITEHEIGHT = 20
SCREENWIDTH = 600
SCREENHEIGHT = 600

size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Riddle Maze")


# allowing for randomization of mazes
mazes = ["maze.png", "kidmaze.png", "coding maze"]
ranmaze = randint(0, len(mazes)-1)

# game starts
game = Starter(mazes[ranmaze], RED, SPRITEWIDTH, SPRITEHEIGHT)
game.resizeBG(SCREENWIDTH, SCREENHEIGHT)
game.resizeSprite(SPRITEWIDTH, SPRITEHEIGHT)

# at the moment, only one riddle is created
ranx = randint(0, SCREENWIDTH)
rany = randint(0, SCREENHEIGHT)

riddle = Riddle(GREEN, SPRITEWIDTH, SPRITEHEIGHT, ranx, rany)
riddle.resize(SPRITEWIDTH, SPRITEHEIGHT)


done = False
riddleSolved = False
clock = pygame.time.Clock()



while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:  # Pressing the x Key will quit the game
                done = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        game.moveRight(1)
    if keys[pygame.K_LEFT]:
        game.moveLeft(1)
    if keys[pygame.K_DOWN]:
        game.moveDown(1)
    if keys[pygame.K_UP]:
        game.moveUp(1)


    screen.fill(WHITE)
    game.drawBG(screen)
    game.drawSprite(screen)
    riddle.draw(screen)

    # if the user is on top of the riddle, then the riddle box opens
    if game.urect.x == ranx and game.urect.y == rany:
        riddle.start()
        if riddle.check() == True:
            riddle.color = GREY
        else:
            riddle.start()

    # the game ends when the user reaches the lower right corner of the screen
    if game.urect.x == SCREENWIDTH - 2 and game.urect.y == SCREENHEIGHT - 2:
        done = True
        pygame.quit()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()



