import random
import sys
import pygame
import ticket

# Initialize Pygame
pygame.init()

# Set up the screen (window size)
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set window title
pygame.display.set_caption("Add Text Example")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create a font object
font = pygame.font.SysFont('Arial', 48)  # Use Arial font, size 48
input_font = pygame.font.SysFont('Arial', 24)  # Smaller font for instructions

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a background color (black)
    screen.fill(BLACK)

    # Render the text
    text_surface = font.render('Hello, Pygame!', True, WHITE)  # Render text, white color
    input_text_surface = input_font.render('Press any key to continue...', True, WHITE)  # Smaller text for instructions

    # Blit (draw) the text onto the screen at the specified position
    screen.blit(text_surface, (screen_width // 2 - text_surface.get_width() // 2, screen_height // 2 - text_surface.get_height() // 2))
    screen.blit(input_text_surface, (screen_width // 2 - input_text_surface.get_width() // 2, screen_height // 2 + 50))

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()


