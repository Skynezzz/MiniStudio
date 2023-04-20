import pygame
from random import randint
from entity.player import Player
from entity.entity import Entity
from entity.enemy import SuicidePigeon, StrafingDrone, DrunkPigeon
from game.gameLogic.movement import move
from settings import Setting

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
        self.projectiles = [None for i in range(50)]
        self.enemies = [None for i in range(10)]
        self.player = Player(self.projectiles, 50, 'img/oiseau.jpg', True)

        # initialisation des variables de cooldown
        self.enemySpawnCooldown = pygame.time.get_ticks()

        # initialisation des paramettres
        self.settings = Setting()

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

        # déplacement du joueur si il est vivant
        if not self.player.isDead():
            move(self.settings, self.screen, self.player)
        
        # ajout d'ennemis
        if pygame.time.get_ticks() > self.enemySpawnCooldown:
            for i in range(len(self.enemies)):
                if not self.enemies[i]:
                    self.enemies[i] = DrunkPigeon(10)
                    # self.enemies[i] = StrafingDrone(10, self.screenSize[0], randint(100, 500), self.projectiles)
                    # reset du cooldown de spawn
                    self.enemySpawnCooldown = pygame.time.get_ticks() + 16 * 60 * 2
                    break

        # update de la position des projectiles
        for i in range(len(self.projectiles)):
            if self.projectiles[i]:
                self.projectiles[i].update()
                # si la balle touche un ennemi
                if self.projectiles[i].friendly:
                    for j in range(len(self.enemies)):
                        if self.enemies[j] and self.projectiles[i] and self.enemies[j].rectOverlap(self.projectiles[i]):
                            self.enemies[j].takeDamage(10)
                            # suppression lorsqu'ils entrent en colision avec un ennemi
                            self.projectiles[i] = None
                elif self.player.rectOverlap(self.projectiles[i]):
                    self.player.takeDamage(10)
                    self.projectiles[i] = None

                                
                else:
                    if self.projectiles[i] and self.player.rectOverlap(self.projectiles[i]):
                            self.player.takeDamage(10)
                            self.projectiles[i] = None

                # si la balle sors de l'écran
                if self.projectiles[i] and not self.projectiles[i].rectOverlap(self.screenEntity):
                    self.projectiles[i] = None
                    pass
                
        # update de la position des ennemis et suppression de ces dernier
        for i in range(len(self.enemies)):
            if self.enemies[i]:
                self.enemies[i].update()
                if self.enemies[i].rectOverlap(self.player):
                    self.enemies[i].takeDamage(10)
                    self.player.takeDamage(10)
                if self.enemies[i].isDead() or not self.enemies[i].rectOverlap(self.screenEntity):
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

        # Affichage des ennemis
        for en in self.enemies:
            if en:
                en.draw(self.screen)

        for i in range(len(self.projectiles)):
            if self.projectiles[i]:
                cur = self.projectiles[i]
                self.screen.blit(cur.image, (cur.rect.x, cur.rect.y, cur.rect.width, cur.rect.height))

        # Mise à jour de l'affichage
        pygame.display.flip()

Game()