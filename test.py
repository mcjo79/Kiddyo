from os import curdir
from re import M
import sys, pygame
from typing import Any
import xml.etree.ElementTree as ET
import menu as MN

myMenu = MN.Menu("playlist.xml")



pygame.init()

size = width, height = 1024, 600
speed = [1, 1]

screen = pygame.display.set_mode(size)

firstImage = pygame.transform.scale(pygame.image.load(myMenu.currPos().image), (width, height)) 
listImages = []

for playlist in myMenu.playlists:
    print (playlist.name, playlist.image)
    listImages.append([pygame.transform.scale(pygame.image.load(playlist.image), (276.48, 162)), playlist.name] )


font = pygame.font.SysFont(None, 24)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()
move = 0
rect = Any

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                firstImage = pygame.transform.scale(pygame.image.load(myMenu.nextPos().image), (width, height)) 
            if event.key == pygame.K_UP:
                firstImage = pygame.transform.scale(pygame.image.load(myMenu.prevPos().image), (width, height)) 

    if move == 3 :
        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]
        move = 0
    else:
        move = move + 1

    screen.blit(firstImage, (0, 0))
    screen.blit(ball, ballrect)
    x, y = 50, 20
    for myImage in listImages:
        if myImage[1] == myMenu.currPos().name:
            pygame.draw.rect(screen, (0,0,255), pygame.Rect(x - 2,y - 2, 280.48, 166))
        screen.blit(myImage[0], (x, y))
        y = y + 182
        if y > 500 :
            x = x + 450
            y = 20
    img = font.render(myMenu.currPos().name, True, (0, 0, 255))
    screen.blit(img, (100, 580))
    pygame.display.flip()