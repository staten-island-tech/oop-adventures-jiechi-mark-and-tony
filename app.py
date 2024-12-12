import random
import sys
import pygame
import time

class RouletteWheel():
    def __init__(self): 
        # Screen dimensions
        self.screen_width = 1920
        self.screen_height = 1017

        # Initialize Pygame
        pygame.init()

        # Set up display (only do this once)
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Roulette Background')

        # Load and scale the background image
        self.roulette_image = pygame.image.load('roulettewheel.jpeg')
        self.roulette_image = pygame.transform.scale(self.roulette_image, (self.screen_width, self.screen_height))

        # Font settings
        self.font = pygame.font.Font(None, 74)
        self.text_color = (200, 155, 110)  

        # Define the hitbox (x, y, width, height)
        self.hitbox = pygame.Rect(200, 200, 200, 200)  # Example position and size for the hitbox

    def textRender(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Get the mouse position when clicked
                    mouse_pos = pygame.mouse.get_pos()
                    if self.hitbox.collidepoint(mouse_pos):  # Check if the mouse click is inside the hitbox
                        self.on_hitbox_click()  # Trigger the action

            # Blit the background image to the screen
            self.screen.blit(self.roulette_image, (0, 0))

            # Render the text
            text = self.font.render('Welcome to the Roulette table.', True, self.text_color)
            self.screen.blit(text, (590, 100))

            # Draw the hitbox (for visualization)
            pygame.draw.rect(self.screen, (0, 0, 255), self.hitbox, 2)  # Red color for hitbox boundary

            # Update the display
            pygame.display.update()

        # Quit Pygame
        pygame.quit()
        sys.exit()

    def on_hitbox_click(self):
        print("Hitbox clicked!")

if __name__ == "__main__":
    roulette = RouletteWheel()
    roulette.textRender()