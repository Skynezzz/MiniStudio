import pygame, math
from entity.entity import Entity

class Projectile(Entity):
    
    def __init__(self, spritePath: str, isDestructible: bool, x: int, y: int, w: int, h: int, speedVect: tuple, def_frame: int, spriteY: int, friendly=False):
        super().__init__(isDestructible, x, y, w, h, spritePath=spritePath)
        self.speedVect = speedVect
        self.def_frame = def_frame
        self.spriteY = spriteY
        self.friendly = friendly
        vect = (1,0)
        speedVect = (speedVect[0],-speedVect[1])
        self.temp = speedVect
        self.speed = 6
        # Création de variables pour animation
        self.scale = 5
        spritesWidth, spritesHeigh = 78, 128
        self.imgWidth, self.imgHeigh = w, h
        self.spriteSheet = pygame.transform.scale(pygame.image.load(spritePath).convert_alpha(), (spritesWidth * self.scale, spritesHeigh * self.scale))
        self.frame = 0
        self.curentFrame = pygame.Rect(self.frame * self.imgWidth * self.scale, self.spriteY * self.scale, self.imgWidth * self.scale, self.imgHeigh * self.scale)
        self.timeNextFrame = 150
        # Variables de rotation
        self.angle = math.degrees(math.acos((speedVect[0]*vect[0] + speedVect[1]*vect[1]) / math.sqrt(speedVect[0]**2 + speedVect[1]**2) * math.sqrt(vect[0]**2 + vect[1]**2)))
        self.setImgAngle()

    def update(self, dt):
        self.rect.x  += self.speedVect[0]*self.speed
        self.rect.y  += self.speedVect[1]*self.speed
        # Algo animation
        self.timeNextFrame -= dt
        if self.timeNextFrame < 0:
            self.timeNextFrame += 150
            self.frame = (self.frame + 1) % (self.def_frame-1)
            if self.friendly:
                self.curentFrame = pygame.Rect(self.frame * self.imgWidth * self.scale, self.spriteY * self.scale, self.imgWidth * self.scale, self.imgHeigh * self.scale)
            else:
                self.curentFrame = pygame.Rect(self.frame * self.imgWidth * self.scale, self.spriteY * self.scale, self.imgWidth * self.scale, self.imgHeigh * self.scale)

    def draw(self, screen):
        screen.blit(self.spriteSheet, dest=(self.rect.x, self.rect.y), area=self.curentFrame)

    def setImgAngle(self):
        if self.temp[1] > 0:
            self.image = pygame.transform.rotozoom(self.imgBase, self.angle, 1)
        else:
            self.image = pygame.transform.rotozoom(self.imgBase, 360-self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)