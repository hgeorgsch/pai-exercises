# (C) 2024: Hans Georg Schaathun <georg@schaathun.net> 

from queue import PriorityQueue
from EightQueen import *
from PuzzleGame import *

from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class Item:
    priority: int
    item: Any=field(compare=False)

def astarsolver(game,heuristic=None):
    """
    Use A* to solve a puzzle game.
    """
   
    queue = PriorityQueue()
    state = game.state
    start = str(state)

    # For node n, gScore[n] is the cost of the cheapest path from start to n currently known.
    cameFrom = { start: None }
    gScore = { start : 0 }
    fScore = { start: heuristic(game.state) }
    queue.put( Item( fScore[start], game.state ) )

    while not queue.empty():
        current = queue.get()
        state = current.item
        print(state)
        print( fScore[str(state)], gScore[str(state)], heuristic(state) )
        if game.isGoal(state): 
            print( "SOLUTION\n", state )
            break
        else:
            neighbours = game.nextstates(state)
            tentativeG = gScore[str(state)] + 1
            for s in neighbours:

                if str(s) in gScore: g = gScore[str(s)]
                else: g = tentativeG + 1
                if tentativeG < g:
                    # This path to s is better than any previous one. Record it!
                    cameFrom[str(s)] = state
                    gScore[str(s)] = tentativeG
                    fScore[str(s)] = tentativeG + heuristic(s)
                    print( fScore[str(s)], gScore[str(s)], heuristic(s) )
                    queue.put( Item(fScore[str(s)], s) )

    if not game.isGoal(state): 
        print( "Astar failed\n", state )
        print( "start\n", start )
    else:
        final = state
        path = []
        while type(state) != type(None):
            path.append( state )
            state = cameFrom[str(state)]
        print( path )
        s = path.pop()
        assert start == str(s)
        while path:
            s = path.pop()
            print( s )
            game.setState( s )
        print("FINAL\n", final)
        assert game.isGoal(final), "final is not goal"
        print(s)
        assert game.isGoal(s), "s is not goal"
        assert  str(s) == str(final), "s is not final"
    
    return game

if __name__ == "__main__":
    game = NPuzzle(3,4)
    astarsolver(game,manhattan)
    game.printreport()
