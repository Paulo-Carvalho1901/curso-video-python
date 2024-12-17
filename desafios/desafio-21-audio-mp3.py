"""
Faça um progarama em python
que abra a reproduza o audio de 
arquivo mp3

"""
import pygame

# Initialize Pygame
pygame.init()

# Set up the mixer
pygame.mixer.init()

# Load the MP3 file
pygame.mixer.music.load('Damonte.mp3')

# Play the music
pygame.mixer.music.play()

# Keep the program running until the music finishes
while pygame.mixer.music.get_busy():
    pass

# Quit Pygame
pygame.quit()