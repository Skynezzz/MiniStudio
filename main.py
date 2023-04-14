import pygame
from entity.player import Player
from game.gameLogic.movement import move

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
    move(screen, player)

    # Affichage du jeu
    screen.fill((0, 0, 0))
    screen.blit(player.img, player.rect)
    player.all_projectiles.draw(screen)

    # Mise à jour de l'affichage
    pygame.display.flip()
    

    # timer
    timeEnd = pygame.time.get_ticks()
    if timeStart + 7 > timeEnd:
        pygame.time.delay(timeEnd - timeStart + 7)

# Quitter Pygame
pygame.quit()