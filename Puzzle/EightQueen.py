# (C) 2024: Hans Georg Schaathun <georg@schaathun.net> 

import numpy as np

from PuzzleGame import Game, randomsolver, permute

class EightQueensGame(Game):
    def __init__(self,boardsize=8):
        """
        Initialise a game with a random state on the given (square) board size.
        """
        self.boardsize = boardsize
        self.state = [ np.random.randint(boardsize) for _ in range(boardsize) ]
        super().__init__()
    def nextstates(self,state=None):
        """
        Return a list of possible next states from the current state.
        """
        super().nextstates()
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
        It may be better to use `str(game.state)` instead.
        This function may give a more compact representation, but it
        is non-standard.
        """
        if type(state) == type(None): state = self.state
        return "".join( [ str(x) for x in state ] )

    def conflictcount(self,state=None,queen=None):
        """
        Return the number of constraints violated, i.e. the number of misplaced
        tiles.
        """
        if type(state) == type(None): state = self.state
        return eightqueenheuristic(state)

qpos = lambda state,i: (i,state[i])

def minconflicts(game):
    """
    Solver using the Min-Conflicts algorithm [AIMA:182].
    """
    while not game.isGoal():
       state = game.state.copy()
       vars = permute( list(range(len(state))))
       queen = vars.pop()
       while 0 == conflictcount(state, queen=queen ):
           queen = vars.pop()
       c = [ ( conflictcount(state,(queen,i)), i ) for i in range(game.boardsize) if i != state[queen] ]
       _,n = min(c)
       state[queen] = n
       game.setState( state )
    return game
def conflictcount(state=None,q=None,queen=None):
     if queen != None: q = qpos(state,queen)
     else: queen = q[0]
     boardsize = len(state)
     l = [ (queen,j) 
         for j in range(boardsize)
         if j != queen
         if eightqueenconflict(q,qpos(state,j)) ]
     return len(l)


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
    boardsize = len(state)
    l = [ (i,j) 
              for i in range(boardsize)
              for j in range(i) 
              if eightqueenconflict(qpos(state,i),qpos(state,j)) ]
    return len(l)



if __name__ == "__main__":
    game = EightQueensGame()
    minconflicts(game)
    # randomsolver(game)
    game.printreport()
