import pygame
import pygame_gui
from .base_screen import Screen

class TutorialScreen(Screen):
    def __init__(self, screen_manager, screen):
        self.screen = screen
        self.screen_manager = screen_manager
        self.manager = pygame_gui.UIManager((self.screen.get_width(), self.screen.get_height()), "assets/theme.json")
        self.background_image = pygame.image.load("assets/tutorial.jpg").convert()
      
        # self.background_image = pygame.transform.scale(self.background_image, (self.screen.get_width(), self.screen.get_height()))

        self.setup_ui()

    def setup_ui(self):
        """Creates the tutorial text and back button."""
        tutorial_text = (
            "Welcome to the Elevation Quest!\n\n"
            "You are shown a grid map of 30x30 cells with each cell having a height value assigned to it. A "
            "cell can either be water(height = 0) or land(height > 0). Connected land cells represent "
            "an island. The goal of the game is to find which island has the greatest average height. "
            "You can make your guess by clicking on any island and you have 3 attempts to guess the "
            "correct island.\n\n"
            "Good luck on your quest!"
        )

        self.instructions = pygame_gui.elements.UITextBox(
            html_text=tutorial_text,
            relative_rect=pygame.Rect((50, 50), (500, 400)),
            manager=self.manager
        )
        
        self.back_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((180, 480), (240, 50)),
            text="BACK TO START",
            manager=self.manager
        )

    def handle_event(self, event):
        """Handles button clicks on the tutorial screen."""
        self.manager.process_events(event)
        if event.type == pygame.USEREVENT and event.user_type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.back_button:
                self.screen_manager.set_screen(self.screen_manager.start_screen)

    def update(self, time_delta):
        """Updates the UI manager each frame."""
        self.manager.update(time_delta)

    def draw(self, screen):
        """Draws the tutorial screen and its UI components."""
        screen.blit(self.background_image, (0, 0))
        self.manager.draw_ui(screen)