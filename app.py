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
        self.balance_font = pygame.font.Font(None, 48)  # Smaller font for the balance
        self.balance_color = (255, 255, 255)  # White color for the balance
        self.game_over_font = pygame.font.Font(None, 120)  # Larger font for "Game Over"

        # Define the hitbox (x, y, width, height)
        self.hitbox = pygame.Rect(1128, 750, 160, 120)  # Example position and size for the hitbox
        self.hitbox2 = pygame.Rect(1290, 750, 160, 120)
        self.hitbox3 = pygame.Rect(966, 750, 160, 120)
        self.hitbox4 = pygame.Rect(1452, 750, 160, 120)

        # Initialize the player's balance
        self.balance = 1000

    def textRender(self):
        running = True
        result_text = ""  # To store the winner/loss result text
        result_displayed = False  # Flag to check if result has been displayed

        while running:
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Get the mouse position when clicked
                    mouse_pos = pygame.mouse.get_pos()
                    if self.hitbox.collidepoint(mouse_pos):  # Check if the mouse click is inside the hitbox
                        result_text = self.on_hitbox_click()  # Get random result
                        result_displayed = True
                    if self.hitbox2.collidepoint(mouse_pos):
                        result_text = self.on_hitbox2_click()
                        result_displayed = True
                    if self.hitbox3.collidepoint(mouse_pos):
                        result_text = self.on_hitbox3_click()
                        result_displayed = True
                    if self.hitbox4.collidepoint(mouse_pos):
                        result_text = self.on_hitbox4_click()
                        result_displayed = True

            # Blit the background image to the screen
            self.screen.blit(self.roulette_image, (0, 0))

            # Display result text after a hitbox is clicked
            if result_displayed:
                text_surface = self.font.render(result_text, True, self.text_color)
                self.screen.blit(text_surface, (590, 100))  # Position the text in place of the welcome message

            # Display the balance in the top-left corner
            balance_text = f"Balance: ${self.balance}"
            balance_surface = self.balance_font.render(balance_text, True, self.balance_color)
            self.screen.blit(balance_surface, (20, 20))  # Position the balance text

            # Check if balance is 0 or lower, end the game if true
            if self.balance <= 0:
                self.display_game_over()
                pygame.display.update()
                time.sleep(3)  # Display the game over message for 3 seconds
                running = False

            # Draw hitboxes
            pygame.draw.rect(self.screen, (0, 0, 255), self.hitbox, 2)
            pygame.draw.rect(self.screen, (0, 0, 255), self.hitbox2, 2)
            pygame.draw.rect(self.screen, (0, 0, 255), self.hitbox3, 2)
            pygame.draw.rect(self.screen, (0, 0, 255), self.hitbox4, 2)

            pygame.display.update()

        pygame.quit()

    def on_hitbox_click(self):
        result = random.choice(["Winner", "Loss", "Loss", "Loss"])  # Randomly pick Winner or Loss
        if result == "Winner":
            self.balance += 100  # Example: Increase balance by 100 if the user wins
        else:
            self.balance -= 50  # Example: Decrease balance by 50 if the user loses
        return f"In on red: {result}"
    
    def on_hitbox2_click(self):
        result = random.choice(["Winner", "Loss", "Loss", "Loss"])  # Randomly pick Winner or Loss
        if result == "Winner":
            self.balance += 100
        else:
            self.balance -= 50
        return f"In on black: {result}"
    
    def on_hitbox3_click(self):
        result = random.choice(["Winner", "Loss", "Loss", "Loss"])  # Randomly pick Winner or Loss
        if result == "Winner":
            self.balance += 100
        else:
            self.balance -= 50
        return f"In on even: {result}"
    
    def on_hitbox4_click(self):
        result = random.choice(["Winner", "Loss", "Loss", "Loss"])
        if result == "Winner":
            self.balance += 100
        else:
            self.balance -= 50
        return f"In on odd: {result}"

    def display_game_over(self):
        # Display "Game Over" message in the center of the screen
        game_over_text = "Game Over"
        game_over_surface = self.game_over_font.render(game_over_text, True, (50, 50, 255))
        text_rect = game_over_surface.get_rect(center=(self.screen_width // 2, self.screen_height // 2))
        self.screen.blit(game_over_surface, text_rect)

if __name__ == "__main__":
    roulette = RouletteWheel()
    roulette.textRender()