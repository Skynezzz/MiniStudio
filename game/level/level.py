import pygame

class Level():
    
    def __init__(self, background: str, num=0, enemy=None, map=None):
        self.background = background
        self.num = num
        self. enemy = enemy
        self.map = map