
import numpy as np
import sys

s = " # . " + \
    ".*.*." + \
    " # # " + \
    ".*.*." + \
    " . # "

def toarray(s):
    ss = [ s[0:5], s[5:10], s[10:15], s[15:20], s[20:25] ]
    return np.array( [ list(s0) for s0 in ss ] )

class Game:
    def __init__(self,a):
        self.maze = toarray(a)

class State:
    def __init__(self,g):
        self.game = g
        self.position = (0,0)
    def key(self): return self.position
    def isGoal(self):
        return self.position == (2,2)
    def moves(self):
        (x0,y0) = self.position
        (x,y) = (2*x0,2*y0)
        ml = []
        print( "Finding moves for", (x0,y0), (x,y), file=sys.stderr )
        if y0 < 2 and self.game.maze[x,y+1] == ".":
           ml.append( "RIGHT" )
        if y0 > 0 and self.game.maze[x,y-1] == ".":
           ml.append( "LEFT" )
        if x0 < 2 and self.game.maze[x+1,y] == ".":
           ml.append( "DOWN" )
        if x0 > 0 and self.game.maze[x-1,y] == ".":
           ml.append( "UP" )
        return ml
    def sense(self):
        return self.moves()
    def act(self,move):
        ml = self.moves()
        (y,x) = self.position
        if move not in ml:
            print( "Impossible move:", move )
            return False
        if move == "UP": y -= 1
        elif move == "DOWN": y += 1
        elif move == "RIGHT": x += 1
        elif move == "LEFT": x -= 1
        self.position = (y,x)
        if self.isGoal():
            print( "Goal reached" )
            return True
        return None

undo = {
        "UP": "DOWN",
        "DOWN": "UP",
        "RIGHT": "LEFT",
        "LEFT": "RIGHT"
        }

class Player:
   def __init__(self):
       self.untried = {}
       self.state = None
       self.action = None
       self.unbacktracked = {}
   def dfs(self,state):
       key = state.key()
       if state.isGoal():
           print( "GOAL" )
           return None
       if key not in self.untried:
           self.untried[key] = state.moves()
           print( "Moves in state", key, self.untried[key], file=sys.stderr )
       if self.state != None:
           if key not in self.unbacktracked:
               self.unbacktracked[key] = []
           self.unbacktracked[key].append( (self.state, undo[self.action]) )
           print( "Unbacktracked", key, self.unbacktracked[key] )
       if self.untried[key] == []:
           btl = self.unbacktracked.get( key ) 
           if btl == [] or btl == None: return None
           (s,action) = self.unbacktracked[key].pop( ) 
           self.state = None
           self.action = None
           print( "Backtracking", action, s, file=sys.stderr )
       else:
           action = self.untried[key].pop()
           self.state = state
           self.action = action
           print( "Forward", action )
       print( "DFS returning", action, self.action, self.state, file=sys.stderr )
       return action

if __name__ == "__main__":
    game = Game( s )
    state = State( game )
    print( str(game.maze) )
    complete = False
    win = False
    player = Player()
    while not complete:
        action = player.dfs( state )
        state.act( action ) 
        print( "Position", state.position, file=sys.stderr ) 
        if action == None:
            complete = True
    if state.isGoal():
        print( "Success!" )
    else:
        print( "Failure!" )
