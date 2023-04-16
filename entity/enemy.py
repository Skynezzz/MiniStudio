import pygame
from entity.entity import Entity

class Enemy(Entity):

    def __init__(self, life: int, spritePath: str):
        super().__init__(spritePath, True)
        self.life = life
    
    def takeDamage(self, damageNumber):
        self.life -= damageNumber
    

class Boss(Enemy):

    def __init__(self, life, spritePath):
        super().__init__(life, spritePath)