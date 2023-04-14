import pygame
from entity.entity import Entity

class Projectile(Entity):
    
    def __init__(self, spritePath: str, isDestructible: bool, x: int, y: int):
        super().__init__(spritePath, isDestructible)
        self.speed = 5
        self.angle = 0

    def update(self):
        self.rect.x  += self.speed
        

    def setImgAngle(self):
        self.img = pygame.transform.rotozoom(self.imgBase, self.angle, 1)
        self.rect = self.img.get_rect(center=self.rect.center)