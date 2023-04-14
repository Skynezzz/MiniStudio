import pygame
from entity.entity import Entity
from entity.projectile import Projectile

class Player(Entity):

    def __init__(self, life: int, src: str, destruct: bool):
        super().__init__(src, destruct)
        self.speed = 4
        self.angle = 0
        self.rect = self.img.get_rect()
        self.all_projectiles = pygame.sprite.Group()

    def left(self):
        if self.rect.x - self.speed >= 0:
            self.rect.x -= self.speed

    def right(self, screen):
        if self.rect.x + self.speed <= screen.get_size()[0] - self.rect.width:
            self.rect.x  += self.speed

    def up(self):
        if self.rect.y - self.speed >= 0:
            self.rect.y -= self.speed

    def down(self, screen):
        if self.rect.y + self.speed <= screen.get_size()[1] - self.rect.height:
            self.rect.y += self.speed

    def setImgAngle(self):
        self.img = pygame.transform.rotozoom(self.imgBase, self.angle, 1)
        self.rect = self.img.get_rect(center=self.rect.center)
        
    def launchProjectile(self):
        self.all_projectiles.add(Projectile())