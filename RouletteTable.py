import random
import sys
import pygame
import time

class RouletteWheel():
    def __init__(self): 
        self.screen_width = 1920
        self.screen_height = 1017

        pygame.init()

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Roulette Background')

        self.roulette_image = pygame.image.load('roulettewheel.jpeg')
        self.roulette_image = pygame.transform.scale(self.roulette_image, (self.screen_width, self.screen_height))

        self.font = pygame.font.Font(None, 74)
        self.text_color = (200, 155, 110)  
        self.balance_font = pygame.font.Font(None, 48)
        self.balance_color = (255, 255, 255)
        self.game_over_font = pygame.font.Font(None, 120)

        self.hitbox = pygame.Rect(1128, 750, 160, 120)
        self.hitbox2 = pygame.Rect(1290, 750, 160, 120)
        self.hitbox3 = pygame.Rect(966, 750, 160, 120)
        self.hitbox4 = pygame.Rect(1452, 750, 160, 120)

        self.bet_50 = pygame.Rect(100, 925, 150, 60)
        self.bet_100 = pygame.Rect(300, 925, 150, 60)
        self.bet_250 = pygame.Rect(500, 925, 150, 60)
        self.bet_500 = pygame.Rect(700, 925, 150, 60)
        self.bet_1000 = pygame.Rect(900, 925, 150, 60)

        self.balance = 1000
        self.bet = 50 

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

                    if self.bet_50.collidepoint(mouse_pos) and self.balance >= 50:
                        self.bet = 50
                    elif self.bet_100.collidepoint(mouse_pos) and self.balance >= 100:
                        self.bet = 100
                    elif self.bet_250.collidepoint(mouse_pos) and self.balance >= 250:
                        self.bet = 250
                    elif self.bet_500.collidepoint(mouse_pos) and self.balance >= 500:
                        self.bet = 500
                    elif self.bet_1000.collidepoint(mouse_pos) and self.balance >= 1000:
                        self.bet = 1000

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

            pygame.draw.rect(self.screen, (0, 0, 255), self.hitbox, 2)
            pygame.draw.rect(self.screen, (0, 0, 255), self.hitbox2, 2)
            pygame.draw.rect(self.screen, (0, 0, 255), self.hitbox3, 2)
            pygame.draw.rect(self.screen, (0, 0, 255), self.hitbox4, 2)

            self.draw_bet_option(self.bet_50, "50", self.balance >= 50)
            self.draw_bet_option(self.bet_100, "100", self.balance >= 100)
            self.draw_bet_option(self.bet_250, "250", self.balance >= 250)
            self.draw_bet_option(self.bet_500, "500", self.balance >= 500)
            self.draw_bet_option(self.bet_1000, "1000", self.balance >= 1000)

            pygame.display.update()

        pygame.quit()

    def draw_bet_option(self, rect, text, can_afford):
        if not can_afford:
            pygame.draw.rect(self.screen, (150, 150, 150), rect)
        else:
            pygame.draw.rect(self.screen, (255, 30, 0), rect)
        text_surface = self.balance_font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=rect.center)
        self.screen.blit(text_surface, text_rect)

    def on_hitbox_click(self):
        result = random.choice(["Winner", "Loss", "Loss"])
        if result == "Winner":
            self.balance += self.bet
        else:
            self.balance -= self.bet
        return f"In on red: {result}"
    
    def on_hitbox2_click(self):
        result = random.choice(["Winner", "Loss", "Loss"])
        if result == "Winner":
            self.balance += self.bet
        else:
            self.balance -= self.bet
        return f"In on black: {result}"
    
    def on_hitbox3_click(self):
        result = random.choice(["Winner", "Loss", "Loss"])
        if result == "Winner":
            self.balance += self.bet
        else:
            self.balance -= self.bet
        return f"In on even: {result}"
    
    def on_hitbox4_click(self):
        result = random.choice(["Winner", "Loss", "Loss"])
        if result == "Winner":
            self.balance += self.bet
        else:
            self.balance -= self.bet
        return f"In on odd: {result}"

    def display_game_over(self):
        game_over_text = "Game Over"
        game_over_surface = self.game_over_font.render(game_over_text, True, (50, 50, 255))
        text_rect = game_over_surface.get_rect(center=(self.screen_width // 2, self.screen_height // 2))
        self.screen.blit(game_over_surface, text_rect)

if __name__ == "__main__":
    roulette = RouletteWheel()
    roulette.textRender()
