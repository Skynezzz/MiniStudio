import pygame

class Entity:

    def __init__(self, src: str, destruct: bool):
        self.destructible = destruct
        self.imgBase = pygame.transform.scale(pygame.image.load(src), (50, 50))
        self.img = self.imgBase
        self.rect = self.img.get_rect()

    def rectOverlap(self, a: Entity, b: Entity):
        return a.rect.x < b.rect.x + b.rect.width and a.rect.x + a.rect.width > b.rect.x and a.rect.y < b.rect.y + b.rect.height and a.rect.y + a.rect.height > b.rect.y