import pygame
pygame.init()           # always use this to initialize pygame

screen_width = 500
screen_length = 480

win = pygame.display.set_mode((screen_length,screen_width))        # this is a tuple which gives the size of the window in which our game will run

pygame.display.set_caption("First Game")  # this will give our window a name

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

class player(object):
    def __init__(self,x,y, width , height):
        self.x =x           # it gives the position where our object will be placed initially on the window
        self.y= y           # make sure that it stays inside the window size
        self.width = width      # size of our character
        self.height = height
        self.vel = 5         # velocity with which it moves

        self.isJump = False
        self.jumpCount = 10

        self.left = False
        self.right = False
        self.walkCount = 0

    def draw(self, win):
        if self.walkCount + 1 >= 27:  # as we are using 9 sprites and each one will have 3 frames , else we will get index error
            self.walkCount = 0

        if self.left:
            win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))  # as we are giving 3 frames for each movement , so integer dividing walkCount by 3
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount // 3], (self.x, self.y))  # as we are giving 3 frames for each movement , so integer dividing walkCount by 3
            self.walkCount += 1
        else:
            win.blit(char, (self.x, self.y))

class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x =x
        self.y =y
        self.radius =radius
        self.color = color
        self.facing =facing
        self.vel = 8* facing

    def draw(self,win):
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)

clock = pygame.time.Clock()

def redrawGameWindow():

    # for filling color in background use -  win.fill((0, 0,0))  # it will fill the background as similar to the window colour(i.e. black color) so that it can resolve above problem
    # but now we will use picture
    win.blit(bg,(0,0))          # and we are going to place it in background 0,0
    man.draw(win)

    pygame.display.update()



# main loop
man = player(50,410,64, 64)         # creating an object of class player
run = True
while run:
# here we are going to use 27 fps    pygame.time.delay(50)      # it will give time delay, and so that things will not happen to fast. here 50 milisecond delay is given

    clock.tick(27)          # this will set to 27 fps for our game

    for event in pygame.event.get():        # it is going to get all the events happen like - pressing keys, mouse click, etc..
        if event.type == pygame.QUIT:        # checking if we tap the close button on our window
            run =False

    # now we want our character to move continously when we hold a movement key, but it will move only once if we do it directly
    # so we will use here a list called keys, so it gets updated
    keys = pygame.key.get_pressed()     # gives the list values or the no. of times keys pressed

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x-= man.vel
        man.left =True
        man.right = False
    elif keys[pygame.K_RIGHT] and man.x < screen_length - man.width - man.vel:            # so that right side of the character does not crosses the right side of screen
        man.x+= man.vel
        man.left= False
        man.right= True
    else:
        man.right= False
        man.left = False
        man.walkCount = 0

    if not (man.isJump):            # so that while jumping we do not move up and down
        if keys[pygame.K_SPACE]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:  # will jump upto 10
            neg = 1
            if man.jumpCount < 0:
                neg = -1  # to come down when reaches top of the jump
            man.y -= (man.jumpCount ** 2) * 0.5 * neg  # quadratic equation for jump
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    redrawGameWindow()

pygame.quit()       #quits the game