import os
import stat

import pygame
from pygame import *
from playsound import playsound as ps
import glob
from gtts import gTTS


class ReadFiles:
    global path
    path = "D:\\Projects\\python\\music\\*.mp3"

    global playlist
    playlist = []

    mixer.init()
    display.init()

    screen = pygame.display.set_mode ( ( 420 , 240 ) )

    def __init__(self):
        for file in glob.glob(path):
            playlist.append(file)

    def start_playlist(self):
        mixer.music.load(playlist.pop())  # Get the first track from the playlist

        mixer.music.queue(playlist.pop())  # Queue the 2nd song
        mixer.music.set_endevent(pygame.USEREVENT)  # Setup the end track event
        mixer.music.play()  # Play the music

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.USEREVENT:  # A track has ended
                    if len(playlist) > 0:  # If there are more tracks in the queue...
                        mixer.music.queue(playlist.pop())  # Q
