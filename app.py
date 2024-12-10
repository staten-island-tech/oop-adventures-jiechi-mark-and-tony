import random
import sys
import pygame
import time

# Screen dimensions
screen_width = 1920
screen_height = 1017

# Initialize Pygame
pygame.init()

# Set up display (only do this once)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Roulette Background')

# Load and scale the background image
roulette_image = pygame.image.load('roulettewheel.jpeg')
roulette_image = pygame.transform.scale(roulette_image, (screen_width, screen_height))

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Blit the background image to the screen
    screen.blit(roulette_image, (0, 0))

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()
