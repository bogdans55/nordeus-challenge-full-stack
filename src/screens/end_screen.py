import pygame
import pygame_gui
from .base_screen import Screen

class EndScreen(Screen):
    def __init__(self, screen_manager, screen):
        self.screen = screen
        self.screen_manager = screen_manager
        self.manager = pygame_gui.UIManager((self.screen.get_width(), self.screen.get_height()), "assets/theme.json")
        self.game_won = False
      
        # self.background_image = pygame.transform.scale(self.background_image, (self.screen.get_width(), self.screen.get_height()))

        self.setup_ui()

    def setup_ui(self):
        """Creates buttons for the end screen."""
        self.restart_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((80, 490), (200, 50)),
            text="PLAY AGAIN",
            manager=self.manager
        )
        
        self.quit_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((320, 490), (200, 50)),
            text="QUIT",
            manager=self.manager
        )

    def handle_event(self, event):
        self.manager.process_events(event)
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.restart_button:
                    self.screen_manager.set_screen(self.screen_manager.start_screen)
                elif event.ui_element == self.quit_button:
                    pygame.quit()
                    exit()

    def update(self, time_delta):
        self.manager.update(time_delta)

    def draw(self, screen):
        if self.game_won:
            # self.background_image = pygame.image.load("assets/won.jpg").convert()
            self.background_image = pygame.image.load("assets/won_edit.jpg").convert()
        else:
            # self.background_image = pygame.image.load("assets/lost.jpg").convert()
            self.background_image = pygame.image.load("assets/lost_edit.jpg").convert()
        screen.blit(self.background_image, (0, 0))
        self.manager.draw_ui(screen)
