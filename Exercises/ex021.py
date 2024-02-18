'''
import pygame
import sys

pygame.init()
my_sound = pygame.mixer.Sound('ex021.mp3')
#pygame.mixer.music.load('')
#pygame.mixer.music.play()
#pygame.event.wait()
my_sound.play()
'''

from playsound import playsound

playsound('ex021.mp3')

