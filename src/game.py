# src/game.py

import pygame
from src.grid import Grid

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.grid = Grid(screen)
        self.guesses_left = 3
        self.game_over = False
        self.won = False

        self.target_island = self.grid.find_highest_average_island()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and not self.game_over:
            mouse_x, mouse_y = event.pos
            self.process_guess(mouse_x, mouse_y)

    def process_guess(self, x, y):
        """Processes the user's guess by clicking on a cell."""
        row, col = y // self.grid.cell_size, x // self.grid.cell_size
        if (row, col) in self.target_island:
            self.won = True
            self.game_over = True
        else:
            self.guesses_left -= 1
            if self.guesses_left == 0:
                self.game_over = True  

    def update(self):
        pass

    def draw(self):
        self.grid.draw()
        self.display_info()

    def display_info(self):
        font = pygame.font.Font(None, 36)
        if self.won:
            text = font.render("Correct Island! You found it!", True, (0, 255, 0))
        elif self.game_over:
            text = font.render("Out of guesses! Game Over.", True, (255, 0, 0))
        else:
            text = font.render(f"Guesses left: {self.guesses_left}", True, (0, 0, 0))
        self.screen.blit(text, (10, 10))
