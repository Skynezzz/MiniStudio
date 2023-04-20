import pygame, math
from entity.entity import Entity
from entity.projectile import Projectile

class Player(Entity):

    def __init__(self, projectile, life: int, src: str, destruct: bool):
        super().__init__(destruct, spritePath=src)
        self.life = life
        self.speed = 4
        self.angle = 0
        self.rect = self.image.get_rect()
        self.all_projectiles = projectile
        self.fireCooldown = pygame.time.get_ticks()
        self.abilityCooldown = pygame.time.get_ticks()

    def resetFireCooldown(self):
        self.fireCooldown = pygame.time.get_ticks()+10*16
    
    def resetAbilityCooldown(self):
        self.abilityCooldown = pygame.time.get_ticks()+1800*16

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
    
    def takeDamage(self, damageNumber):
        self.life -= damageNumber

    def setImgAngle(self):
        self.img = pygame.transform.rotozoom(self.imgBase, self.angle, 1)
        self.rect = self.img.get_rect(center=self.rect.center)
        
    def isDead(self):
        return self.life <= 0
    
    def launchProjectile(self):
        if pygame.time.get_ticks() > self.fireCooldown:
            offSetX = self.rect.x + self.rect.width + 10
            offSetY = self.rect.y
            mouseX, mouseY = pygame.mouse.get_pos()
            mouseY -= 25
            vectX, vectY = mouseX - offSetX, mouseY - offSetY
            norm = math.sqrt( vectX**2 + vectY**2 )
            vect = (vectX/norm, vectY/norm)
            self.resetFireCooldown()

            for projIndex in range(len(self.all_projectiles)):
                if not self.all_projectiles[projIndex]:
                    self.all_projectiles[projIndex] = Projectile("img/bullet.png", False, offSetX, offSetY, vect, True)
                    break
    
    def juanAbility(self):
        if pygame.time.get_ticks() > self.abilityCooldown:
            offSetX = self.rect.x + self.rect.width + 10
            offSetY = self.rect.y
            spawnX = 0-25
            spawnY = 300-25
            upX = spawnX - 20
            upY = spawnY - 70
            downX = spawnX - 20
            downY = spawnY + 70
            vect = (1, 0)
            print("Millieu :", spawnX, ",", spawnY, "\n", "Haut :", upX, ",", upY, "\n", "Bas :", downX, ",", downY)
            self.resetAbilityCooldown()

            for projIndex in range(len(self.all_projectiles)):
                if not self.all_projectiles[projIndex]:
                    self.all_projectiles[projIndex] = Projectile("img/[Juan_Carlos_Brito]-Colombe.jpg", False, spawnX, spawnY, vect, True)
                    self.all_projectiles[projIndex + 1] = Projectile("img/[Juan_Carlos_Brito]-Colombe.jpg", False, upX, upY, vect, True)
                    self.all_projectiles[projIndex + 2] = Projectile("img/[Juan_Carlos_Brito]-Colombe.jpg", False, downX, downY, vect, True)
                    break