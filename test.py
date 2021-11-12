import sys, pygame
from typing import Any

import menu as MN
from PIL import Image, ImageFilter
import configuration


def createListImage(myMenu):
    listImages = []
    for playlist in myMenu.currList:
        try : 
            listImages.append([pygame.transform.scale(pygame.image.load(playlist.image), (276.48, 162)), playlist.name] )
        except  FileNotFoundError:
            listImages.append([None,  playlist.name])
            continue
    return listImages

MENU=1
PLAYLIST=2

page = MENU

myMenu = MN.Menu("playlist.xml")
conf = configuration.Configuration()

pygame.init()

size = width, height = conf.width, conf.height

fullscreen = pygame.RESIZABLE
if conf.fullscreen == 1:
    fullscreen = pygame.FULLSCREEN

speed = [1, 1]

screen = pygame.display.set_mode(size, fullscreen)

try : 
    pilImage = Image.open(myMenu.currPos().image).filter(ImageFilter.GaussianBlur(radius=32))
    drawedImage = pygame.transform.scale( pygame.image.fromstring(pilImage.tobytes(), pilImage.size, pilImage.mode  ), (width, height))
except FileNotFoundError:
    None

listImages = createListImage(myMenu)


font = pygame.font.SysFont(None, 24)

move = 0
rect = Any
runP = True
while runP:
    if page == MENU:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                runP = False
            if event.type == pygame.KEYDOWN:
                if event.key == conf.K_PLAY:
                    page=PLAYLIST
                    break
                if event.key == conf.K_QUIT:
                    runP = False
                if event.key == conf.K_DOWN:
                    try : 
                        pilImage = Image.open(myMenu.nextPos().image).filter(ImageFilter.GaussianBlur(radius=32))
                        drawedImage = pygame.transform.scale( pygame.image.fromstring(pilImage.tobytes(), pilImage.size, pilImage.mode  ), (width, height))
                    except FileNotFoundError:
                        None
                    listImages = createListImage(myMenu)
                if event.key == conf.K_UP:
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
                pygame.draw.rect(screen, (0,0,255), pygame.Rect(x - 2,y - 2, 280, 166))
            if myImage[0] != None:
                screen.blit(myImage[0], (x, y))
            y = y + 182
            if y > 500 :
                x = x + 450
                y = 20
        img = font.render(myMenu.currPos().name, True, (0, 0, 255))
        img1 = font.render(str(myMenu.currentPage + 1) + '/' + str(myMenu.pageCount()), True, (0, 0, 255))
        screen.blit(img, (100, 580))
        screen.blit(img1, (900, 580))
        pygame.display.flip()
    if page == PLAYLIST:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                runP = False
            if event.type == pygame.KEYDOWN:
                if event.key == conf.K_QUIT:
                    runP = False
                if event.key == conf.K_STOP:
                    page=MENU
                    break


sys.exit()
