import pygame, math

class Level():
    
    def __init__(self, background, num=0, enemy=None, map=None):
        self.background = background
        self.num = num
        self. enemy = enemy
        self.map = map

class Demo(Level):
    
    def __init__(self, background: str, num, enemy, map):
        super().__init__(background, num, enemy, map)
        self.background = pygame.transform.scale(pygame.image.load(self.background).convert(), (2150, 600))
        self.screenWidth = 600
        self.scroll = 0
        self.speed = 4
        self.tiles = math.ceil(self.screenWidth / self.background.get_width()) + 1
    
    def draw(self, screen):
        i = 0
        while(i < self.tiles):
            screen.blit(self.background, (self.background.get_width()*i + self.scroll, 0))
            i += 1
        # FRAME FOR SCROLLING
        self.scroll -= self.speed
    
        # RESET THE SCROLL FRAME
        if abs(self.scroll) > self.background.get_width():
            self.scroll = 0