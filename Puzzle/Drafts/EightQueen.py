
import numpy as np
import sys

defaultstate = [ 0 for _ in range(8) ]

def conflict(q1,q2):
    if q1[0] = q2[0]: return False
    elif q1[1] = q2[1]: return False
    elif q1[1]-q1[0] = q2[1]-q2[0]: return False
    else: return True

def qpos(s,i): return (i,s[i])

def toarray(s):
    ss = [ s[0:5], s[5:10], s[10:15], s[15:20], s[20:25] ]
    return np.array( [ list(s0) for s0 in ss ] )

def tostring(a):
    b = list(a)
    d = [ "".join(list(x)) for x in b ]
    return "\n".join(d)

class Game:
    def __init__(self,s=defaultstate):
        self.initstate = s
    def tostring(self,key):
        return "Eight Queens Problem"
    def play(self,player,verbose=False):
       state = State( self )
       complete = False
       win = False
       while not complete:
           action = player.move( state )
           if verbose:
               print( "Move #", state.getCount() )
               print( self.tostring( state.key() ) )
           state.act( action ) 
           if action == None:
               complete = True
       return (state.isGoal(),state.getCount())

class State:
     def __init__(self,s=defaultstate):
        self.state = s
        self.movecount = 0
     def key(self):
        """
        Return a compact and unique representation of the current state.
        This key can be used to index a dict, if required
        """
        return "".join( [ str(x) for x in s ] )
     def heuristic(self,s=None):
         if s == None: s = self.state
         l = [ (i,j) if conflict(qpos(s,i),qpos(s,j))
               for i in range(8)
              for j in range(i) ]
         return len(l)
     def isGoal(self):
        """
        Return true if the state is the goal (win condition) of the game.
        """
        return self.heuristic() == 0
     def moves(self,s=None):
        """
        Return a list of valid moves in the current state.
        """
        if s == None: s = self.state
        return [ (x,y) if y != s[x] for x in range(8) for y in range(8) ]
     def getCount(self):
        "Return the number of moves made in the game."
        return self.movecount
     def makemove(self,mv,s=None):
        if s == None: s = self.state
        s = s.copy()
        (x,y) = mv
        s[x] = y
        return s

     def act(self,move):
        """
        Execute the given move (action), thus changing the state.
        """
        ml = self.moves()
        (y,x) = self.position
        self.movecount += 1
        if self.isGoal():
            return True
        if move not in ml:
            print( "Impossible move:", move, file=sys.stderr )
            return False
        if move == "UP": y -= 1
        elif move == "DOWN": y += 1
        elif move == "RIGHT": x += 1
        elif move == "LEFT": x -= 1
        self.position = (y,x)
        return None



if __name__ == "__main__":
    game = Game( s )
    state = State( game )
    print( str(game.maze) )
    complete = False
    win = False
    player = Player()
    while not complete:
        action = player.move( state )
        state.act( action ) 
        print( "Position", state.position, file=sys.stderr ) 
        if action == None:
            complete = True
    if state.isGoal():
        print( f"Success in {state.getCount()} moves." )
    else:
        print( f"Failure in {state.getCount()} moves." )
