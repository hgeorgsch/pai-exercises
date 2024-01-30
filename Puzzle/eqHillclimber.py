# (C) 2024: Hans Georg Schaathun <georg@schaathun.net> 

from EightQueen import *
from HillClimber import *

if __name__ == "__main__":
    game = EightQueensGame()
    hillclimber(game,eightqueenheuristic)
    game.printreport()
