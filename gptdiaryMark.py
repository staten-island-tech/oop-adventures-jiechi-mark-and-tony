#How can i display an image on the screen when i run python?
"""         self.screen_width = 1920
        self.screen_height = 1017

        pygame.init()

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Roulette Background')

        self.roulette_image = pygame.image.load('roulettewheel.jpeg')
        self.roulette_image = pygame.transform.scale(self.roulette_image, (self.screen_width, self.screen_height))"""

#How can i add text to the screen? 
"""    def textRender(self):
        running = True
        result_text = ""  
        result_displayed = False 
            bet_types = ["red", "black", "even", "odd"]"""

#how can i implement hitboxes into the game that can be coded to do different things?
"""         self.hitbox = pygame.Rect(1128, 750, 160, 120)
        self.hitbox2 = pygame.Rect(1290, 750, 160, 120)
        self.hitbox3 = pygame.Rect(966, 750, 160, 120)
        self.hitbox4 = pygame.Rect(1452, 750, 160, 120)
        hitboxes = [self.hitbox, self.hitbox2, self.hitbox3, self.hitbox4]
                    bet_types = ["red", "black", "even", "odd"]

                    for hitbox, bet_type in zip(hitboxes, bet_types):
                        if hitbox.collidepoint(mouse_pos):
                            result_text = self.on_hitbox_click(bet_type)
                            result_displayed = True
                            break """

#How can i make it so that i can bet a custom amount of money?
"""                     if self.bet_50.collidepoint(mouse_pos) and self.balance >= 50:
                        self.bet = 50
                    elif self.bet_100.collidepoint(mouse_pos) and self.balance >= 100:
                        self.bet = 100
                    elif self.bet_250.collidepoint(mouse_pos) and self.balance >= 250:
                        self.bet = 250
                    elif self.bet_500.collidepoint(mouse_pos) and self.balance >= 500:
                        self.bet = 500
                    elif self.bet_1000.collidepoint(mouse_pos) and self.balance >= 1000:
                        self.bet = 1000

            self.draw_bet_option(self.bet_50, "50", self.balance >= 50)
            self.draw_bet_option(self.bet_100, "100", self.balance >= 100)
            self.draw_bet_option(self.bet_250, "250", self.balance >= 250)
            self.draw_bet_option(self.bet_500, "500", self.balance >= 500)
            self.draw_bet_option(self.bet_1000, "1000", self.balance >= 1000) """

#How can i make a game over screen?
"""     def display_game_over(self):
        game_over_text = "Game Over"
        game_over_surface = self.game_over_font.render(game_over_text, True, (50, 50, 255))
        text_rect = game_over_surface.get_rect(center=(self.screen_width // 2, self.screen_height // 2))
        self.screen.blit(game_over_surface, text_rect) """

#how can i make it so that if i dont have the amount of money to bet on something the option goes away and changes the current bet to something lower?
"""     def draw_bet_option(self, rect, text, can_afford):
        if not can_afford:
            pygame.draw.rect(self.screen, (150, 150, 150), rect)
        else:
            pygame.draw.rect(self.screen, (255, 30, 0), rect)
        text_surface = self.balance_font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=rect.center)
        self.screen.blit(text_surface, text_rect) """
#How can i condense my code of the hitboxes?
"""     def on_hitbox_click(self, bet_type):
        result = random.choice(["Winner", "Loss", "Loss"])
        if result == "Winner":
            self.balance += self.bet
        else:
            self.balance -= self.bet
        return f"In on {bet_type}: {result}" """

