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

x =50           # it gives the position where our object will be placed initially on the window
y= 400          # make sure that it stays inside the window size
width = 64      # size of our character
height = 64
vel = 5         # velocity with which it moves

isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0

clock = pygame.time.Clock()

def redrawGameWindow():
    global walkCount

    # for filling color in background use -  win.fill((0, 0,0))  # it will fill the background as similar to the window colour(i.e. black color) so that it can resolve above problem
    # but now we will use picture
    win.blit(bg,(0,0))          # and we are going to place it in background 0,0
    #as we are going to use image here not a block-    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))  # for circle type circle,for polygon type polygon ,and so on
    # win is the surface at which our character will get placed,(255,0,0) is the colour code for RGB values, (x,y) is the position of the character

    if walkCount +1 >=27:       # as we are using 9 sprites and each one will have 3 frames , else we will get index error
        walkCount =0

    if left:
        win.blit(walkLeft[walkCount//3], (x,y))         # as we are giving 3 frames for each movement , so integer dividing walkCount by 3
        walkCount +=1
    elif right:
        win.blit(walkRight[walkCount // 3], (x, y))  # as we are giving 3 frames for each movement , so integer dividing walkCount by 3
        walkCount += 1
    else:
        win.blit(char, (x,y) )

    pygame.display.update()



# main loop
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

    if keys[pygame.K_LEFT] and x > vel:
        x-= vel
        left =True
        right = False
    elif keys[pygame.K_RIGHT] and x < screen_length - width - vel:            # so that right side of the character does not crosses the right side of screen
        x+= vel
        left= False
        right= True
    else:
        right= False
        left = False
        walkCount = 0

    if not (isJump):            # so that while jumping we do not move up and down

        '''     as we are not going to use up and down movement in this game
        if keys[pygame.K_UP] and y>vel:
            y-=vel
        if keys[pygame.K_DOWN] and y< screen_width - height - vel:
            y+=vel
        '''
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
    else:
        if jumpCount >= -10:  # will jump upto 10
            neg = 1
            if jumpCount < 0:
                neg = -1  # to come down when reaches top of the jump
            y -= (jumpCount ** 2) * 0.5 * neg  # quadratic equation for jump
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    # so now if we run the above program , it will create a continous line like we are drawing in paint. it happens bcoz we have not updated the character position , so it will be created at every location to which it moves
    redrawGameWindow()

pygame.quit()       #quits the game