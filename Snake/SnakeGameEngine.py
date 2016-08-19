from enum import Enum
from random import randint


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Direction(Enum):
    up = 1
    right = 2
    down = 3
    left = 4


class GameEngine:
    height = 10
    width = 10

    headDirection = Direction.right
    headPosition = Point(width / 2, height / 2)
    nomNomPosition = Point(width / 2 + 2, height / 2 - 1)

    points = 0
    isRunning = True
    isWon = False

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def rotateRight(self):
        if self.headDirection == Direction.left:
            self.headDirection = Direction.up
        elif self.headDirection == Direction.up:
            self.headDirection = Direction.right
        elif self.headDirection == Direction.right:
            self.headDirection = Direction.down
        else:
            self.headDirection = Direction.left

    def rotateLeft(self):
        if self.headDirection == Direction.up:
            self.headDirection = Direction.left
        elif self.headDirection == Direction.left:
            self.headDirection = Direction.down
        elif self.headDirection == Direction.down:
            self.headDirection = Direction.right
        else:
            self.headDirection = Direction.up

    def goForward(self):
        if self.headDirection == Direction.up:
            self.headPosition.y += 1
        elif self.headDirection == Direction.down:
            self.headPosition.y -= 1
        elif self.headDirection == Direction.right:
            self.headPosition.x += 1
        else:
            self.headPosition.x -= 1

        if self.headPosition.x < 0 or self.headPosition.x >= self.width or \
                        self.headPosition.y < 0 or self.headPosition.y >= self.height:
            self.gameLost()

        if self.headPosition == self.nomNomPosition:
            self.eatNomNom()

    def goLeft(self):
        self.rotateLeft()
        self.goForward()

    def goRight(self):
        self.rotateRight()
        self.goForward()

    def spawnNomNom(self):
        self.nomNomPosition.x = randint(0, self.width - 1)
        self.nomNomPosition.y = randint(0, self.height - 1)

    def eatNomNom(self):
        self.points += 1
        self.spawnNomNom()

    def gameLost(self):
        self.isRunning = False
        self.isWon = False

    def gameWon(self):
        self.isRunning = True
        self.isWon = True