# (C) 2024: Hans Georg Schaathun <georg@schaathun.net> 

from queue import PriorityQueue
from EightQueen import *
from PuzzleGame import *

def hillclimber(game,heuristic=None):
    """
    This solver tries to solve a puzzle game by moving at random.
    """
    print(game.tostring())
    while not game.isGoal():
        moves = game.nextstates()
        moves = np.random.permutation( moves )
        h = 2**30
        move = None
        for m in moves:
            if heuristic(m) < h: move = m
        game.setState( m )
        print(game.tostring())
        if heuristic: print(heuristic(game.state))
    return(game.state)

if __name__ == "__main__":
    game = EightQueensGame()
    hillclimber(game,eightqueenheuristic)
