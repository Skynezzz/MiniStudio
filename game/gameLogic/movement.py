import pygame
from entity.player import Player

def move(settings, screen, player):
    keyPressed = pygame.key.get_pressed()
    mousePressed = pygame.mouse.get_pressed(num_buttons=3)
    if keyPressed[int(settings.settings['left'])]:
        player.left()
    if keyPressed[int(settings.settings['right'])]:
        player.right(screen)
    if keyPressed[int(settings.settings['up'])]:
        player.up()
    if keyPressed[int(settings.settings['down'])]:
        player.down(screen)
    if keyPressed[int(settings.settings['dead'])]:
        player.takeDamage(10)
    if mousePressed == (1, 0, 0):
        player.launchProjectile()
    if mousePressed == (0, 0, 1):
        player.juanAbility()