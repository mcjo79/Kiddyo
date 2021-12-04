from re import M
import os, sys, pygame, vlc
from typing import Any
import menu as MN
import menupl as MNPL
import configparser
from tools import ToolsKey


m = None
if sys.platform == "linux":
    import alsaaudio
    m = alsaaudio.Mixer()
from PIL import Image, ImageFilter

configFilePath = os.path.join(os.path.dirname(__file__), 'config.cfg')
config = configparser.ConfigParser()
config.read(configFilePath)

quitKeys = ToolsKey.getKeys(config['setup']['exit'])
upKeys = ToolsKey.getKeys(config['setup']['up'])
downKeys = ToolsKey.getKeys(config['setup']['down'])
stopKeys = ToolsKey.getKeys(config['setup']['stop'])
playKeys = ToolsKey.getKeys(config['setup']['play'])
soundplusKeys = ToolsKey.getKeys(config['setup']['soundplus'])
soundminusKeys = ToolsKey.getKeys(config['setup']['soundminus'])

def createListImage(menu):
    listImages = []
    for playlist in menu.currList:
        try :
            listImages.append([pygame.transform.scale(pygame.image.load(playlist.image), (276, 162)), playlist.name] )
        except  FileNotFoundError:
            listImages.append([None,  playlist.name])
            continue
    return listImages




myMenu = MN.Menu("playlist.xml")
myMenuPL = None
currVideo = None
movie = None
vlcInstance = None
if sys.platform == "linux":
    vlcInstance = vlc.Instance('--no-xlib -q > /dev/null 2>&1')
else:
    vlcInstance = vlc.Instance('-q')

player = vlcInstance.media_player_new()
em = player.event_manager()
pygame.init()

size = width, height = 1024, 600
speed = [1, 1]
pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

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

vlc_onload = False
vlc_onstop = False
waitTime = 0
while 1:
    if vlc_onstop == True and player.get_state() != vlc.State.Stopped:
        continue
    if waitTime > 0:
        waitTime = waitTime - 1
        continue
    if player.get_state() == vlc.State.Opening:
        continue
    if vlc_onload :
        continue
    
    if vlc_onstop == True and player.get_state() == vlc.State.Stopped:
        vlc_onstop = False
        continue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYUP:
            if event.key in quitKeys:
                sys.exit()
            if event.key in soundplusKeys:
                if sys.platform == "linux":
                    if m.getvolume()[0] < 100:
                        volume = m.getvolume()[0] + 10
                        if volume > 100:
                            volume = 100
                        m.setvolume(volume)
                else :
                    volume = player.audio_get_volume() + 10
                    if volume > 100: 
                        volume = 100
                    player.audio_set_volume(volume)


            if event.key in soundminusKeys:
                if sys.platform == "linux":
                    if m.getvolume()[0] > 0:
                        volume = m.getvolume()[0] - 10
                        if volume < 0:
                            volume = 0
                        m.setvolume(volume)
                else:
                    volume = player.audio_get_volume() - 10
                    if volume < 0: 
                        volume = 0
                    player.audio_set_volume(volume)

            if myMenuPL == None:
                if event.key in playKeys:
                    myMenuPL = None
                    if len(myMenu.currPos().videos) > 0:
                        myMenuPL = MNPL.MenuPL(myMenu.currPos().videos)
                        listImages = createListImage(myMenuPL)
                if event.key in downKeys:
                    try : 
                        pilImage = Image.open(myMenu.nextPos().image).filter(ImageFilter.GaussianBlur(radius=32))
                        drawedImage = pygame.transform.scale( pygame.image.fromstring(pilImage.tobytes(), pilImage.size, pilImage.mode  ), (width, height))
                    except FileNotFoundError:
                        None
                    listImages = createListImage(myMenu)
                if event.key in upKeys:
                    try : 
                        pilImage = Image.open(myMenu.prevPos().image).filter(ImageFilter.GaussianBlur(radius=32))
                        drawedImage = pygame.transform.scale( pygame.image.fromstring(pilImage.tobytes(), pilImage.size, pilImage.mode  ), (width, height))
                    except FileNotFoundError:
                        None
                    listImages = createListImage(myMenu)
            elif currVideo == None:
                if event.key in playKeys:
                    movie = None
                    currVideo = myMenuPL.currPos()
                if event.key in stopKeys:
                    myMenuPL = None
                    try : 
                        pilImage = Image.open(myMenu.currPos().image).filter(ImageFilter.GaussianBlur(radius=32))
                        drawedImage = pygame.transform.scale( pygame.image.fromstring(pilImage.tobytes(), pilImage.size, pilImage.mode  ), (width, height))
                    except FileNotFoundError:
                        None
                    listImages = createListImage(myMenu)
                if event.key in downKeys:
                    try : 
                        pilImage = Image.open(myMenuPL.nextPos().image).filter(ImageFilter.GaussianBlur(radius=32))
                        drawedImage = pygame.transform.scale( pygame.image.fromstring(pilImage.tobytes(), pilImage.size, pilImage.mode  ), (width, height))
                    except FileNotFoundError:
                        None
                    listImages = createListImage(myMenuPL)
                if event.key in upKeys:
                    try : 
                        pilImage = Image.open(myMenuPL.prevPos().image).filter(ImageFilter.GaussianBlur(radius=32))
                        drawedImage = pygame.transform.scale( pygame.image.fromstring(pilImage.tobytes(), pilImage.size, pilImage.mode  ), (width, height))
                    except FileNotFoundError:
                        None
                    listImages = createListImage(myMenuPL)
            else:
                if event.key in playKeys:
                    if player.get_state() == vlc.State.Paused:
                        player.play()
                    if player.get_state() == vlc.State.Playing:
                        player.pause()
                    continue
                if event.key in downKeys:
                    movie = None
                    player.stop()
                    vlc_onstop = True
                    currVideo = myMenuPL.nextPos()
                    waitTime = 500
                    continue
                if event.key in upKeys:
                    player.stop()
                    vlc_onstop = True
                    movie = None
                    currVideo = myMenuPL.prevPos()
                    waitTime = 500
                    continue
                if event.key in stopKeys:
                    player.stop()
                    currVideo = None
                    movie = None
                    waitTime = 500
                    try : 
                        pilImage = Image.open(myMenuPL.currPos().image).filter(ImageFilter.GaussianBlur(radius=32))
                        drawedImage = pygame.transform.scale( pygame.image.fromstring(pilImage.tobytes(), pilImage.size, pilImage.mode  ), (width, height))
                    except FileNotFoundError:
                        None
                    listImages = createListImage(myMenuPL)
                    continue
    if myMenuPL == None:
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
        img = font.render(myMenu.currPos().name, True, (0,0,0))
        img1 = font.render(str(myMenu.currentPage + 1) + '/' + str(myMenu.pageCount()), True, (0,0,0))
        screen.blit(img, (100, 560))
        screen.blit(img1, (900, 560))
    elif currVideo == None:
        screen.blit(drawedImage, (0, 0))
        x, y = 50, 20
        for myImage in listImages:
            if myImage[1] == myMenuPL.currPos().name:
                pygame.draw.rect(screen, (58,142,186), pygame.Rect(x - 8,y - 8, 292, 178))
            if myImage[0] != None:
                screen.blit(myImage[0], (x, y))
            y = y + 182
        img = font.render(myMenu.currPos().name, True, (0,0,0))
        img1 = font.render(myMenuPL.currPos().name, True, (0,0,0))
        img2 = font.render(str(myMenuPL.currentPage + 1) + '/' + str(myMenuPL.pageCount()), True, (0,0,0))
        screen.blit(img, (100, 560))
        screen.blit(img2, (900, 560))
        try :
            img3 = pygame.transform.scale(pygame.image.load(myMenuPL.currPos().image), (504, 324))
        except  FileNotFoundError:
            img3 = None
        if img3 != None : 
            screen.blit(img3, (412, 108))
        screen.blit(img1, (412, 440))
    elif vlc_onstop == False:
        if (movie == None) :
            vlc_onload = True
            movie = os.path.expanduser(myMenuPL.currPos().file)
            pygame.draw.rect(screen, (0,0,0), pygame.Rect(0, 0, width, height))
            if not os.access(movie, os.R_OK):
                print('Error: %s file not readable' % movie)
                currVideo = None
                movie = None
                try : 
                    pilImage = Image.open(myMenuPL.currPos().image).filter(ImageFilter.GaussianBlur(radius=32))
                    drawedImage = pygame.transform.scale( pygame.image.fromstring(pilImage.tobytes(), pilImage.size, pilImage.mode  ), (width, height))
                except FileNotFoundError:
                    None
                listImages = createListImage(myMenuPL)
                continue
            media = vlcInstance.media_new(movie)
            win_id = pygame.display.get_wm_info()['window']
            if sys.platform == "linux":
                player.set_xwindow(win_id)
            elif sys.platform == "win32":
                player.set_hwnd(win_id)
            elif sys.platform == "darwin":
                player.set_agl(win_id)
            player.set_media(media)
            pygame.mixer.quit()
            player.play()
            waitTime = 500
            vlc_onload = False
        else:
            if player.get_state() == vlc.State.Ended and vlc_onload == False:
                currVideo = myMenuPL.nextPos()
                movie = None
    pygame.display.flip()

