import pygame
from entity.player import Player
from entity.entity import Entity
from game.gameLogic.movement import move

class Game:
    
    def __init__(self):
        # Initialise Pygame
        pygame.init()

        # Définir la taille de la fenêtre
        self.screenSize = (800, 600)
        self.screen = pygame.display.set_mode(self.screenSize)
        self.screenEntity = Entity(False, 0, 0, self.screenSize[0], self.screenSize[1])

        #Définis une clock pour limiter des actions
        self.clock = pygame.time.Clock()

        # Définir le titre de la fenêtre
        pygame.display.set_caption("Le Blaze")

        # intialisation de la variable en la remplissant de None
        self.projectiles = [None for i in range(30)]
        self.enemies = [None for i in range(30)]

        self.player = Player(self.projectiles, 50, 'img/oiseau.jpg', True)

        # Boucle principale
        done = False
        while not(done):
            self.timeStart = pygame.time.get_ticks()
            self.frames = self.timeStart//16
            # Gestion des événements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            self.update()
            self.draw()
        
        # Quitter Pygame
        pygame.quit()
    
    def update(self):

        # Logique du jeu
        move(self.screen, self.player)

        # update de la position des projectiles et suppression de ces dernier lorsqu'il sortent de l'écran ou qu'ils entrent en colision avec un ennemi
        for i in range(len(self.projectiles)):
            if self.projectiles[i]:
                self.projectiles[i].update()
                # si la balle touche un ennemi
                if self.projectiles[i].friendly:
                    for j in range(len(self.enemies)):
                        if self.enemies[j] and self.enemies[j].rectOverlap(self.projectiles[i]):
                                self.enemies[j].takeDamage(10)
                                self.projectiles[i] = None
                else:
                    if self.player.rectOverlap(self.projectiles[i]):
                            self.player.takeDamage(10)
                            self.projectiles[i] = None
                # si la balle sors de l'écran
                if not self.projectiles[i].rectOverlap(self.screenEntity):
                    self.projectiles[i] = None
                    pass
                

        # update de la position des ennemis et suppression de ces dernier
        for i in range(len(self.enemies)):
            if self.enemies[i]:
                self.enemies[i].update()
                if self.enemies[i].rectOverlap(self.player):
                    self.enemies[i].takeDamage(10)
                    self.player.takeDamage(10)
                if self.enemies[i].isDead():
                    self.enemies[i] = None

        # timer
        timeEnd = pygame.time.get_ticks()
        if self.timeStart + 7 > timeEnd:
            pygame.time.delay(timeEnd - self.timeStart + 7)

        self.clock.tick(60)
    
    def draw(self):
        # Affichage du jeu
        self.screen.fill((0, 0, 0))

        # Affichage du joueur
        self.screen.blit(self.player.image, self.player.rect)

        for i in range(len(self.projectiles)):
            if self.projectiles[i]:
                cur = self.projectiles[i]
                self.screen.blit(cur.image, (cur.rect.x, cur.rect.y, cur.rect.width, cur.rect.height))

        # Mise à jour de l'affichage
        pygame.display.flip()

Game()