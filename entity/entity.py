import pygame

class Entity():

    def __init__(self, destructible: bool, x=0, y=0, w=0, h=0, spritePath=None):
        """spritePath est une string optionelle à n'utiliser que pour les entité visible"""
        self.destructible = destructible
        if spritePath:
            self.imgBase = pygame.transform.scale(pygame.image.load(spritePath), (w, h))
            self.image = self.imgBase
            self.rect = self.image.get_rect()
            if x != 0 and y != 0:
                self.rect.update(x, y, self.rect.width, self.rect.height)
        else:
            self.rect = pygame.Rect(x, y, w, h)

    def rectOverlap(self, otherEntity):
        """Renvoie True si l'entité entre en colision avec un autre"""
        return self.rect.x < otherEntity.rect.x + otherEntity.rect.width and self.rect.x + self.rect.width > otherEntity.rect.x and self.rect.y < otherEntity.rect.y + otherEntity.rect.height and self.rect.y + self.rect.height > otherEntity.rect.y

class Button(Entity):

    def __init__(self, x: int, y: int, w: int, h: int):
        super().__init__(False, x, y, w, h, "img/ui.png")
        self.hover = False
        self.image = pygame.image.load("img/drone.png").convert_alpha()
        self.background = pygame.Surface((self.rect.width,self.rect.height)).convert_alpha()
        self.background.blit(self.image, (0,0), (160, 320, 730, 140))
        self.textPlay = self.background
        self.textPlay.blit(self.image, (180,20), (1620, 340, 360, 100))
        self.textPlayHover = self.background
        self.textPlayHover.blit(self.image, (180,20), (1060, 340, 360, 100))
    
    def isPressed(self):
        if pygame.mouse.get_pressed(num_buttons=3)[0]:
            mouseX, mouseY = pygame.mouse.get_pos()
            return self.rectOverlap(Entity(False, mouseX, mouseY))

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        # mouseX, mouseY = pygame.mouse.get_pos()
        # if self.rectOverlap(Entity(False, mouseX, mouseY)):
        #     screen.blit(self.textPlayHover, self.rect)
        # else:
        #     screen.blit(self.textPlay, self.rect)