# (C) 2024: Hans Georg Schaathun <georg@schaathun.net> 

import numpy as np

class Game:
    """
    Some generic features of puzzle games, intended as superclass for
    the N-Puzzle and the Eight Queens Problem.
    """
    def setState(self,state):
        """
        Set the solution state.
        """
        self.state = state
    def isGoal(self,state=None):
        """
        Return true if the state is the goal (win condition) of the game.
        """
        if type(state) == type(None): state = self.state
        return self.conflictcount(state) == 0
    def conflictcount(self,state=None):
        """
        Return the number of constraints violated.
        """
        return 0

def randomsolver(game,heuristic=None):
    """
    This solver tries to solve a puzzle game by moving at random.
    """
    print(game.tostring())
    while not game.isGoal():
        moves = game.nextstates()
        i = np.random.choice( range( len( moves ) ) )
        game.setState( moves[i] )
        print(game.tostring())
        if heuristic: print(heuristic(game.state))
    return(game.state)

def manhattan(state):
    """
    Calculate the total Manhattan distances of misplaced tiles in the
    N-Puzzle game.
    """
    rows,columns = state.shape
    goal = np.array(list(range(1,state.size)) + [0])
    goal.shape = state.shape
    mdist = 0
    for x in range(1,state.size):
      m1 = np.where( state == x )
      m2 = np.where( goal == x )
      mdist += int(np.abs(m1[0]-m2[0]))
      mdist += int(np.abs(m1[1]-m2[1]))
    return mdist
def puzzlecount(state):
    """
    The number of misplaced tiles in N-Puzzle.
    """
    state = state.flatten()
    misplaced = [ i for i in range(1,state.size) if state[i-1] != i ]
    return len(misplaced)


if __name__ == "__main__":
    game = NPuzzle()
    randomsolver(game,manhattan)
