import random
import sys
import pygame
import time

class roulettewheel():
    def __init__(self):
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

    font = pygame.font.Font(None, 74)
    text_color = (200, 155, 110)  

    # Main game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Blit the background image to the screen
        screen.blit(roulette_image, (0, 0))

        # Render the text
        text = font.render('Welcome to the Roulette table.', True, text_color)
        # Blit the text onto the screen at a specific position
        screen.blit(text, (590, 100))

        # Update the display
        pygame.display.update()

    # Quit Pygame
    pygame.quit()
    sys.exit()
