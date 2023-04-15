import pygame
import math
from entity.entity import Entity

class Projectile(Entity):
    
    def __init__(self, projInList, projIndex, spritePath: str, isDestructible: bool, x: int, y: int, speedVect: tuple, friendly=False):
        super().__init__(spritePath, isDestructible, x, y)
        self.projInList = projInList
        self.projIndex = projIndex
        self.speedVect = speedVect
        vect = (1,0)
        self.speed = 5
        self.angle = math.acos((speedVect[0]*vect[0] + speedVect[1]*vect[1]) / math.sqrt(speedVect[0]**2 + speedVect[1]**2) * math.sqrt(vect[0]**2 + vect[1]**2)) * 100
        print(self.angle)
        self.friendly = friendly
        self.setImgAngle()

    def update(self):
        self.rect.x  += self.speedVect[0]*self.speed
        self.rect.y  += self.speedVect[1]*self.speed
        if self.rect.x >= 800:
            self.projInList[self.projIndex] = None

    def setImgAngle(self):
        self.image = pygame.transform.rotozoom(self.imgBase, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)