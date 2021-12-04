import pygame
from pygame.constants import K_KP0, K_KP_MINUS

class ToolsKey:
    @staticmethod
    def otherKeys(key):
        other = {
            pygame.K_SLASH: pygame.K_KP_DIVIDE,
            pygame.K_RETURN: pygame.K_KP_ENTER,
            pygame.K_EQUALS: pygame.K_KP_EQUALS,
            pygame.K_MINUS: pygame.K_KP_MINUS,
            pygame.K_ASTERISK: pygame.K_KP_MULTIPLY,
            pygame.K_PERIOD: pygame.K_KP_PERIOD,
            pygame.K_PLUS: pygame.K_KP_PLUS,
            pygame.K_0: pygame.K_KP0,
            pygame.K_1: pygame.K_KP0,
            pygame.K_2: pygame.K_KP0,
            pygame.K_3: pygame.K_KP0,
            pygame.K_4: pygame.K_KP0,
            pygame.K_5: pygame.K_KP0,
            pygame.K_6: pygame.K_KP0,
            pygame.K_7: pygame.K_KP0,
            pygame.K_8: pygame.K_KP0,
            pygame.K_9: pygame.K_KP0
        }
        return other.get(key, 0)

    @staticmethod
    def getKeys(key):
        listKeys = []
        try :
            currCode = pygame.key.key_code(key)
        except :
            print("key " + key + " no found")
            return listKeys
        
        listKeys.append(currCode)
        otherCode = ToolsKey.otherKeys(currCode)
        if (otherCode > 0) :
            listKeys.append(otherCode)
        return listKeys
   
