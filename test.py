from os import curdir
from re import M
import sys, pygame
from typing import Any
import xml.etree.ElementTree as ET
import menu as MN
from PIL import Image, ImageFilter


def createListImage(myMenu):
    listImages = []
    for playlist in myMenu.currList:
        try : 
            listImages.append([pygame.transform.scale(pygame.image.load(playlist.image), (276, 162)), playlist.name] )
        except  FileNotFoundError:
            listImages.append([None,  playlist.name])
            continue
    return listImages

myMenu = MN.Menu("playlist.xml")

pygame.init()

size = width, height = 1024, 600
speed = [1, 1]
pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
screen = pygame.display.set_mode(size, pygame.WINDOWMAXIMIZED)

try : 
    pilImage = Image.open(myMenu.currPos().image).filter(ImageFilter.GaussianBlur(radius=32))
    drawedImage = pygame.transform.scale( pygame.image.fromstring(pilImage.tobytes(), pilImage.size, pilImage.mode  ), (width, height))
except FileNotFoundError:
    None

listImages = createListImage(myMenu)


font = pygame.font.SysFont(None, 30)
font1 = pygame.font.SysFont(None, 31)

move = 0
rect = Any

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
            if event.key == pygame.K_DOWN:
                try : 
                    pilImage = Image.open(myMenu.nextPos().image).filter(ImageFilter.GaussianBlur(radius=32))
                    drawedImage = pygame.transform.scale( pygame.image.fromstring(pilImage.tobytes(), pilImage.size, pilImage.mode  ), (width, height))
                except FileNotFoundError:
                    None
                listImages = createListImage(myMenu)
            if event.key == pygame.K_UP:
                try : 
                    pilImage = Image.open(myMenu.prevPos().image).filter(ImageFilter.GaussianBlur(radius=32))
                    drawedImage = pygame.transform.scale( pygame.image.fromstring(pilImage.tobytes(), pilImage.size, pilImage.mode  ), (width, height))
                except FileNotFoundError:
                    None
                listImages = createListImage(myMenu)
        

    screen.blit(drawedImage, (0, 0))
    x, y = 50, 20
    for myImage in listImages:
        if myImage[1] == myMenu.currPos().name:
            pygame.draw.rect(screen, (58,142,186), pygame.Rect(x - 8,y - 8, 292, 178))
        if myImage[0] != None:
             screen.blit(myImage[0], (x, y))
        y = y + 182
        if y > 500 :
            x = x + 450
            y = 20
    img3 = font1.render(myMenu.currPos().name, True, (0,0,0))
    img4 = font1.render(str(myMenu.currentPage + 1) + '/' + str(myMenu.pageCount()), True, (0,0,0))
    img = font.render(myMenu.currPos().name, True, (58,142,186))
    img1 = font.render(str(myMenu.currentPage + 1) + '/' + str(myMenu.pageCount()), True, (58,142,186))
    screen.blit(img3, (100, 560))
    screen.blit(img4, (900, 560))
    pygame.display.flip()

