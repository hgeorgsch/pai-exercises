# (C) 2024: Hans Georg Schaathun <georg@schaathun.net> 

from EightQueen import *
from Astar import *

if __name__ == "__main__":
    game = EightQueensGame()
    astarsolver(game,eightqueenheuristic)
    game.printreport()
