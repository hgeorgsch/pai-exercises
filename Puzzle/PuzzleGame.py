# (C) 2024: Hans Georg Schaathun <georg@schaathun.net> 

import numpy as np


class Game:
    """
    Some generic features of puzzle games, intended as superclass for
    the N-Puzzle and the Eight Queens Problem.
    """
    def __init__(self):
        self.movecount = 0
        self.nodecount = 0

    def printreport(self):
        if self.isGoal():
           print( f"Solved" )
        else:
           print( f"NOT SOLVED" )
        print( "Number of moves", self.movecount )
        print( "Nodes expanded ", self.nodecount )

    def setState(self,state):
        """
        Set the solution state.  Returns True if the goal is reached
        and raises an exception if the new state is not a valid move.
        """
        if str(state) in map(str,self.nextstates()):
            self.state = state
            self.movecount += 1
            print( "setState", state, self.movecount )
        else: 
            print( self.state, state )
            raise Exception( "Invalid move" )
        return self.isGoal()

    def nextstates(self,state=None):
        """
        Return a list of possible next states from the current state.
        """
        self.nodecount += 1
        return []
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
def permute(s):
        perm = np.random.permutation( list(range(len(s))) )
        return [ s[i] for i in perm ]

class NPuzzle(Game):
    def __init__(self,rows=3,columns=3):
        """
        Initialise a game with a random state on the given rows-x-columns board size.
        """
        self.size = size = rows*columns
        self.state = np.random.permutation(range(size))
        self.state.shape = (rows,columns)
        super().__init__()

    def nextstates(self,state=None):
        """
        Return a list of possible next states from the current state.
        """
        super().nextstates()
        if type(state) == type(None): state = self.state
        empty = np.where( state == 0 )
        (x,y) = int(empty[0]), int(empty[1])
        (m,n) = state.shape
        moves = []
        if x > 0: moves.append( (x-1,y) )
        if x < m-1: moves.append( (x+1,y) )
        if y > 0: moves.append( (x,y-1) )
        if y < n-1: moves.append( (x,y+1) )
        r = []
        for (x0,y0) in moves:
            s = state.copy()
            s[x,y] = s[x0,y0]
            s[x0,y0] = 0
            r.append(s)
        return r

    def tostring(self,state=None):
        """
        Return a string representation of the current state.
        """
        if type(state) == type(None): state = self.state
        return str(state)

    def conflictcount(self,state=None):
        """
        Return the number of constraints violated, i.e. the number of misplaced
        tiles.
        """
        if type(state) == type(None): state = self.state
        return puzzlecount(state)

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
    game = NPuzzle(2,3)
    randomsolver(game,manhattan)
    game.printreport()
