import sys
import random
import time
import pygame


# Initialize Pygame
pygame.init()


# Constants for the screen
WIDTH, HEIGHT = 1200, 800
ROULETTE_WIDTH, ROULETTE_HEIGHT = 1920, 1017


# Load background image
background_image = pygame.image.load('Your paragraph text.jpg')
background_image = pygame.transform.scale(background_image, (ROULETTE_WIDTH, ROULETTE_HEIGHT))


# Inventory class
class Inventory:
    def __init__(self, balance=1000):
        self.balance = balance  # Main account balance
        self.gambling_balance = 0  # Money available for betting


    def withdraw(self, amount):
        if amount <= 0:
            return "Please choose a positive number."
        elif amount > self.balance:
            return f"You cannot withdraw more than your balance of {self.balance}."
        else:
            self.balance -= amount
            self.gambling_balance += amount
            return f'{amount} has been withdrawn to gambling. New balance: {self.balance}. Gambling balance: {self.gambling_balance}.'


    def deposit(self, amount):
        if amount <= 0:
            return "Choose a valid amount."
        elif amount > self.gambling_balance:
            return "Cannot deposit more than your gambling balance."
        elif self.balance + amount > 1_000_000:
            return "Cannot exceed $1,000,000 in total balance."
        else:
            self.balance += amount
            self.gambling_balance -= amount
            return f'{amount} has been added. New balance: {self.balance}. Gambling balance: {self.gambling_balance}.'


# Roulette class
class RouletteWheel:
    def __init__(self, inventory):
        self.screen_width = ROULETTE_WIDTH
        self.screen_height = ROULETTE_HEIGHT
        self.inventory = inventory
        self.balance = inventory.gambling_balance  # Starting with gambling balance
        self.bet = 50
        self.game_active = True
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Roulette Background')


        self.roulette_image = pygame.image.load('roulettewheel.jpeg')
        self.roulette_image = pygame.transform.scale(self.roulette_image, (self.screen_width, self.screen_height))


        self.font = pygame.font.Font(None, 74)
        self.text_color = (200, 155, 110)
        self.balance_font = pygame.font.Font(None, 48)
        self.balance_color = (255, 255, 255)
        self.game_over_font = pygame.font.Font(None, 120)


        # Hitboxes for betting options
        self.hitbox = pygame.Rect(1128, 750, 160, 120)
        self.hitbox2 = pygame.Rect(1290, 750, 160, 120)
        self.hitbox3 = pygame.Rect(966, 750, 160, 120)
        self.hitbox4 = pygame.Rect(1452, 750, 160, 120)


        # Betting options
        self.bet_options = {50: pygame.Rect(100, 925, 150, 60), 100: pygame.Rect(300, 925, 150, 60),
                            250: pygame.Rect(500, 925, 150, 60), 500: pygame.Rect(700, 925, 150, 60),
                            1000: pygame.Rect(900, 925, 150, 60)}


        # Back button hitbox in top-right corner
        self.back_button_rect = pygame.Rect(ROULETTE_WIDTH - 200, 20, 180, 60)


    def textRender(self):
        running = True
        result_text = ""
        result_displayed = False


        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()


                    if self.hitbox.collidepoint(mouse_pos):
                        result_text = self.on_hitbox_click()
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


                    for bet_amount, rect in self.bet_options.items():
                        if rect.collidepoint(mouse_pos) and self.balance >= bet_amount:
                            self.bet = bet_amount


                    # Check if back button was clicked
                    if self.back_button_rect.collidepoint(mouse_pos):
                        running = False  # Close roulette and return to main menu


            if self.bet > self.balance:
                self.bet = self.balance


            self.screen.blit(self.roulette_image, (0, 0))


            if result_displayed:
                text_surface = self.font.render(result_text, True, self.text_color)
                self.screen.blit(text_surface, (590, 100))


            balance_text = f"Balance: ${self.balance}"
            balance_surface = self.balance_font.render(balance_text, True, self.balance_color)
            self.screen.blit(balance_surface, (20, 20))


            bet_text = f"Bet: ${self.bet}"
            bet_surface = self.balance_font.render(bet_text, True, self.balance_color)
            self.screen.blit(bet_surface, (20, 80))


            if self.balance <= 0:
                self.display_game_over()
                pygame.display.update()
                time.sleep(3)
                running = False


            # Draw hitboxes for betting options
            for rect in [self.hitbox, self.hitbox2, self.hitbox3, self.hitbox4]:
                pygame.draw.rect(self.screen, (0, 0, 255), rect, 2)


            # Draw bet options
            for bet_amount, rect in self.bet_options.items():
                self.draw_bet_option(rect, str(bet_amount), self.balance >= bet_amount)


            # Draw back button
            pygame.draw.rect(self.screen, (255, 0, 0), self.back_button_rect)
            back_button_text = self.font.render("Back", True, (255, 255, 255))
            self.screen.blit(back_button_text, (self.back_button_rect.x + 60, self.back_button_rect.y + 10))


            pygame.display.update()


        # When exiting roulette, save the gambling balance back to inventory
        self.inventory.gambling_balance = self.balance  # Update gambling balance in inventory
        # Return control back to the main screen
        return "Roulette finished"


    def draw_bet_option(self, rect, text, can_afford):
        color = (150, 150, 150) if not can_afford else (255, 30, 0)
        pygame.draw.rect(self.screen, color, rect)
        text_surface = self.balance_font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=rect.center)
        self.screen.blit(text_surface, text_rect)


    def on_hitbox_click(self):
        return self.resolve_bet("red")


    def on_hitbox2_click(self):
        return self.resolve_bet("black")


    def on_hitbox3_click(self):
        return self.resolve_bet("even")


    def on_hitbox4_click(self):
        return self.resolve_bet("odd")


    def resolve_bet(self, color):
        result = random.choice(["Winner", "Loss", "Loss"])
        if result == "Winner":
            self.balance += self.bet
        else:
            self.balance -= self.bet
        return f"In on {color}: {result}"


    def display_game_over(self):
        self.game_active = False
        game_over_text = "Game Over"
        game_over_surface = self.game_over_font.render(game_over_text, True, (50, 50, 255))
        text_rect = game_over_surface.get_rect(center=(self.screen_width // 2, self.screen_height // 2))
        self.screen.blit(game_over_surface, text_rect)


# Main function for the inventory management screen
def main():
    # Set screen to the resolution of the roulette wheel
    screen = pygame.display.set_mode((ROULETTE_WIDTH, ROULETTE_HEIGHT))
    pygame.display.set_caption("Inventory Management")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 48)


    inventory = Inventory()
    input_amount = ""
    action = None
    message = ""


    # Define hitboxes for buttons (but no longer draw rectangles or text)
    withdraw_button_rect = pygame.Rect(20, 100, 600, 150)  # Moved down and left
    deposit_button_rect = pygame.Rect(ROULETTE_WIDTH - 800, 100, 600, 150)  # Moved down and right
    roulette_button_rect = pygame.Rect(500, 600, 200, 100)  # Hitbox for roulette button


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
                        if action == "Deposit":
                            message = inventory.deposit(amount)
                        elif action == "Withdraw":
                            message = inventory.withdraw(amount)
                        input_amount = ""
                        action = None
                    except ValueError:
                        message = "Please enter a valid number."
                   
                    # Check if both balance and gambling balance are zero after any deposit or withdrawal
                    if inventory.balance == 0 and inventory.gambling_balance == 0:
                        pygame.quit()
                        sys.exit()


                else:
                    if action:
                        input_amount += event.unicode


            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if deposit_button_rect.collidepoint((x, y)):
                    action = "Deposit"
                    input_amount = ""
                elif withdraw_button_rect.collidepoint((x, y)):
                    action = "Withdraw"
                    input_amount = ""
                elif roulette_button_rect.collidepoint((x, y)):  # Check if roulette button is clicked
                    if inventory.gambling_balance <= 0:  # Check if gambling balance is 0
                        message = "You need gambling balance to play roulette!"
                    else:
                        roulette = RouletteWheel(inventory)
                        roulette.textRender()  # Start roulette game
                        message = "Returned to inventory management"


        screen.blit(background_image, (0, 0))


        # Render input amount text
        input_text_surface = font.render(input_amount, True, (0, 0, 0))
        screen.blit(input_text_surface, (425, 425))


        # Render balance text
        balance_text_surface = font.render(f'Balance: ${inventory.balance}', True, (255, 255, 255))
        screen.blit(balance_text_surface, (ROULETTE_WIDTH // 2 - 180, ROULETTE_HEIGHT - 120))


        # Render gambling balance text
        gambling_balance_text_surface = font.render(f'Gambling Balance: ${inventory.gambling_balance}', True, (255, 255, 255))
        screen.blit(gambling_balance_text_surface, (ROULETTE_WIDTH // 2 - 180, ROULETTE_HEIGHT - 150))


        # Show messages in the bottom right corner
        message_surface = font.render(message, True, (255, 255, 255))
        message_rect = message_surface.get_rect(bottomright=(ROULETTE_WIDTH - 20, ROULETTE_HEIGHT - 20))
        screen.blit(message_surface, message_rect)


        # Draw the roulette button
        pygame.draw.rect(screen, (0, 255, 0), roulette_button_rect)
        roulette_button_text = font.render("Go to Roulette", True, (0, 0, 0))
        screen.blit(roulette_button_text, (roulette_button_rect.x + 10, roulette_button_rect.y + 30))


        pygame.display.flip()
        clock.tick(30)


if __name__ == "__main__":
    main()


