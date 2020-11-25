import pygame
import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

class SoundManager() :
    instance = None

    def __init__(self) :
        self.sound_dict = dict()

    @classmethod
    def getInstance(cls) :
        if cls.instance is None :
            cls.instance = SoundManager()
        return cls.instance

    def load_music(self, directory) :
        self.stop_music()

        pygame.mixer.music.load(directory)
        pygame.mixer.music.play(-1)

    def stop_music(self) :
        if pygame.mixer.get_busy() :
            pygame.mixer.music.stop()

    def load_sound(self, directory, sound_name) :
        sound = pygame.mixer.Sound(directory)
        self.sound_dict[sound_name] = sound

    def play_sound(self, sound_name) :
        self.sound_dict[sound_name].play()
