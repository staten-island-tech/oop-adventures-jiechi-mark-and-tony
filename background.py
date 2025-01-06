import pygame

# Initialize pygame
pygame.init()

# Set up the screen (window size)
screen_width = 1920
screen_height = 1017
screen = pygame.display.set_mode((screen_width, screen_height))

# Set window title
pygame.display.set_caption("Background")

# Load a custom background image
background_image = pygame.image.load('backgroundwhite.jpg')  # Make sure the image path is correct

# Scale the background image to match the screen size (if necessary)
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with the background image
    screen.blit(background_image, (0, 0))

    # Optionally, you can add other elements like text or objects
    pygame.display.update()

# Quit pygame
pygame.quit()
