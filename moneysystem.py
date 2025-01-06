import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants for the screen
WIDTH, HEIGHT = 1200, 800  # Increased screen size

# Load background image
background_image = pygame.image.load('Your paragraph text.jpg')
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))  # Scale to fit the entire window

# Inventory class
class Inventory:
    def __init__(self, balance=1000):
        self.balance = balance
        self.gambling_balance = 0  # Initialize gambling balance

    def withdraw(self, amount):
        if amount <= 0:
            return "Please choose a positive number."
        elif amount > self.balance:
            return f"You cannot withdraw more than your balance of {self.balance}."
        else:
            self.balance -= amount
            self.gambling_balance += amount  # Add withdrawn amount to gambling balance
            return f'{amount} has been withdrawn to gambling. New balance: {self.balance}. Gambling balance: {self.gambling_balance}.'

    def deposit(self, amount):
        if amount <= 0:
            return "Choose a valid amount."
        elif amount > self.gambling_balance:  # Check if deposit exceeds gambling balance
            return "Cannot deposit more than your gambling balance."
        elif self.balance + amount > 1_000_000:  # Check max balance limit
            return "Cannot exceed $1,000,000 in total balance."
        else:
            self.balance += amount
            self.gambling_balance -= amount  # Deduct the deposited amount from gambling balance
            return f'{amount} has been added. New balance: {self.balance}. Gambling balance: {self.gambling_balance}.'

# Main function
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Inventory Management")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 48)  # Increased font size for balances

    inventory = Inventory()
    input_amount = ""
    action = None
    message = ""

    # Define enlarged hitboxes for buttons
    withdraw_button_rect = pygame.Rect(20, 20, 400, 150)  # Enlarged Withdraw button
    deposit_button_rect = pygame.Rect(WIDTH - 420, 20, 400, 150)  # Enlarged Deposit button
    input_rect = pygame.Rect(400, 350, 400, 100)  # Enlarged input field

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_BACKSPACE:
                    input_amount = input_amount[:-1]
                elif event.key == pygame.K_RETURN:
                    try:
                        amount = float(input_amount)
                        if action == "Withdraw":
                            message = inventory.withdraw(amount)
                        elif action == "Deposit":
                            message = inventory.deposit(amount)
                        input_amount = ""  # Clear input after action
                        action = None  # Reset action after processing
                    except ValueError:
                        message = "Please enter a valid number."
                else:
                    if action:  # Allow input only if an action is selected
                        input_amount += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if withdraw_button_rect.collidepoint((x, y)):
                    action = "Withdraw"
                    input_amount = ""  # Clear previous input
                elif deposit_button_rect.collidepoint((x, y)):
                    action = "Deposit"
                    input_amount = ""  # Clear previous input

        # Draw the background image covering the whole screen
        screen.blit(background_image, (0, 0))

        # Draw input amount slightly higher
        input_text_surface = font.render(input_amount, True, (0, 0, 0))  # No label
        screen.blit(input_text_surface, (input_rect.x - 100, input_rect.y - 50))  # Move slightly higher

        # Draw the current balance, slightly up
        balance_text_surface = font.render(f'Balance: ${inventory.balance}', True, (255, 255, 255))  # White text for balance
        screen.blit(balance_text_surface, (WIDTH // 2 - 180, HEIGHT - 120))  # Position adjusted up

        # Draw the gambling balance, slightly up
        gambling_balance_text_surface = font.render(f'Gambling Balance: ${inventory.gambling_balance}', True, (255, 255, 255))  # White text for gambling balance
        screen.blit(gambling_balance_text_surface, (WIDTH // 2 - 180, HEIGHT - 150))  # Position adjusted up

        # Show messages in the upper part of the bottom right corner
        message_surface = font.render(message, True, (255, 255, 255))  # White text for messages
        message_rect = message_surface.get_rect(bottomright=(WIDTH - 20, HEIGHT - 20))  # Position it in the bottom right
        screen.blit(message_surface, message_rect)

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
