import pygame


pygame.init()


class tile(pygame.sprite.Sprite):
    def __init__(self, x, y, size, screen, image):
        super().__init__()
        self.x = x
        self.y = y
        self.size = size
        self.screen = screen
        self.image = image
        self.rect = self.image.get_rect()
        self.render_offset = [0, 0]
        self.group = None
        self.color = (0,0,0)
        #self.gravity = GravityHandler(self.x, self.y, self.group.remove(self), self.rect)


    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y
        #self.gravity.x = self.x
        #self.gravity.y = self.y
        #self.gravity.rect.x = self.x
        #self.gravity.rect.y = self.y
        #self.image = pygame.transform.scale(self.image, (self.size[0], self.size[1]))
        self.image.fill(self.color)
        #self.gravity.handleGravity()
        #if self.gravity.falling:
            #self.y = self.y + 20
        #print(self.gravity.falling)
        self.screen.blit(self.image, (self.x + self.render_offset[0], self.y + self.render_offset[1]))
