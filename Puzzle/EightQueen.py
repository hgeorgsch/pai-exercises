# (C) 2024: Hans Georg Schaathun <georg@schaathun.net> 

import numpy as np
import sys

boardsize = 8
defaultstate = [ 0 for _ in range(boardsize) ]
randomstate = [ np.random.randint(boardsize) for _ in range(boardsize) ]

def nextstates(state):
    """
    Return a list of possible next states from the current state.
    """
    r = []
    for x in range(boardsize):
       for y in range(boardsize):
           if y != state[x]:
               s = state.copy()
               s[x] = y
               r.append( s )
    return r

def conflict(q1,q2):
    if q1[0] == q2[0]: return False
    elif q1[1] == q2[1]: return False
    elif q1[1]-q1[0] == q2[1]-q2[0]: return False
    else: return True

def qpos(s,i): return (i,s[i])

def tostring(s): return "".join( [ str(x) for x in s ] )

def conflictcount(s):
    l = [ (i,j) 
          for i in range(boardsize)
          for j in range(i) 
          if conflict(qpos(s,i),qpos(s,j)) ]
    return len(l)

def isGoal(s):
    """
    Return true if the state is the goal (win condition) of the game.
    """
    return conflictcount(s) == 0


if __name__ == "__main__":
    state = randomstate
    print(tostring(state))
    while not isGoal(state):
        i = np.random.choice( range( len( nextstates( state ) ) ) )
        state = nextstates( state )[i]
        print(state)
