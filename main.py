import pygame
from entity.player import Player

# Initialise Pygame
pygame.init()

# Définir la taille de la fenêtre
size = (800, 600)
screen = pygame.display.set_mode(size)

# Définir le titre de la fenêtre
pygame.display.set_caption("Le Blaze")
player = Player()

# Boucle principale
done = False
while not(done):
    timeStart = pygame.time.get_ticks()
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Logique du jeu
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

    # Affichage du jeu
    screen.fill((0, 0, 0))
    screen.blit(player.img, player.rect)

    # Mise à jour de l'affichage
    pygame.display.flip()
    

    # timer
    timeEnd = pygame.time.get_ticks()
    if timeStart + 7 > timeEnd:
        pygame.time.delay(timeEnd - timeStart + 7)

# Quitter Pygame
pygame.quit()