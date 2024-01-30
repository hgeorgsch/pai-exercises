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
        perm = np.random.permutation( list(range(len(moves))) )
        moves = [ moves[i] for i in perm ]
        h = 2**30
        move = None
        for m in moves:
            if heuristic(m) < h: move = m
        print( "HillClimber", game.tostring(move), heuristic(game.state))
        game.setState( move )
    return(game.state)

if __name__ == "__main__":
    game = EightQueensGame()
    hillclimber(game,eightqueenheuristic)
    game.printreport()
