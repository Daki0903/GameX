import pygame

class GameEngine:
    def __init__(self, width=800, height=600, title="GameX"):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.running = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        pass  # Ovde se dodaje logika igre

    def render(self):
        self.screen.fill((0, 0, 0))
        pygame.display.flip()

    def run(self, fps=60):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(fps)

        pygame.quit()
