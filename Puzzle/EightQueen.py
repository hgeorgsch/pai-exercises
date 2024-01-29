# (C) 2024: Hans Georg Schaathun <georg@schaathun.net> 

import numpy as np

from PuzzleGame import Game, randomsolver

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



if __name__ == "__main__":
    game = EightQueensGame()
    randomsolver(game)
