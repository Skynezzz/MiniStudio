import pygame
from entity.entity import Entity

class Enemy(Entity):

    def __init__(self, life: int, x: int, y: int, spritePath: str):
        super().__init__(True, x, y, spritePath=spritePath)
        self.life = life
        self.speedVect = (-1, 0)
        self.speed = 2
    
    def takeDamage(self, damageNumber):
        self.life -= damageNumber

    def isDead(self):
        return self.life <= 0
    
    def update(self):
        self.rect.x += self.speedVect[0] * self.speed
        self.rect.y += self.speedVect[1] * self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    

class Boss(Enemy):

    def __init__(self, life, spritePath):
        super().__init__(life, spritePath)