import pygame
from entity.player import Player
from entity.entity import Entity
from game.gameLogic.movement import move

# Initialise Pygame
pygame.init()

# Définir la taille de la fenêtre
size = (800, 600)
screen = pygame.display.set_mode(size)
screenEntity = Entity(False, 0, 0, size[0], size[1])

#Définis une clock pour limiter des actions
clock = pygame.time.Clock()

# Définir le titre de la fenêtre
pygame.display.set_caption("Le Blaze")

# intialisation de la variable en la remplissant de None
projectiles = [None for i in range(30)]
enemies = [None for i in range(30)]

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

    # update de la position des projectiles et suppression de ces dernier lorsqu'il sortent de l'écran ou qu'ils entrent en colision avec un ennemi
    for i in range(len(projectiles)):
        if projectiles[i]:
            projectiles[i].update()
            # si la balle touche un ennemi
            if projectiles[i].friendly:
                for j in range(len(enemies)):
                    if enemies[j] and enemies[j].rectOverlap(projectiles[i]):
                            enemies[j].takeDamage(10)
                            projectiles[i] = None
            else:
                if player.rectOverlap(projectiles[i]):
                        player.takeDamage(10)
                        projectiles[i] = None
            # si la balle sors de l'écran
            if not projectiles[i].rectOverlap(screenEntity):
                projectiles[i] = None
                pass
            

    # update de la position des ennemis et suppression de ces dernier
    for i in range(len(enemies)):
        if enemies[i]:
            enemies[i].update()
            if enemies[i].rectOverlap(player):
                enemies[i] = None
                player.takeDamage(10)

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

    clock.tick(60)

# Quitter Pygame
pygame.quit()