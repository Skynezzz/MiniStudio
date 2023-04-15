import pygame
from entity.entity import Entity

class Projectile(Entity):
    
    def __init__(self, projInList, projIndex, spritePath: str, isDestructible: bool, x: int, y: int, friendly=False):
        super().__init__(spritePath, isDestructible, x, y)
        self.projInList = projInList
        self.projIndex = projIndex
        self.speed = 5
        self.angle = 0
        self.friendly = friendly

    def update(self):
        self.rect.x  += self.speed
        if self.rect.x >= 800:
            self.projInList[self.projIndex] = None

    def setImgAngle(self):
        self.img = pygame.transform.rotozoom(self.imgBase, self.angle, 1)
        self.rect = self.img.get_rect(center=self.rect.center)