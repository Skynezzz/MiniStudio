import pygame

class Entity():

    def __init__(self, src: str, destruct: bool, x=0, y=0):
        self.destructible = destruct
        self.imgBase = pygame.transform.scale(pygame.image.load(src), (50, 50))
        self.image = self.imgBase
        self.rect = self.image.get_rect()
        if x != 0 and y != 0:
            self.rect.update(x, y, self.rect.width, self.rect.height)

    def rectOverlap(self, a, b):
        return a.rect.x < b.rect.x + b.rect.width and a.rect.x + a.rect.width > b.rect.x and a.rect.y < b.rect.y + b.rect.height and a.rect.y + a.rect.height > b.rect.y