import pygame

pygame.init()


class Game():
    def __init__(self, level, camera, tiles, screen, player=None):
        self.level = level
        self.camera = camera
        self.tiles = tiles
        self.player = player
        self.screen = screen
        self.window_title = None
        self.window_width = None
        self.window_height = None
        self.icon = None
        self.bg_color = (255, 255, 255)

    def draw(self):
        self.screen.fill(self.bg_color)
        self.level.render([self.window_width, self.window_height])
        self.camera.update()

    def input(self, event, key):
        if event.key == key:
            return True
        else:
            return False

    def update(self, game_pygame=None):
        self.draw()
        if game_pygame:
            game_pygame.display.update()

    def events(self, game_pygame):
        info_list = [None, None]
        for event in game_pygame.event.get():
            if event.type == game_pygame.QUIT:
                info_list[0] = False
            info_list[1] = event
        return info_list

    def load_image(self, path):
        image = pygame.image.load(path)
        return image

    def load_sound(self, path):
        sound = pygame.mixer.Sound(path)
        return sound

    def setMusic(self, path):
        pygame.mixer.music.load(path)

    def playMusic(self, loops, start, fade_ms):
        pygame.mixer.music.play(loops,start,fade_ms)

    def setMusicVolume(self, volume):
        pygame.mixer.music.set_volume(volume)

    def playSound(self, sound, loops, start, fade_ms):
        sound.play(loops, start, fade_ms)

    def setSoundVolume(self, volume, sound):
        sound.set_volume(volume)






