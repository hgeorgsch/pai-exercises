# (C) 2024: Hans Georg Schaathun <georg@schaathun.net> 

import numpy as np
import sys


class Game:
    def setState(self,state):
        self.state = state
    def isGoal(self,state=None):
        """
        Return true if the state is the goal (win condition) of the game.
        """
        if state == None: state = self.state
        return self.conflictcount(state) == 0
    def conflictcount(self,state=None):
        return 0

class EightQueensGame(Game):
    def __init__(self,boardsize=8):
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
        if state == None: state = self.state
        return "".join( [ str(x) for x in state ] )

    def conflictcount(self,state=None):
        if state == None: state = self.state
        return eightqueenheuristic(state)

class NPuzzle(Game):
    def __init__(self,rows,columns):
        size = rows*columns
        self.state = np.random.permutation(range(size))
        self.state.shape = (rows,columns)
    def nextstates(self,state=None):
        """
        Return a list of possible next states from the current state.
        """
        if state == None: state = self.state
        r = []
        for x in range(boardsize):
           for y in range(boardsize):
               if y != state[x]:
                   s = state.copy()
                   s[x] = y
                   r.append( s )
        return r


    def tostring(self,state=None):
        if state == None: state = self.state
        return "".join( [ str(x) for x in state ] )

    def conflictcount(self,state=None):
        if state == None: state = self.state
        return eightqueenheuristic(state)

def eightqueenconflict(q1,q2):
        if q1[0] == q2[0]: return False
        elif q1[1] == q2[1]: return False
        elif q1[1]-q1[0] == q2[1]-q2[0]: return False
        else: return True

def eightqueenheuristic(state):
        qpos = lambda state,i: (i,state[i])
        boardsize = len(state)
        l = [ (i,j) 
              for i in range(boardsize)
              for j in range(i) 
              if eightqueenconflict(qpos(state,i),qpos(state,j)) ]
        return len(l)

def randomsolver(game,heuristic=None):
    print(game.tostring())
    while not game.isGoal():
        moves = game.nextstates()
        i = np.random.choice( range( len( moves ) ) )
        game.setState( moves[i] )
        print(game.tostring())
    return(game.state)

def astarsolver(game,heuristic=None):
    pass

if __name__ == "__main__":
    game = EightQueensGame()
    randomsolver(game)
