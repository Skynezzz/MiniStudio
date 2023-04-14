import pygame
from entity.entity import Entity

class Projectile(Entity):
    
    def __init__(self):
        super().__init__()
        self.speed = 5
        self.angle = 0
        self.imgBase = pygame.transform.scale(pygame.image.load('img/bullet.png'), (20, 20))
        self.img = pygame.transform.scale(pygame.image.load('img/bullet.png'), (20, 20))
        self.react = self.img.get_rect()

    def update(self):
        self.rect.x  += self.speed
        

    def setImgAngle(self):
        self.img = pygame.transform.rotozoom(self.imgBase, self.angle, 1)
        self.rect = self.img.get_rect(center=self.rect.center)