import pygame
from entity.player import Player
from game.gameLogic.movement import move

# Initialise Pygame
pygame.init()

# Définir la taille de la fenêtre
size = (800, 600)
screen = pygame.display.set_mode(size)

#Définis une clock pour limiter des actions
clock = pygame.time.Clock()

# Définir le titre de la fenêtre
pygame.display.set_caption("Le Blaze")

# intialisation de la variable en la remplissant de None
projectiles = [None for i in range(30)]

player = Player(projectiles, 50, 'img/oiseau.jpg', True)

# Boucle principale
done = False
while not(done):
    timeStart = pygame.time.get_ticks()
    frames = timeStart//16
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    # Logique du jeu
    move(screen, player)

    for i in range(len(projectiles)):
        if projectiles[i]:
            projectiles[i].update()

    # Affichage du jeu
    screen.fill((0, 0, 0))
    screen.blit(player.image, player.rect)

    for i in range(len(projectiles)):
        if projectiles[i]:
            cur = projectiles[i]
            screen.blit(cur.image, (cur.rect.x, cur.rect.y, cur.rect.width, cur.rect.height))

    # Mise à jour de l'affichage
    pygame.display.flip()

    # timer
    timeEnd = pygame.time.get_ticks()
    if timeStart + 7 > timeEnd:
        pygame.time.delay(timeEnd - timeStart + 7)

    
    print(frames)
    clock.tick(60)

# Quitter Pygame
pygame.quit()