import configuration
import sys, pygame

conf = configuration.Configuration()

pygame.init()
fullScreen = pygame.RESIZABLE
if conf.fullscreen == 1:
    fullScreen = pygame.FULLSCREEN
screen = pygame.display.set_mode((conf.width,conf.height), fullScreen)
runP = True
while runP:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            runP = False
        if event.type == pygame.KEYDOWN:
            if event.key == conf.K_QUIT:
                runP = False

