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
        self.hitbox = pygame.Rect(1128, 750, 160, 120)  # Example position and size for the hitbox
        self.hitbox2 = pygame.Rect(1228, 750, 160, 120)
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
                    if self.hitbox2.collidepoint(mouse_pos):
                        self.on_hitbox2_click()
            # Blit the background image to the screen
            self.screen.blit(self.roulette_image, (0, 0))

            # Render the text
            text = self.font.render('Welcome to the Roulette table.', True, self.text_color)
            self.screen.blit(text, (590, 100))

            pygame.draw.rect(self.screen, (0, 0, 255), self.hitbox, 2)
            pygame.draw.rect(self.screen, (0, 0, 255), self.hitbox2, 2)
            pygame.display.update()

        pygame.quit()
        sys.exit()

    def on_hitbox_click(self):
        print("Hitbox clicked!")

if __name__ == "__main__":
    roulette = RouletteWheel()
    roulette.textRender()