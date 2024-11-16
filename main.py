import pygame
from src.screen_manager import ScreenManager
from src.screens.start_screen import StartScreen
from src.screens.game_screen import GameScreen
from src.screens.tutorial_screen import TutorialScreen
from src.screens.end_screen import EndScreen

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Elevation Quest')

screen_manager = ScreenManager()
start_screen = StartScreen(screen_manager, screen)
game_screen = GameScreen(screen_manager, screen)
tutorial_screen = TutorialScreen(screen_manager, screen)
end_screen = EndScreen(screen_manager, screen)

screen_manager.start_screen = start_screen
screen_manager.game_screen = game_screen
screen_manager.tutorial_screen = tutorial_screen
screen_manager.end_screen = end_screen

screen_manager.set_screen(start_screen)

def main():
    clock = pygame.time.Clock()
    running = True

    while running:
        time_delta = clock.tick(30) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            screen_manager.handle_event(event)

        screen_manager.update(time_delta)
        screen_manager.draw(screen)
        pygame.display.flip()

        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
