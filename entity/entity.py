import pygame

class Entity:

    def __init__(self, src: str, destruct: bool):
        self.destructible = destruct
        self.img = pygame.transform.scale(pygame.image.load(src), (50, 50))
        self.rect = self.img.get_rect()

    def rectOverlap(self, a: Entity, b: Entity):
        return x1 < x2 + w2 and x1 + w1 > x2 and y1 < y2 + h2 and y1 + h1 > y2