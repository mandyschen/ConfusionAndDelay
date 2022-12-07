import pygame
import glob


class GameGUI:

    def __init__(self):
        self.clock = pygame.time.Clock()

    def start(self):
        pygame.font.init()
        pygame.mixer.init()
        pygame.display.init()
        self.load_sounds()

    def load_sounds(self):
        self.sounds = {}
        for sound_file in glob.glob(f"./sounds/*.mp3"):
            sound = pygame.mixer.Sound(sound_file)
            sound.set_volume(0.5)
            self.sounds[sound_file] = sound

    def play_sound(self, sound):
        pygame.mixer.music.stop()
        if sound == "thomas_theme" or sound == "bg_music":
            self.sounds[f'./sounds/{sound}.mp3'].play(-1)
        else:
            self.sounds[f'./sounds/{sound}.mp3'].play()