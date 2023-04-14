import pygame
from entity import Entity

class Enemy(Entity):

    def __init__(self, life: int, src: str, destruct: bool):
        super().__init__(src, destruct)
        self.life = life