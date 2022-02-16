from Labyrinth import ( State, Game, mazelist )
import random

class RandomPlayer:
    def __init__(self):
        pass
    def move(self,state):
        "Make a random move from a given list of options."
        return random.choice(state.moves())

if __name__ == "__main__":
    for s in mazelist:
       game = Game( s )
       print( str(game.maze) )
       (w,c) = game.play( RandomPlayer() )
       if w:
           print( f"Success in {c} moves." )
       else:
           print( f"Failure in {c} moves." )
