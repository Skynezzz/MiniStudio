import pygame
from entity.entity import Entity
from entity.projectile import Projectile

class Player(Entity):

    def __init__(self, projectile, life: int, src: str, destruct: bool):
        super().__init__(src, destruct)
        self.life = life
        self.speed = 4
        self.angle = 0
        self.rect = self.image.get_rect()
        self.all_projectiles = projectile
        self.fireCooldown = pygame.time.get_ticks()

    def resetFireCooldown(self):
        self.fireCooldown = pygame.time.get_ticks()+15*16

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
        if pygame.time.get_ticks() > self.fireCooldown:
            self.resetFireCooldown()
            offSetX=self.rect.x+self.rect.width+10
            offSetY=self.rect.y+self.rect.height/2

            for projIndex in range(len(self.all_projectiles)):
                if not self.all_projectiles[projIndex]:
                    self.all_projectiles[projIndex] = Projectile(self.all_projectiles, projIndex,"img/bullet.png", False, offSetX, offSetY)
                    break