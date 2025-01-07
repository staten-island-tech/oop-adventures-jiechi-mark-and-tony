import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FONT = pygame.font.SysFont("Arial", 24)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
NUM_SIZE = 50
NUM_MARGIN = 10
ROWS = 10
COLS = 7
NUMBERS = list(range(1, 71))  # Numbers from 1 to 70

# Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Lottery Game")

class Ticket():
    def __init__(self, guesses=5):
        self.guesses = guesses
        self.guess = []
        self.random_number = []
        self.guessing = True

    def rlotto(self):
        # Generate 5 random unique numbers
        self.random_number = random.sample(range(1, 71), self.guesses)

    def reveal(self):
        # Sort both lists for comparison (since order doesn't matter)
        if sorted(self.guess) == sorted(self.random_number):
            return True
        else:
            return False

ticket = Ticket()

# Function to draw the lottery numbers
def draw_numbers():
    for i, num in enumerate(NUMBERS):
        row = i // COLS
        col = i % COLS
        x = col * (NUM_SIZE + NUM_MARGIN) + NUM_MARGIN
        y = row * (NUM_SIZE + NUM_MARGIN) + NUM_MARGIN
        pygame.draw.rect(screen, WHITE, (x, y, NUM_SIZE, NUM_SIZE))
        pygame.draw.rect(screen, BLUE, (x, y, NUM_SIZE, NUM_SIZE), 2)  # Border
        text_surface = FONT.render(str(num), True, BLUE)
        screen.blit(text_surface, (x + (NUM_SIZE - text_surface.get_width()) // 2, 
                                   y + (NUM_SIZE - text_surface.get_height()) // 2))

# Function to draw the guesses at the top-right corner
def draw_guesses():
    start_x = SCREEN_WIDTH - (NUM_SIZE + NUM_MARGIN) * len(ticket.guess) - NUM_MARGIN  # Calculate the starting x position
    for i, num in enumerate(ticket.guess):
        x = start_x + i * (NUM_SIZE + NUM_MARGIN)  # Calculate the position for each number
        y = NUM_MARGIN  # Keep them at the top
        pygame.draw.rect(screen, GREEN, (x, y, NUM_SIZE, NUM_SIZE))
        pygame.draw.rect(screen, BLUE, (x, y, NUM_SIZE, NUM_SIZE), 2)  # Border
        text_surface = FONT.render(str(num), True, WHITE)
        screen.blit(text_surface, (x + (NUM_SIZE - text_surface.get_width()) // 2, 
                                   y + (NUM_SIZE - text_surface.get_height()) // 2))

# Function to draw the random numbers at the bottom-right corner
def draw_random_numbers():
    start_x = SCREEN_WIDTH - (NUM_SIZE + NUM_MARGIN) * len(ticket.random_number) - NUM_MARGIN  # Calculate the starting x position
    for i, num in enumerate(ticket.random_number):
        x = start_x + i * (NUM_SIZE + NUM_MARGIN)  # Calculate the position for each number
        y = SCREEN_HEIGHT - NUM_SIZE - NUM_MARGIN  # Position them at the bottom
        pygame.draw.rect(screen, YELLOW, (x, y, NUM_SIZE, NUM_SIZE))
        pygame.draw.rect(screen, BLUE, (x, y, NUM_SIZE, NUM_SIZE), 2)  # Border
        text_surface = FONT.render(str(num), True, WHITE)
        screen.blit(text_surface, (x + (NUM_SIZE - text_surface.get_width()) // 2, 
                                   y + (NUM_SIZE - text_surface.get_height()) // 2))

# Function to draw the result
def draw_result():
    if not ticket.guessing:
        result_text = "You Win!" if ticket.reveal() else "You Lose!"
        text_surface = FONT.render(result_text, True, RED)
        screen.blit(text_surface, (SCREEN_WIDTH // 2 - text_surface.get_width() // 2, 
                                   SCREEN_HEIGHT // 2 - text_surface.get_height() // 2))

# Main game loop
def main():
    ticket.rlotto()  # Generate random numbers once at the beginning
    clock = pygame.time.Clock()
    
    while True:
        screen.fill((0, 0, 0))  # Clear screen with black
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and ticket.guessing:
                mx, my = pygame.mouse.get_pos()
                
                # Determine clicked number
                for i, num in enumerate(NUMBERS):
                    row = i // COLS
                    col = i % COLS
                    x = col * (NUM_SIZE + NUM_MARGIN) + NUM_MARGIN
                    y = row * (NUM_SIZE + NUM_MARGIN) + NUM_MARGIN
                    
                    if x <= mx <= x + NUM_SIZE and y <= my <= y + NUM_SIZE:
                        if num not in ticket.guess and len(ticket.guess) < ticket.guesses:
                            ticket.guess.append(num)
                        elif num in ticket.guess:
                            ticket.guess.remove(num)

                # End guessing if 5 numbers are selected
                if len(ticket.guess) == ticket.guesses:
                    ticket.guessing = False

        # Draw the lottery numbers
        draw_numbers()

        # Draw the user's selected guesses at the top-right
        draw_guesses()

        # Draw the random lottery numbers at the bottom-right if the guessing is finished
        if not ticket.guessing:
            draw_random_numbers()

        # Draw the result if the guessing is done
        draw_result()

        # Update display
        pygame.display.flip()

        # Limit the frame rate
        clock.tick(60)

# Start the game
main()
