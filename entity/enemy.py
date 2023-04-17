import pygame, math
from entity.entity import Entity
from entity.projectile import Projectile

class Enemy(Entity):

    def __init__(self, life: int, x: int, y: int, spritePath: str):
        super().__init__(True, x, y, spritePath=spritePath)
        self.life = life
    
    def takeDamage(self, damageNumber):
        self.life -= damageNumber

    def isDead(self):
        return self.life <= 0
    
    def update(self):
        self.rect.x += self.speedVect[0] * self.speed
        self.rect.y += self.speedVect[1] * self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class SuicidePigeon(Enemy):

    def __init__(self, life: int, x: int, y: int):
        super().__init__(life, x, y, spritePath="img/oiseau.jpg")
        self.speedVect = (-1, 0)
        self.speed = 4
    

class StrafingPigeon(Enemy):

    def __init__(self, life: int, x: int, y: int, projectile):
        super().__init__(life, x, y, spritePath="img/oiseau.jpg")
        self.speedVect = (-1, 0)
        self.threshold = False
        self.speed = 2
        self.angle = 0
        self.all_projectiles = projectile
        self.fireCooldown = pygame.time.get_ticks()
    
    def resetFireCooldown(self):
        self.fireCooldown = pygame.time.get_ticks()+10*200


    def update(self):
        self.rect.x += self.speedVect[0] * self.speed
        self.rect.y += self.speedVect[1] * self.speed
        # avance puis monte et descend
        if self.rect.x <= 700 and not self.threshold:
            self.speedVect = (0, -1)
            self.threshold = True
        elif self.rect.y <= 50:
            self.speedVect = (0, 1)
        elif self.rect.y >= 550:
            self.speedVect = (0, -1)
        # fonction de tir des ennemies
        if self.threshold and pygame.time.get_ticks() > self.fireCooldown:
            offSetX = self.rect.x - 60
            offSetY = self.rect.y
            vect = (-1, 0)
            self.resetFireCooldown()

            for projIndex in range(len(self.all_projectiles)):
                if not self.all_projectiles[projIndex]:
                    self.all_projectiles[projIndex] = Projectile("img/bullet.png", False, offSetX, offSetY, vect, True)
                    break


class Boss(Enemy):

    def __init__(self, life, spritePath):
        super().__init__(life, spritePath)