import pygame
from random import randint
from game.level.level import Level
from entity.player import Player
from entity.entity import Entity, Button
from entity.enemy import SuicidePigeon, StrafingDrone, DrunkPigeon
from game.gameLogic.movement import move
from settings import Setting

class Game:
    
    def __init__(self):
        # Initialise Pygame
        pygame.init()
        self.state = "menu"

        # Définir la taille de la fenêtre
        self.screenSize = (1920, 1080)
        self.screen = pygame.display.set_mode(self.screenSize, pygame.FULLSCREEN)
        self.screenEntity = Entity(False, 0, 0, self.screenSize[0], self.screenSize[1])

        #Définis une clock pour limiter les actions
        self.clock = pygame.time.Clock()

        # Définir le titre de la fenêtre
        pygame.display.set_caption("Feathers of Freedom")

        # initialisation des variables de cooldown
        self.enemySpawnCooldown = 0
        self.actionCooldown = 0
        # initialisation des paramettres
        self.settings = Setting()
        self.startButton = None
        self.level = None

        # chargement et réduction de l'image de background pour un affichage moins gourmand
        self.background = pygame.Surface(self.screenSize).convert_alpha()
        self.background.blit(pygame.image.load("img/bg1.png"),(0,0), (0,0,self.screenSize[0],self.screenSize[1]))
        
        self.backgroundGacha = pygame.Surface(self.screenSize).convert_alpha()
        self.backgroundGacha.blit(pygame.image.load("img/bg_gacha.png"),(0,0), (0,0,self.screenSize[0],self.screenSize[1]))
        
        #initialisation des boutons
        self.backButton = Button(self.screenSize[0]/2 - 365 + 100, self.screenSize[1]/2 + 260 , "menu")
        self.gachaButton = Button(self.screenSize[0]/2 - 365 + 100, self.screenSize[1]/2 + 80 , "gacha")
        self.replayButton = Button(self.screenSize[0]/2 - 365 + 100, self.screenSize[1]/2 - 100, "replay")
        self.game_overButton = Button(self.screenSize[0]/2 - 460 + 100, self.screenSize[1]/2 - 300, "game_over")
        self.startButton = Button(self.screenSize[0]/2 - 365 + 100, self.screenSize[1]/2 - 100, "start")
        self.optionButton = Button(self.screenSize[0]/2 - 365 + 100, self.screenSize[1]/2 + 80, "option")
        self.optionQuitButton = Button(self.screenSize[0]/2 - 365 + 100, self.screenSize[1]/2 + 80, "menu")
        self.quitButton = Button(self.screenSize[0]/2 - 365 + 100, self.screenSize[1]/2 + 260, "quit")
        self.openButton = Button(self.screenSize[0]/2 - 365 + 100, self.screenSize[1]/2 + 180, "open")
        self.back1Button = Button(self.screenSize[0] - 680 + 100, self.screenSize[1]/2 + 400 , "menu")

        
        # Boucle principale
        self.game = True
        while self.game:
            self.timeStart = pygame.time.get_ticks()
            self.frames = self.timeStart//16
            # Gestion des événements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game = False
            self.update()
            self.draw()
        
        # Quitter Pygame
        pygame.quit()
    
    def draw(self):
        self.screen.fill("aliceblue")
        if self.state == "game":
            self.drawLevel()
        elif self.state == "menu":
            self.drawMenu()
        elif self.state == "option":
            self.drawOption()
        elif self.state == "end":
            self.drawEnd()
        elif self.state == "gacha":
            self.drawReward()
        # Mise à jour de l'affichage
        pygame.display.flip()
    
    def update(self):
        self.dt = self.clock.tick(60)
        if self.state == "game":
            self.updateLevel()
        elif self.state == "menu":
            print("menu")
            self.updateMenu()
        elif self.state == "option":
            self.updateOption()
        elif self.state == "end" :
            self.updateEnd()
        elif self.state == "gacha":
            self.updateReward()
        # timer
        timeEnd = pygame.time.get_ticks()
        if self.timeStart + 7 > timeEnd:
            pygame.time.delay(timeEnd - self.timeStart + 7)
            print("cooldown")
                
    def updateMenu(self):
        
        if self.startButton.isPressed() and self.actionCooldown < pygame.time.get_ticks():
            self.actionCooldown = pygame.time.get_ticks() + 16 * 60 * 0.2
            self.initLevel()
            self.state = "game"
            self.level = Level(1)
            self.gameTimeStart = pygame.time.get_ticks()
        elif self.optionButton.isPressed() and self.actionCooldown < pygame.time.get_ticks():
            self.actionCooldown = pygame.time.get_ticks() + 16 * 60 * 0.2
            self.state = "option"
        elif self.quitButton.isPressed() and self.actionCooldown < pygame.time.get_ticks():
            self.actionCooldown = pygame.time.get_ticks() + 16 * 60 * 0.2
            self.game = False
    
    def drawMenu(self):
        self.screen.blit(self.background, (0,0,0,0))
        self.startButton.draw(self.screen)
        self.optionButton.draw(self.screen)
        self.quitButton.draw(self.screen)
        title = pygame.transform.scale(pygame.image.load("img/game-title.png"), (256*7, 64*7))
        titleW, titleH = 256*7, 64*7
        self.screen.blit(title, (self.screenSize[0]/2 - titleW/2, 0, 0, 0))
       
    def updateEnd(self):
        
        if self.backButton.isPressed() and self.actionCooldown < pygame.time.get_ticks():
            self.actionCooldown = pygame.time.get_ticks() + 16 * 60 * 0.2
            print("back")
            self.state = "menu"
        elif self.gachaButton.isPressed() and self.actionCooldown < pygame.time.get_ticks():
            self.actionCooldown = pygame.time.get_ticks() + 16 * 60 * 0.2
            print("gacha")
            self.state = "gacha"
        elif self.replayButton.isPressed() and self.actionCooldown < pygame.time.get_ticks():
            self.actionCooldown = pygame.time.get_ticks() + 16 * 60 * 0.2
            print("rejouer")
            self.initLevel()
            self.state = "game"
            self.level = Level(1)
            self.gameTimeStart = pygame.time.get_ticks()
            
    
    def drawEnd(self):
        self.drawLevel()
        self.game_overButton.draw(self.screen)
        self.replayButton.draw(self.screen)
        self.gachaButton.draw(self.screen)
        self.backButton.draw(self.screen)
    
    def updateReward (self):
        
        if self.openButton.isPressed() and self.actionCooldown < pygame.time.get_ticks():
            self.actionCooldown = pygame.time.get_ticks() + 16 * 60 * 0.2
            print("ouverture")
            self.state = "open"
        if self.back1Button.isPressed() and self.actionCooldown < pygame.time.get_ticks():
            self.actionCooldown = pygame.time.get_ticks() + 16 * 60 * 0.2
            print("back")
            self.state = "menu"
    
    def drawReward(self):
        image = pygame.transform.scale(pygame.image.load("img/bg_gacha.png"),(self.screenSize[0]*1,self.screenSize[1]*1))
        self.screen.blit(image, (0,0))
        self.openButton.draw(self.screen)
        self.back1Button.draw(self.screen)
        
    def updateOption(self):
        if pygame.key.get_pressed()[pygame.K_BACKSPACE]:
            self.state = "menu"
        if self.optionQuitButton.isPressed() and self.actionCooldown < pygame.time.get_ticks():
            self.actionCooldown = pygame.time.get_ticks() + 16 * 60 * 0.5
            self.state = "menu"

    def drawOption(self):
        self.optionQuitButton.draw(self.screen)

    def initLevel(self):
        # intialisation de la variable en la remplissant de None
        self.projectiles = [None for i in range(50)]
        self.enemies = [None for i in range(100)]
        self.obstacle = [None for i in range(100)]
        self.player = Player(50, self.screen.get_size()[1]//2, 16, 16, self.projectiles, 50, True)
        self.gamePause = False
        self.gameTimeStart = pygame.time.get_ticks()

    def updateLevel(self):
        if pygame.key.get_pressed()[pygame.K_ESCAPE] and self.actionCooldown < pygame.time.get_ticks():
            self.actionCooldown = pygame.time.get_ticks() + 16 * 60 * 0.2
            self.gamePause = not self.gamePause

        if not self.gamePause:
            # déplacement du joueur si il est vivant
            if not self.player.isDead():
                move(self.settings, self.screen, self.player)
            else:
                self.actionCooldown = pygame.time.get_ticks() + 16 * 60 * 0.2
                print("is dead")
                self.state = "end"
                self.updateEnd()
                self.drawEnd()
            self.level.update()
            self.player.update(self.dt)
            
            # ajout d'ennemis
            self.level.ennemiesSpawn(pygame.time.get_ticks() - self.gameTimeStart, self)

            # ajout d'obstacle
            #self.level.obstaclesSpawn(pygame.time.get_ticks() - self.gameTimeStart, self)

            # update de la position des projectiles
            for i in range(len(self.projectiles)):
                if self.projectiles[i]:
                    self.projectiles[i].update(self.dt)
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
                    self.enemies[i].update(self.dt)
                    if self.enemies[i].rectOverlap(self.player):
                        self.enemies[i].takeDamage(10)
                        self.player.takeDamage(10)
                    if self.enemies[i].isDead() or not self.enemies[i].rectOverlap(self.screenEntity):
                        self.enemies[i] = None
    
    def drawLevel(self):
        # Affichage du jeu
        self.level.draw(self.screen)

        # Affichage du joueur
        if self.player:
            self.player.draw(self.screen)

        # Affichage des ennemis
        for en in self.enemies:
            if en:
                en.draw(self.screen)

        # Affichage des projectiles
        for i in self.projectiles:
            if i:
                i.draw(self.screen)

Game()