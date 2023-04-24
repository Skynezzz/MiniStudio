import pygame, math

class Level():
    
    def __init__(self, levelNumber):
        self.level = {}
        a = 'game/level/level' + str(levelNumber) + '.txt'
        docLevels = open(a, 'r')
        levels = docLevels.read()
        docLevels.close
        for row in levels.split('\n'):
            level = row.split(': ')
            self.level[level[0]] = level[1]
        ennemies = self.level['ennemies'].split(', ')
        self.level['ennemies'] = []
        for ennemy in ennemies:
            ennemyProps = ennemy.split('/')
            self.level['ennemies'].append({'time': int(ennemyProps[0]), 'type': ennemyProps[1]})
        obstacles = self.level['obstacles'].split(', ')
        self.level['obstacles'] = []
        for obstacle in obstacles:
            obstacleProps = obstacle.split('/')
            self.level['obstacles'].append({'time': int(obstacleProps[0]), 'type': obstacleProps[1]})

        self.background = pygame.transform.scale(pygame.image.load(self.level['background']).convert(), (2150 * pygame.display.get_window_size()[1] / 600, pygame.display.get_window_size()[1]))
        self.scroll = 0
        self.speed = 10

        print("ENEMY:" +  str(self.level['ennemies']))
        print("OBSTACLES:" +  str(self.level['obstacles']))
        
    def ennemiesSpawn(self, timer):
        ennemyTab = []
        for ennemy in self.level['ennemies']:
            if timer >= ennemy['time']:
                ennemyTab += [ennemy['type']]
        return ennemyTab

    def obstaclesSpawn(self, timer):
        obstacleTab = []
        for obstacle in self.level['obstacles']:
            if timer >= obstacle['time']:
                obstacleTab += [obstacle['type']]
        return obstacleTab
    
    def draw(self, screen):
        i = 0
        while(i < 100):
            screen.blit(self.background, (self.background.get_width()*i + self.scroll, 0))
            i += 1

    def update(self):
        # FRAME FOR SCROLLING
        self.position -= self.speed
        # RESET THE SCROLL FRAME
        if abs(self.position) > self.background.get_width():
            self.position = 0