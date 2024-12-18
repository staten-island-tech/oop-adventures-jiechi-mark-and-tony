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
        self.hitbox2 = pygame.Rect(1290, 750, 160, 120)
        self.hitbox3 = pygame.Rect(966, 750, 160, 120)
        self.hitbox4 = pygame.Rect(1452, 750, 160, 120)

    def textRender(self):
        running = True
        text_list = [
            "Welcome to the Roulette table",
            "To place a bet click on the boxes highlighted in blue"
        ]
        text_index = 0  # Start with the first text
        current_text = ""  # Empty string to store progressively printed text
        start_time = pygame.time.get_ticks()  # Start time for slow printing
        text_displayed_time = 0  # Track the time since text was fully displayed
        text_duration = 5000  # Time in milliseconds for how long the text stays on screen

        while running:
            # Event handling
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
                    if self.hitbox3.collidepoint(mouse_pos):
                        self.on_hitbox3_click()
                    if self.hitbox4.collidepoint(mouse_pos):
                        self.on_hitbox4_click()

            # Blit the background image to the screen
            self.screen.blit(self.roulette_image, (0, 0))

            # Print the current text character by character (slow printing)
            if len(current_text) < len(text_list[text_index]) and pygame.time.get_ticks() - start_time > 10 * len(current_text):
                current_text += text_list[text_index][len(current_text)]  # Add next character
                start_time = pygame.time.get_ticks()  # Reset start time after printing a character

            # Render the text
            text_surface = self.font.render(current_text, True, self.text_color)
            self.screen.blit(text_surface, (590, 100))

            # Check if the text has been displayed long enough (e.g., 5 seconds)
            if text_displayed_time > text_duration:
                # Move to the next text in the list
                text_index += 1
                current_text = ""  # Reset current text to print the next one
                text_displayed_time = 0  # Reset the timer

            text_displayed_time = pygame.time.get_ticks() - start_time

            # If all texts have been shown, exit the loop
            if text_index >= len(text_list):
                running = False

            # Draw hitboxes
            pygame.draw.rect(self.screen, (0, 0, 255), self.hitbox, 2)
            pygame.draw.rect(self.screen, (0, 0, 255), self.hitbox2, 2)
            pygame.draw.rect(self.screen, (0, 0, 255), self.hitbox3, 2)
            pygame.draw.rect(self.screen, (0, 0, 255), self.hitbox4, 2)

            pygame.display.update()

        pygame.quit()

    def on_hitbox_click(self):
        print("In on red")
    def on_hitbox2_click(self):
        print("In on black")
    def on_hitbox3_click(self):
        print("In on even")
    def on_hitbox4_click(self):
        print("In on odd")

if __name__ == "__main__":
    roulette = RouletteWheel()
    roulette.textRender()