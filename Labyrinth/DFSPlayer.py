from Labyrinth import ( State, Game, mazelist )
import sys

undo = {
        "UP": "DOWN",
        "DOWN": "UP",
        "RIGHT": "LEFT",
        "LEFT": "RIGHT"
        }

class DFSPlayer:
   def __init__(self,debug=False):
       self.untried = {}
       self.state = None
       self.action = None
       self.unbacktracked = {}
       self.debug = debug
   def move(self,state):
       key = state.key()
       if state.isGoal():
           if self.debug: print( "GOAL" )
           return None
       if key not in self.untried:
           self.untried[key] = [ x for x in state.moves()
                                   if undo[x] != self.action ]
           if self.debug:
             print( "Moves in state", key, self.untried[key], file=sys.stderr )
       if self.state != None:
           if key not in self.unbacktracked:
               self.unbacktracked[key] = []
           self.unbacktracked[key].append( (self.state, undo[self.action]) )
           if self.debug:
             print( "Unbacktracked", key, self.unbacktracked[key] )
       if self.untried[key] == []:
           btl = self.unbacktracked.get( key ) 
           if btl == [] or btl == None: return None
           (s,action) = self.unbacktracked[key].pop( ) 
           self.state = None
           self.action = None
           if self.debug:
              print( "Backtracking", action, s, file=sys.stderr )
       else:
           action = self.untried[key].pop()
           self.state = state
           self.action = action
           if self.debug:
              print( "Forward", action )
       if self.debug:
           print( "DFS returning", action, self.action, self.state, file=sys.stderr )
       return action

if __name__ == "__main__":
    for s in mazelist:
       game = Game( s )
       print( str(game.maze) )
       (w,c) = game.play( DFSPlayer(), verbose=True )
       if w:
           print( f"Success in {c} moves." )
       else:
           print( f"Failure in {c} moves." )
