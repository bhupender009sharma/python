import pygame
pygame.init()           # always use this to initialize pygame

screen_width = 480
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
        self.standing = True

    def draw(self, win):
        if self.walkCount + 1 >= 27:  # as we are using 9 sprites and each one will have 3 frames , else we will get index error
            self.walkCount = 0

        if not (self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))  # as we are giving 3 frames for each movement , so integer dividing walkCount by 3
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount // 3], (self.x, self.y))  # as we are giving 3 frames for each movement , so integer dividing walkCount by 3
                self.walkCount += 1
        else:                               # so that it stays in on direction when stopped
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))

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

class enemy(object):
    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'),
                 pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'),
                 pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'),
                 pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
    walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'),
                pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'),
                pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'),
                pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]

    def __init__(self,x,y,width,height,end):
        self.x= x
        self.y=y
        self.width =width
        self.height = height
        self.end = end
        self.path = [self.x , self.end]
        self.walkCount =0
        self.vel =3

    def draw(self,win):
        self.move()
        if self.walkCount +1 >= 33:              # so here we have 11 images
            self.walkCount =0

        if self.vel >0:
            win.blit(self.walkRight[self.walkCount // 3], (self.x,self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1


    def move(self):
        if self.vel >0:             # for moving in right direction
            if self.x + self.vel < self.path[1]:        # for moving upto a certain point and not covering up the whole screen and then coming back to attack
                self.x += self.vel                      # it it is less than end , then keep moving in right direction
            else:
                self.vel *= -1                          # if it has reached the end point then starting coming back
                self.walkCount =0
        else:
            if self.x -self.vel >self.path[0]:          # simlarly for left direction
                self.x += self.vel                      # as we are moving in left direction , so it is already -ve , so here we add it directly , no need for subtraction
            else:
                self.vel *= -1                          # if it has reached the end point then starting coming back
                self.walkCount =0


clock = pygame.time.Clock()

def redrawGameWindow():

    # for filling color in background use -  win.fill((0, 0,0))  # it will fill the background as similar to the window colour(i.e. black color) so that it can resolve above problem
    # but now we will use picture
    win.blit(bg,(0,0))          # and we are going to place it in background 0,0
    man.draw(win)
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()



# main loop
man = player(50,410,64, 64)         # creating an object of class player
goblin = enemy(50,410,64,64,410)
bullets = []
run = True
while run:
# here we are going to use 27 fps    pygame.time.delay(50)      # it will give time delay, and so that things will not happen to fast. here 50 milisecond delay is given

    clock.tick(27)          # this will set to 27 fps for our game

    for event in pygame.event.get():        # it is going to get all the events happen like - pressing keys, mouse click, etc..
        if event.type == pygame.QUIT:        # checking if we tap the close button on our window
            run =False

    for bullet in bullets:
        if bullet.x <screen_length and bullet.x >0:  # keep it inside the screen
            bullet.x += bullet.vel
        else:                           # so that bullet does not get stuck at end of the window
            bullets.pop(bullets.index(bullet))          # find index of bullet from bullets and delete(pop) it

    # now we want our character to move continously when we hold a movement key, but it will move only once if we do it directly
     # so we will use here a list called keys, so it gets updated
    keys = pygame.key.get_pressed()     # gives the list values or the no. of times keys pressed

    if keys[pygame.K_SPACE]:
        if man.left:
            facing = -1         # as we want to move our bullet in left direction , so we have to subtract from its current position
        else:
            facing =1

        if len(bullets)<5:      # no. of bullets on screen
            bullets.append(projectile(round(man.x + man.width//2),round(man.y + man.height//2),3,(0,0,0),facing))             # rounding off so that bullet comes from centre of the man

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x-= man.vel
        man.left =True
        man.right = False
        man.standing = False

    elif keys[pygame.K_RIGHT] and man.x < screen_length - man.width - man.vel:            # so that right side of the character does not crosses the right side of screen
        man.x+= man.vel
        man.left= False
        man.right= True
        man.standing =False

    else:
        man.standing = True
        man.walkCount = 0

    if not (man.isJump):            # so that while jumping we do not move up and down
        if keys[pygame.K_UP]:
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