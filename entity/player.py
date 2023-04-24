import pygame, math
from entity.entity import Entity
from entity.projectile import Projectile

class Player(Entity):

    def __init__(self, x: int, y: int, w: int, h: int, projectile, life: int, destruct: bool):
        super().__init__(destruct, x, y, w, h, spritePath="img/sprite_character.png")
        self.life = life
        self.speed = 6
        self.angle = 0
        self.damage = False
        self.all_projectiles = projectile
        self.fireCooldown = pygame.time.get_ticks()
        self.abilityCooldown = pygame.time.get_ticks()
        
        # Création de variables pour animation
        self.charaWidth = self.charaHeigh = 100
        self.spriteSheet = pygame.transform.scale(pygame.image.load("img/sprite_character.png").convert_alpha(), (self.charaWidth*9, self.charaHeigh))
        self.frame = 0
        self.actualFrame = pygame.Rect(self.frame * self.charaWidth, 0, self.charaWidth, self.charaHeigh)
        self.timeNextFrame = 200
    
    def takeDamage(self, damageNumber):
        self.life -= damageNumber
        self.damage = True
    
    def draw(self, screen, dt):
        self.timeNextFrame -= dt

        if self.timeNextFrame < 0:
            self.timeNextFrame += 200
            if self.damage:
                self.frame = 8
                self.damage = False
            else:
                if self.frame >= 8:
                    self.frame = 0
                else:
                    self.frame = (self.frame + 1) % 7
            self.actualFrame = pygame.Rect(self.frame * self.charaWidth, 0, self.charaWidth, self.charaHeigh)

        screen.blit(self.spriteSheet, dest=(self.rect.x, self.rect.y), area=self.actualFrame)

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

    def setImgAngle(self):
        self.img = pygame.transform.rotozoom(self.imgBase, self.angle, 1)
        self.rect = self.img.get_rect(center=self.rect.center)
        
    def isDead(self):
        return self.life <= 0
    
    def launchProjectile(self):
        if pygame.time.get_ticks() > self.fireCooldown:
            offSetX = self.rect.x + self.rect.width + 10
            offSetY = self.rect.y + self.rect.height/2
            mouseX, mouseY = pygame.mouse.get_pos()
            mouseY -= 25
            vectX, vectY = mouseX - offSetX, mouseY - offSetY
            norm = math.sqrt( vectX**2 + vectY**2 )
            vect = (vectX/norm, vectY/norm)
            self.resetFireCooldown()

            for projIndex in range(len(self.all_projectiles)):
                if not self.all_projectiles[projIndex]:
                    self.all_projectiles[projIndex] = Projectile("img/projectiles_sprite.png", False, offSetX, offSetY, 90, 30, vect, 3, True)
                    break
    
    def juanAbility(self):
        if pygame.time.get_ticks() > self.abilityCooldown:
            spawnX = 0-25
            spawnY = 300-25
            upX = spawnX - 20
            upY = spawnY - 70
            downX = spawnX - 20
            downY = spawnY + 70
            vect = (1, 0)
            self.resetAbilityCooldown()

            for projIndex in range(len(self.all_projectiles)):
                if not self.all_projectiles[projIndex]:
                    self.all_projectiles[projIndex] = Projectile("img/[Juan_Carlos_Brito]-Colombe.jpg", False, spawnX, spawnY, 50, 50, vect, True)
                    self.all_projectiles[projIndex + 1] = Projectile("img/[Juan_Carlos_Brito]-Colombe.jpg", False, upX, upY, 50, 50, vect, True)
                    self.all_projectiles[projIndex + 2] = Projectile("img/[Juan_Carlos_Brito]-Colombe.jpg", False, downX, downY, 50, 50, vect, True)
                    break