# creates a sprite that the user can move up, down, left, and write

# http://www.101computing.net/creating-sprites-using-pygame/
# http://www.101computing.net/pygame-how-to-control-your-sprite/

import riddles
import pygame
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (20, 255, 140)



class Starter(pygame.sprite.Sprite):
    # Represents all background and player sprites
    def __init__(self, bimage, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # uimage is the user of the player, bimage is the background image

        self.uimage = pygame.Surface([width, height])

        self.bimage = pygame.image.load(bimage).convert_alpha()
        pygame.draw.rect(self.uimage, color, [0, 0, width, height])



        # Fetch the rectangle object that has the dimensions of the image.
        self.urect = self.uimage.get_rect()
        self.brect = self.bimage.get_rect()


    def drawBG(self, screen):
        screen.blit(self.bimage, self.brect)

    def drawSprite(self, screen):
        screen.blit(self.uimage, self.urect)


    # user is only allowed to move if the spot their moving to is not a wall (black) or a riddle (green)

    def moveRight(self, pixels):
        try:
            if not self.bimage.get_at((self.urect.x + pixels + self.urect.width, self.urect.y)) == BLACK \
                    or self.bimage.get_at((self.urect.x + pixels + self.urect.width, self.urect.y)) == GREEN:
                self.urect.x += pixels
        except:
            pass

    def moveLeft(self, pixels):
       try:
            if not self.bimage.get_at((self.urect.x - pixels, self.urect.y)) == BLACK \
                    or self.bimage.get_at((self.urect.x - pixels, self.urect.y)) == GREEN:
                self.urect.x -= pixels
       except:
           pass

    def moveDown(self, pixels):
        try:
            if not self.bimage.get_at((self.urect.x, self.urect.y + pixels + self.urect.height)) == BLACK \
                    or self.bimage.get_at((self.urect.x, self.urect.y + pixels + self.urect.height)) == GREEN:
                self.urect.y += pixels
        except:
            pass

    def moveUp(self, pixels):
        try:
            if not self.bimage.get_at((self.urect.x, self.urect.y - pixels)) == BLACK \
                    or self.bimage.get_at((self.urect.x, self.urect.y - pixels)) == GREEN:
                self.urect.y -= pixels
        except:
            pass

    # functions to make sure that all images are the proper size

    def resizeBG(self, width, height):
        self.bimage = pygame.transform.scale(self.bimage, (width, height))

    def resizeSprite(self, width, height):
        self.uimage = pygame.transform.scale(self.uimage, (width, height))



