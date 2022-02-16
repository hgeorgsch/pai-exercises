
import numpy as np
import sys

mazelist = [
     " # . " + \
     ".*.*." + \
     " # # " + \
     ".*.*." + \
     " . # ",
     " # . " + \
     ".*.*." + \
     " . # " + \
     "#*.*#" + \
     " . . ",
     " . # " + \
     ".*.*." + \
     " # . " + \
     ".*.*." + \
     " . # ",
     " . . " + \
     ".*.*." + \
     " # # " + \
     ".*#*#" + \
     " . . ",
     " . . " + \
     ".*.*." + \
     " # # " + \
     ".*#*." + \
     " . # "
     ]

def toarray(s):
    ss = [ s[0:5], s[5:10], s[10:15], s[15:20], s[20:25] ]
    return np.array( [ list(s0) for s0 in ss ] )

def tostring(a):
    b = list(a)
    d = [ "".join(list(x)) for x in b ]
    return "\n".join(d)

class Game:
    def __init__(self,a):
        self.maze = toarray(a)
    def tostring(self,key):
        maze = self.maze.copy()
        (x,y) = key
        maze[2*x,2*y] = "X"
        return tostring(maze)
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
    def __init__(self,g):
        self.game = g
        self.position = (0,0)
        self.movecount = 0
    def key(self):
        """
        Return a compact and unique representation of the current state.
        This key can be used to index a dict, if required
        """
        return self.position
    def isGoal(self):
        """
        Return true if the state is the goal (win condition) of the game.
        """
        return self.position == (2,2)
    def moves(self):
        """
        Return a list of valid moves in the current state.
        """
        (x0,y0) = self.position
        (x,y) = (2*x0,2*y0)
        ml = []
        if y0 < 2 and self.game.maze[x,y+1] == ".":
           ml.append( "RIGHT" )
        if y0 > 0 and self.game.maze[x,y-1] == ".":
           ml.append( "LEFT" )
        if x0 < 2 and self.game.maze[x+1,y] == ".":
           ml.append( "DOWN" )
        if x0 > 0 and self.game.maze[x-1,y] == ".":
           ml.append( "UP" )
        return ml
    def getCount(self):
        "Return the number of moves made in the game."
        return self.movecount
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
