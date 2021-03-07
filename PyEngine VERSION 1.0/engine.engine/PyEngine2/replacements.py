import pygame

pygame.init()

def group():
    return pygame.sprite.Group()

def PyEngineWindow(window_width, window_height):
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption(" PyEngineGL ")
    return screen
def PyEngineWindowTitleSet(title):
    pygame.display.set_caption(title)

def PyEngineWindowTitleGet():
    return pygame.display.get_caption()

def PyEngineWindowIconSet(icon):
    pygame.display.set_icon(icon)

def PyEngineWindowIconGet():
    return pygame.display.get_caption()

def PyEngineInit():
    pygame.init()

def PyEngineUninit():
    pygame.quit()

def surface(size):
    return pygame.Surface((size[0], size[1]))

def get_image_spritesheet(spritesheet, spritesize, i):
    rect = pygame.Rect(i * spritesize[0], 0, spritesize[0], spritesize[1])
    image = pygame.Surface(rect.size)
    image.blit(spritesheet, (0,0), rect)
    a = image.get_at((0,0))
    image.set_colorkey(a)
    return image
