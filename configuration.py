import configparser
import sys, pygame

class Configuration:
    config = None
    width: 1280
    height: 600
    fullscreen: 0
    K_UP: pygame.K_UP
    K_DOWN: pygame.K_DOWN
    K_PLAY: pygame.K_RETURN
    K_STOP: pygame.K_DELETE
    K_PLUS: pygame.K_PLUS
    K_MINUS: pygame.K_MINUS
    K_QUIT: pygame.K_ESCAPE

    def __init__(self) :
        self.config = configparser.ConfigParser()
        if self.config.read("configuration.ini") == [] :
            self.createConfig()
        self.width = int(self.config['DEFAULT']['width'])
        self.height = int(self.config['DEFAULT']['height'])
        self.fullscreen = int(self.config['DEFAULT']['fullscreen'])
        self.K_UP = int(self.config['DEFAULT']['up'])
        self.K_DOWN = int(self.config['DEFAULT']['down'])
        self.K_PLAY = int(self.config['DEFAULT']['play'])
        self.K_STOP = int(self.config['DEFAULT']['stop'])
        self.K_PLUS = int(self.config['DEFAULT']['soundup'])
        self.K_MINUS = int(self.config['DEFAULT']['sounddown'])
        self.K_QUIT = int(self.config['DEFAULT']['quit'])

    def createConfig(self):
        self.config['DEFAULT'] = {  'width': 1280,
                                    'height': 600, 
                                    'fullscreen': 0, 
                                    'up': pygame.K_UP, 
                                    'down': pygame.K_DOWN, 
                                    'play': pygame.K_RETURN, 
                                    'stop': pygame.K_DELETE, 
                                    'soundup': pygame.K_PLUS, 
                                    'sounddown': pygame.K_MINUS, 
                                    'quit': pygame.K_ESCAPE }
        with open('configuration.ini', 'w') as configfile:
            self.config.write(configfile)