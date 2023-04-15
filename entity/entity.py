import pygame

class Entity():

    def __init__(self, spritePath: str, destructible: bool, x=0, y=0):
        self.destructible = destructible
        self.imgBase = pygame.transform.scale(pygame.image.load(spritePath), (50, 50))
        self.image = self.imgBase
        self.rect = self.image.get_rect()
        if x != 0 and y != 0:
            self.rect.update(x, y, self.rect.width, self.rect.height)

    def rectOverlap(self, otherEntity):
        """Renvoie True si l'entité entre en colision avec un autre"""
        return self.rect.x < otherEntity.rect.x + otherEntity.rect.width and self.rect.x + self.rect.width > otherEntity.rect.x and self.rect.y < otherEntity.rect.y + otherEntity.rect.height and self.rect.y + self.rect.height > otherEntity.rect.y