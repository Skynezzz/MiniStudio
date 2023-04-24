import pygame, math
from entity.entity import Entity

class Projectile(Entity):
    
    def __init__(self, spritePath: str, isDestructible: bool, x: int, y: int, w: int, h: int, speedVect: tuple, def_frame: int, friendly=False):
        super().__init__(isDestructible, x, y, w, h, spritePath=spritePath)
        self.speedVect = speedVect
        self.def_frame = def_frame
        self.friendly = friendly
        vect = (1,0)
        speedVect = (speedVect[0],-speedVect[1])
        self.temp = speedVect
        self.speed = 5
        # Création de variables pour animation
        scale = 2
        imgWidth = 78
        imgHeigh = 128
        self.spriteSheet = pygame.transform.scale(pygame.image.load(spritePath).convert_alpha(), (imgWidth*scale, imgHeigh*scale))
        self.frame = 0
        #self.frame1 = pygame.transform.scale(self.spriteSheet, ())
        self.actualFrame = pygame.Rect(0*scale, 4*scale, 26*scale, 9*scale)
        self.timeNextFrame = 200
        self.angle = math.degrees(math.acos((speedVect[0]*vect[0] + speedVect[1]*vect[1]) / math.sqrt(speedVect[0]**2 + speedVect[1]**2) * math.sqrt(vect[0]**2 + vect[1]**2)))
        self.setImgAngle()

    def update(self, dt):
        self.rect.x  += self.speedVect[0]*self.speed
        self.rect.y  += self.speedVect[1]*self.speed
        # Algo animation
        self.timeNextFrame -= dt
        if self.timeNextFrame < 0:
            self.timeNextFrame += 200
            # self.frame = (self.frame + 1) % (self.def_frame-1)
            # self.actualFrame = pygame.Rect(0, 4, 26, 9)

    def draw(self, screen):
        screen.blit(self.spriteSheet, dest=(self.rect.x, self.rect.y), area=self.actualFrame)

    def setImgAngle(self):
        if self.temp[1] > 0:
            self.image = pygame.transform.rotozoom(self.imgBase, self.angle, 1)
        else:
            self.image = pygame.transform.rotozoom(self.imgBase, 360-self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)