import sys
from pip._vendor.distlib.compat import raw_input
from Snake.SnakeGameEngine import *
from Snake.GUI import *


def main(argv):
    useGui = True

    gameEngine = GameEngine(10, 10)

    gui = SnakeGUI()

    if not useGui:

        input = raw_input("Next command:")
        input = input.lower()

        while input not in ["exit", "0", "quit", "q"]:
            if input in ["go", "g"]:
                gameEngine.goForward()
            elif input in ["left", "l"]:
                gameEngine.goLeft()
            elif input in ["right", "r"]:
                gameEngine.goRight()

            gui.update()

            if not gameEngine.isRunning:
                print("you lost :c")
                break

            print(gameEngine.draw())

            input = raw_input("Next command:")
            input = input.lower()
    else:
        gui.run(gameEngine)

    pass


if __name__ == "__main__":
    main(sys.argv)
