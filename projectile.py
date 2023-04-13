import pygame

class Projectile(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.speed = 5
        self.imgBase = pygame.transform.scale(pygame.image.load('img/bullet.png'), (50, 50))
        self.img = pygame.transform.scale(pygame.image.load('img/bullet.png'), (50, 50))
        self.react = self.img.get_rect() 