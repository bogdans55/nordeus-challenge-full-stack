import pygame
import pygame_gui
from .base_screen import Screen

class StartScreen(Screen):
    def __init__(self, screen_manager, screen):
        self.screen = screen
        self.screen_manager = screen_manager
        self.manager = pygame_gui.UIManager((self.screen.get_width(), self.screen.get_height()))
        self.setup_ui()

        self.background_image = pygame.image.load("assets/background.jpg").convert()
        # self.background_image = pygame.transform.scale(self.background_image, (self.screen.get_width(), self.screen.get_height()))


    def setup_ui(self):
        """Creates buttons for the start screen."""
        self.play_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((200, 150), (200, 50)),
            text="Play Game",
            manager=self.manager
        )
        
        self.settings_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((200, 220), (200, 50)),
            text="Options/Settings",
            manager=self.manager,
        )
        
        self.quit_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((200, 290), (200, 50)),
            text="Quit",
            manager=self.manager
        )

    def handle_event(self, event):
        """Handles button clicks on the start screen."""
        self.manager.process_events(event)
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.play_button:
                    self.screen_manager.set_screen(self.screen_manager.game_screen)
                elif event.ui_element == self.settings_button:
                    print("Settings clicked (optional screen)")
                elif event.ui_element == self.quit_button:
                    pygame.quit()
                    exit()

    def update(self, time_delta):
        """Updates the UI manager each frame."""
        self.manager.update(time_delta)

    def draw(self, screen):
        """Draws the start screen and its UI components."""
        screen.blit(self.background_image, (0, 0))
        self.manager.draw_ui(screen)
