import pygame
from .base_screen import Screen
from src.game import Game

class GameScreen(Screen):
    def __init__(self, screen_manager, screen):
        self.screen_manager = screen_manager
        self.game = Game(screen)

    def handle_event(self, event):
        self.game.handle_event(event)

    def update(self, time_delta):
        self.game.update(time_delta)
        if self.game.game_over:
            self.screen_manager.end_screen.game_won = self.game.won
            self.screen_manager.set_screen(self.screen_manager.end_screen)
            self.game = Game(self.game.screen)

    def draw(self, screen):
        self.game.draw()
