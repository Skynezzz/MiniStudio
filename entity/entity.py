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

    def __init__(self, x: int, y: int, type: str):
        super().__init__(False, x, y, 73*7.5, 14*7.5, "img/ui.png")
        self.type = type
        self.hover = False
        self.image = pygame.transform.scale(pygame.image.load("img/ui.png").convert_alpha(), (1920, 960))
        self.background = pygame.Surface((self.rect.width,self.rect.height)).convert_alpha()
    
    def isPressed(self):
        if pygame.mouse.get_pressed(num_buttons=3)[0]:
            mouseX, mouseY = pygame.mouse.get_pos()
            return self.rectOverlap(Entity(False, mouseX, mouseY))

    def draw(self, screen):
        scale = 7.5
        screen.blit(self.image, (self.rect.x, self.rect.y), (16*scale, 32*scale, 73*scale, 14*scale))
        mouseX, mouseY = pygame.mouse.get_pos()
        if self.rectOverlap(Entity(False, mouseX, mouseY)):
            if self.type == "start":
                screen.blit(self.image, (self.rect.x + 18*scale, self.rect.y + 2*scale), (162*scale, 34*scale, 36*scale, 10*scale))
            elif self.type == "option":
                screen.blit(self.image, (self.rect.x + 10*scale, self.rect.y + 2*scale), (23*scale, 66*scale, 56*scale, 10*scale))
            elif self.type == "quit":
                screen.blit(self.image, (self.rect.x + 20*scale, self.rect.y + 2*scale), (35*scale, 98*scale, 32*scale, 10*scale))
        else:
            if self.type == "start":
                screen.blit(self.image, (self.rect.x + 18*scale, self.rect.y + 2*scale), (106*scale, 34*scale, 36*scale, 10*scale))
            elif self.type == "option":
                screen.blit(self.image, (self.rect.x + 10*scale, self.rect.y + 2*scale), (23*scale, 82*scale, 56*scale, 10*scale))
            elif self.type == "quit":
                screen.blit(self.image, (self.rect.x + 20*scale, self.rect.y + 2*scale), (35*scale, 114*scale, 32*scale, 10*scale))