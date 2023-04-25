import pygame, math
from entity.entity import Entity
from entity.projectile import Projectile

class Enemy(Entity):

    def __init__(self, life: int, x: int, y: int, w: int, h: int, spritePath: str):
        super().__init__(True, x, y, w, h, spritePath=spritePath)
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
        super().__init__(life, x, y, 50, 50, spritePath="img/drone_little.png")
        self.speedVect = (-1, 0)
        self.speed = 4
    

class StrafingDrone(Enemy):

    def __init__(self, life: int, x: int, y: int, projectile):
        super().__init__(life, x, y, 100, 100, spritePath="img/drone_big.png")
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
                    self.all_projectiles[projIndex] = Projectile("img/projectiles_sheet.png", False, offSetX, offSetY, 26, 9, vect, 1, 4, True)
                    break

class DrunkPigeon(Enemy):
    def __init__(self, life, reverse=False):
        super().__init__(life, 1920, 250, 50, 50, spritePath="img/drone_little.png")
        # self.pathXAxis = 700
        self.speedVect = (-1, 0)
        self.reversed = reverse
        self.speed = 3
    
    def update(self):
        # self.pathXAxis += self.speedVect[0] * self.speed
        self.rect.x += self.speedVect[0] * self.speed
        if self.reversed:
            self.rect.y = 275 + math.cos(self.rect.x/80) * 250
        else:
            self.rect.y = 275 + math.sin(self.rect.x/80) * 250

class Scientist(Enemy):
    def __init__(self, life: int, spritePath: str):
        super().__init__(life, 1920, 1000, w=spritesWidth*self.scale, h=spritesHeigh*self.scale, spritePath="img/scient-cat-Sheet.png")
        self.speedVect = (-1, 0)
        self.speed = 3
        # Création de variables pour animation
        self.scale = 5
        spritesWidth, spritesHeigh = 80, 48
        self.imgWidth = self.imgHeigh = 16
        self.spriteY = 16
        self.spriteSheet = pygame.transform.scale(pygame.image.load(spritePath).convert_alpha(), (spritesWidth * self.scale, spritesHeigh * self.scale))
        self.frame = 0
        self.actualFrame = pygame.Rect(self.frame * self.imgWidth * self.scale, self.spriteY * self.scale, self.imgWidth * self.scale, self.imgHeigh * self.scale)
        self.timeNextFrame = 150

    def update(self, dt):
        # Algo animation
        self.timeNextFrame -= dt
        if self.timeNextFrame < 0:
            self.timeNextFrame += 150
            self.frame = (self.frame + 1) % (self.def_frame-1)
            self.actualFrame = pygame.Rect(self.frame * self.imgWidth * self.scale, self.spriteY * self.scale, self.imgWidth * self.scale, self.imgHeigh * self.scale)

    def draw(self, screen):
        screen.blit(self.spriteSheet, dest=(self.rect.x, self.rect.y), area=self.actualFrame)


class Boss(Enemy):

    def __init__(self, life, spritePath):
        super().__init__(life, spritePath)