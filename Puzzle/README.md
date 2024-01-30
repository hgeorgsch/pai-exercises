# Puzzle Games

This directory includes two puzzle games used several times as examples 
in AIMA Chapter 3-5, namely the Eight Queens Problem and the $N$-Puzzle
(8-Puzzle and 11-Puzzle).

Both games are implemented using the same Game interface, and the
default `randomsolver(game)` function can solve either game by a random
walk.  Please refer to this as an example of how to use the Game
interface.

+ To solve a game `game`, the solver has iteratively to call 
  `game.setState(s)` each time giving a valid new state `s` 
  as given by `game.nextstates()`.
+ When the game reaches the goal state, i.e. `game.isGoal()`
  returns True, the solver should terminate.
+ The length of the solution path can now be examined as
  `game.movecount`.
+ The number of nodes expanded (calls to `game.nextstates()`
  can be examined as `game.nodecount`
+ A diagnostic result can be printed with `game.printreport()`.


Note that the `game` object can be used to examine states without
actually changing the state of the game.  Thus
+ `game.isGoal(s)` checks if `s` is the goal
+ `game.nextstates(s)` given the valid next states that can be 
  reached from state `s`
+ `game.conflictcount(s)` gives the number of conflicts in state `s`,
  and serves as a basic heuristic function.
  (Similarly `game.conflictcount()` coit
The current state can be retrieved as `game.state`.

To test a given solver function `solver` on the 8-Puzzle,
the following code will do
```
game = NPuzzle(3,3)
solver(game)
print( f"Solved in {game.movecount} moves" )
```
Other typical games to test would be
+ `game = NPuzzle(4,3)`
+ `game = EightQueens()`

For the NPuzzle game there is an extra heuristic function provided,
called `manhattan()` in addition to the default `puzzlecount()` aka.
`game.conflictcount()`.

+ **Task**
    1. Can you implement solvers which are faster than `randomsolver()`?
    2. How fast can you make it?
+ **Caveats**
    1. The code is not optimised in any way; for benchmarking purposes, it would
       have to be reviewed and made faster.
    2. The $N$-Puzzle does not always have a solution, and some of the solvers will
       continue for ever.
+ **Sample Solutions**
    1. A* : `Astar.py`
    2. Naive Hill Climber : `HillClimber.py`
    3. Random walk : `PuzzleGame.py`
