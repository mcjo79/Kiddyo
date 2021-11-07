# importing time and vlc
import time, vlc
 
# method to play video
def video(source):

    # creating a vlc instance
    vlc_instance = vlc.Instance()

    # creating a media player
    player = vlc_instance.media_player_new()

    # creating a media
    media = vlc_instance.media_new(source)

    # setting media to the player
    player.set_media(media)

    player.toggle_fullscreen()

    # play the video
    player.play()

    time.sleep(2)

    # getting the duration of the video
    duration = player.get_length()

    # printing the duration of the video
    print("Duration : " + str(duration))

    currPosition = player.get_position() 

    while currPosition >= 0. and currPosition < 1.:
        currPosition = player.get_position() 
        currSec = player.get_length() * currPosition
        time.sleep(5)
        print("Duration : " + str(currSec) + "/" + str(player.get_length()))
        currPosition = currPosition + 0.2
        if currPosition >= 1.:
            player.set_position(1.)
            break
        player.set_position(currPosition)

    #player.stop()

# call the video method
video("f:/test.mp4")