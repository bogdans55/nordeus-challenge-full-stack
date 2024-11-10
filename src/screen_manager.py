class ScreenManager:
    def __init__(self):
        self.current_screen = None

    def set_screen(self, screen):
        self.current_screen = screen

    def handle_event(self, event):
        if self.current_screen:
            self.current_screen.handle_event(event)

    def update(self, time_delta):
        if self.current_screen:
            self.current_screen.update(time_delta)

    def draw(self, screen):
        if self.current_screen:
            self.current_screen.draw(screen)
