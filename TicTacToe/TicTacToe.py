"""
A module containing the basic infrastructure to play a game
of tic tac toe.
"""

import numpy as np
import sys

def tostring(a):
    return "".join(list(a.flatten()))
def toarray(s):
    ss = [ s[0:3], s[3:6], s[6:9] ]
    return np.array( [ list(s0) for s0 in ss ] )

def equiv(a):
    return [ a, a[:,::-1], a[::-1,:], a[::-1,::-1] ]

def moves(a):
    return [ (x,y) for x in range(3) for y in range(3) if a[x,y] == "." ]

def lines(a):
    l = [ a.diagonal(), a[:,::-1].diagonal() ]
    for i in range(3):
        l.append( a[:,i] )
        l.append( a[i,:] )
    return l

def getvalue(w):
    v = { "X": +1, "O": -1, None: 0 }[w]
    print("getvalue",w,v,file=sys.stderr)
    return v

class Game:
    def __init__(self):
        self.state = State(toarray("........."))
    def play(self,xplayer,oplayer):
        cont = True
        winner = None
        while cont:
            print(str(self.state.getArray()))
            p = self.state.toMove()
            if p == "X":
                m = xplayer.move(self.state)
            elif p == "O":
                m = oplayer.move(self.state)
            else:
                cont = False
            self.state.makeMove(m)
            winner = self.state.isWin()
            if winner != None:
                cont = False
        if winner == None:
            print( "The game ended in a draw." )
        else:
            print( "Player ", winner, " won!" )
        print(str(self.state.getArray))
        return winner

class State:
    def __init__(self,array):
        self.array = array
    def getArray(self):
        """
        Get the board state as a 3x3 numpy array with "X", "O", and "."
        entries.
        """
        return self.array
    def key(self):
        return tostring(self.array)
    def copy(self):
        """
        Return a copy of the State.
        """
        return State(self.array.copy())
    def moveCopy(self,m):
        """
        Make a new State object by copying the current state and
        applying the move m.
        """
        s = State(self.array.copy())
        s.makeMove(m)
        return s
    def makeMove(self,m):
        (x,y) = m
        if x < 0 or x > 2:
            print("Error: x coordinate is out of bounds",file=sys.stderr)
            return None
        if y < 0 or y > 2:
            print("Error: x coordinate is out of bounds",file=sys.stderr)
            return None
        if self.array[x,y] != ".":
            print("Square is already occupied", file=sys.stderr)
            return None
        self.array[x,y] = self.toMove()
    def moves(self):
        """
        Return a list of valid moves.
        Each move is (x,y) coordinates in the 0,1,2 range.
        """
        return moves(self.array)
    def isWin(self):
        win1 = np.array(list("OOO"))
        win2 = np.array(list("XXX"))
        for l in lines(self.array):
            if (l == win1).all():
                return "O"
            elif (l == win2).all():
                return "X"
        return None
    def toMove(self):
        c1 = self.array.flatten().tolist().count("O")
        c2 = self.array.flatten().tolist().count("X")
        if c2+c1 == 9:
            return None
        elif c2 > c1:
            return "O"
        else: 
            return "X"
