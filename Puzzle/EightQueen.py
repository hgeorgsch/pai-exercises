# (C) 2024: Hans Georg Schaathun <georg@schaathun.net> 

import numpy as np
import sys



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

class EightQueensGame(Game):
    def __init__(self,boardsize=8):
        """
        Initialise a game with a random state on the given (square) board size.
        """
        self.boardsize = boardsize
        self.state = [ np.random.randint(boardsize) for _ in range(boardsize) ]
    def nextstates(self,state=None):
        """
        Return a list of possible next states from the current state.
        """
        if state == None: state = self.state
        r = []
        for x in range(self.boardsize):
           for y in range(self.boardsize):
               if y != state[x]:
                   s = state.copy()
                   s[x] = y
                   r.append( s )
        return r

    def tostring(self,state=None):
        """
        Return a string representation of the current state.
        """
        if state == None: state = self.state
        return "".join( [ str(x) for x in state ] )

    def conflictcount(self,state=None):
        """
        Return the number of constraints violated, i.e. the number of pairs of queens
        which attack each other.
        """
        if state == None: state = self.state
        return eightqueenheuristic(state)

class NPuzzle(Game):
    def __init__(self,rows=3,columns=3):
        """
        Initialise a game with a random state on the given rows-x-columns board size.
        """
        self.size = size = rows*columns
        self.state = np.random.permutation(range(size))
        self.state.shape = (rows,columns)
    def nextstates(self,state=None):
        """
        Return a list of possible next states from the current state.
        """
        if type(state) == type(None): state = self.state
        empty = np.where( state == 0 )
        print(empty)
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
        if state == None: state = self.state
        return str(state)

    def conflictcount(self,state=None):
        """
        Return the number of constraints violated, i.e. the number of misplaced
        tiles.
        """
        if type(state) == type(None): state = self.state
        return puzzlecount(state)

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

def eightqueenconflict(q1,q2):
    """
    True if two Queens in positions q1 and q2 would attack each other 
    on a chess board.
    """
    if q1[0] == q2[0]: return True
    elif q1[1] == q2[1]: return True
    elif abs(q1[1]-q2[1]) == abs(q1[0]-q2[0]): return True
    else: return False

def eightqueenheuristic(state):
    """
    The number of mutually attacking queen pairs in the Eight Queens problem.
    """
    qpos = lambda state,i: (i,state[i])
    boardsize = len(state)
    l = [ (i,j) 
              for i in range(boardsize)
              for j in range(i) 
              if eightqueenconflict(qpos(state,i),qpos(state,j)) ]
    return len(l)

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


if __name__ == "__main__":
    game = EightQueensGame()
    randomsolver(game)
    # game = NPuzzle()
    # randomsolver(game,manhattan)
