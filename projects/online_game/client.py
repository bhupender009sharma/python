import pygame
from network import Network
from player import Player

width =500
height =500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNumber = 0


def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

def redrawWindow(win, player, player2):

    win.fill((255,255,255))         # code for white colour
    player.draw(win)
    player2.draw(win)
    pygame.display.update()


def main():         #this program is going to run continously  and would be checking for collsion,checking for events and will be constantly asking server for information
    run = True
    n = Network()
    p = n.getP()
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        p2 = n.send(p)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()            # this will move our character on which keys are pressing
        redrawWindow(win, p, p2)

main()