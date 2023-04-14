import pygame
from entity.player import Player

def move(screen, player):
    keyPressed = pygame.key.get_pressed()
    if keyPressed[pygame.K_q]:
        player.left()
    if keyPressed[pygame.K_d]:
        player.right(screen)
    if keyPressed[pygame.K_z]:
        player.up()
    if keyPressed[pygame.K_s]:
        player.down(screen)
    if keyPressed[pygame.K_e]:
        player.angle -= 1
        player.setImgAngle()
    if keyPressed[pygame.K_a]:
        player.angle += 1
        player.setImgAngle()
    if keyPressed[pygame.K_SPACE]:
        player.launchProjectile()