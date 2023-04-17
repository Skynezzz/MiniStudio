import pygame
from entity.entity import Entity

class Enemy(Entity):

    def __init__(self, life: int, spritePath: str):
        super().__init__(spritePath, True)
        self.life = life
        self.speedVect = (-1, 0)
        self.speed = 2
    
    def takeDamage(self, damageNumber):
        self.life -= damageNumber

    def isDead(self):
        return self.life <= 0
    
    def update(self):
        self.rect.x += self.speedVect * self.speed
    

class Boss(Enemy):

    def __init__(self, life, spritePath):
        super().__init__(life, spritePath)