from gpiozero import Button
from signal import pause
import pygame

currently_playing = '/home/jimmy/jinglebells.mp3'

pygame.mixer.init()
pygame.mixer.music.load(currently_playing)
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play()

def play_song(song):
    global currently_playing
    if currently_playing == song and pygame.mixer.music.get_busy():
        # Already playing this song. Not restarting it...
        return
    else:
        pygame.mixer.music.stop()
        pygame.mixer.music.load(song)
        currently_playing = song
        pygame.mixer.music.play()
        print(song)

def jinglebells():
    play_song("/home/jimmy/jinglebells.mp3")
def silentnight():
    play_song("/home/jimmy/silentnight.mp3")

def stop_song():
    if pygame.mixer.music.get_busy():
        global currently_playing
        currently_playing = None
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        pygame.mixer.init()
        print("Stopped playing")


# https://gpiozero.readthedocs.io/en/latest/recipes.html#pin-numbering
# GPIO2 == pin 2, etc.

button_jinglebells = Button(2)
button_jinglebells.when_pressed = jinglebells

button_silentnight = Button(3)
button_silentnight.when_pressed = silentnight

button_stop = Button(4)
button_stop.when_pressed = stop_song

pause()