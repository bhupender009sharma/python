import pygame

class Player():                                     # class for our character( here is a box)
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)          # to make things faster when drawing our character
        self.vel = 3                           # for movement

    def draw(self, win):            # win is the window here
        # draw our character that represents on our screen
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):         # to check the moves
        keys = pygame.key.get_pressed()       # its going to gives us the dictionary of all of the keys and essentially each key is going to have a value of either 0 or 1, if 1 is true then we are pressing the key else not
        # and if we press more then one key , then it will allow to move us diagonally
        # now we will check if the certain keys are pressed and then the value of x and y accordingly

        if keys[pygame.K_LEFT]:
            self.x -= self.vel                   # when we press left value we will have to -1 from x
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
        if keys[pygame.K_UP]:
            self.y -= self.vel
        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)           # we have to update the position of our character, otherwise it will create itself at same position at which it was created
