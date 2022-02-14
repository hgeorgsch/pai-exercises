
import numpy as np
import sys

s = """ # . """
    """.*.*."""
    """ # # """
    """.*.*."""
    """ . # """ 

def toarray(s):
    ss = [ s[0:5], s[5:10], s[10:15], s[15:20], s[20:25] ]
    return np.array( [ list(s0) for s0 in ss ] )

class Game:
    def __init__(self,a):
        self.maze = a

class State:
    def __init__(self,g):
        self.game = g
        self.position = (0,0)
    def isGoal(self)
        return self.position == (2,2)
    def moves(self)
        (x0,y0) = self.position
        (x,y) = (2*x0,2*y0)
        ml = []
        if x0 < 2 and self.game.maze[x0+1,y0] " ":
           ml.append( "RIGHT" )
        if x0 > 0 and self.game.maze[x0-1,y0] == " ":
           ml.append( "LEFT" )
        if y0 < 2 and self.game.maze[x0,y0+1] " ":
           ml.append( "DOWN" )
        if y0 > 0 and self.game.maze[x0,y0-1] == " ":
           ml.append( "UP" )
        return ml
    def sense(self):
        return self.moves()
    def act(self,move):
        ml = self.moves
        (x,y) = self.position
        if not move in ml:
            print( "Impossible move" )
            return False
        if move == "UP": y -= 1
        elif move == "DOWN": y += 1
        elif move == "RIGHT": x += 1
        elif move == "LEFT": x -= 1
        self.position = (x,y)
        if self.isGoal():
            print( "Goal reached" )
            return True
        return None

