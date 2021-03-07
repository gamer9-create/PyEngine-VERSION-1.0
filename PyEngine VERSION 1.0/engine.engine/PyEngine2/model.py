import pygame


pygame.init()

class Model(pygame.sprite.Sprite):
    def __init__(self,x,y,image,screen):
        super().__init__()
        self.x = x
        self.y = y
        self.image = image
        self.rect = self.image.get_rect()
        self.size = self.image.get_size()
        self.screen = screen
        self.group = None
        self.render_offset = [0,0]
        #self.gravity = GravityHandler(self.x, self.y, None, self.rect)
    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y
        #if self.group:
            #self.gravity.groups = self.group
        #self.gravity.x = self.x
        #self.gravity.y = self.y
        #self.gravity.rect.x = self.x
        #self.gravity.rect.y = self.y
        #self.gravity.rect = self.rect
        self.image = pygame.transform.scale(self.image, (self.size[0], self.size[1]))
        #self.gravity.handleGravity()
        #if self.gravity.falling:
            #self.y = self.y + 20
        self.screen.blit(self.image, (self.x + self.render_offset[0], self.y + self.render_offset[1]))

