import pygame

class Sound:
    def __init__(self, sound_path):
        pygame.mixer.init()
        self.sound = pygame.mixer.Sound(sound_path)

    def play(self):
        self.sound.play()
