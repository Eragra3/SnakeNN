import pygame, math, sys
from pygame.locals import *


class SnakeGUI:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.nomNom = pygame.image.load('apple.png')

    def init(self, boardWidth, boardHeight):

        offset = 25

        self.tileWidth = (800 - offset * 2) / boardWidth
        self.tileHeight = (600 - offset * 2) / boardHeight

        top = offset
        right = 600 - offset
        bottom = 800 - offset
        left = offset

        gridColor = Color(255, 255, 255, 255)

        for i in range(boardWidth):
            x = left + self.tileWidth
            pygame.draw.line(self.screen, gridColor, (x * i + left, top), (x * i + left, bottom))
        for j in range(boardHeight):
            y = left + self.tileWidth
            pygame.draw.line(self.screen, gridColor, (left, y * i + top), (right, y * i + top))

        pygame.display.update()

    def update(self):
        pygame.display.update()

    def displayNomNom(self, gameEngine):
        self.screen.blit(self.nomNom, gameEngine.nomNomPosition)

    def drawHead(self):
        #todo
        return False


    def run(self, gameEngine):

        self.init(gameEngine.width, gameEngine.height)

        gameEngine.start()
        self.displayNomNom(gameEngine.nomNomPosition)
        self.drawHead(gameEngine.headPosition)

        while True:

            for event in pygame.event.get():
                if not hasattr(event, 'key'): continue
                down = event.type == KEYDOWN  # key down or up?
                if down:
                    if event.key == K_UP:
                        gameEngine.goForward()
                        self.update()
                    elif event.key == K_RIGHT:
                        gameEngine.goRight()
                        self.update()
                    elif event.key == K_LEFT:
                        gameEngine.goLeft()
                        self.update()
                    elif event.key == K_ESCAPE:
                        sys.exit(0)

            if not gameEngine.isRunning:
                print("you lost :c")
                gameEngine.restart()
