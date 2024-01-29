# Puzzle Games

This directory includes two puzzle games used several times as examples 
in AIMA Chapter 3-5, namely the Eight Queens Problem and the $N$-Puzzle
(8-Puzzle and 11-Puzzle).

Both games are implemented using the same Game interface, and the
default `randomsolver()` function can solve either game by a random
walk.  Please refer to this as an example of how to use the Game
interface.

1.  Initialise the game with a random start state
    + `game = NPuzzle(4,3)`
    + `game = EightQueens(4,3)`

    The game has a current state, but most methods can be called with
    an explicit state; if none is given, the current state is used.
2.  You can get the current state as `game.state` 
3.  `game.isGoal()` or `game.isGoal(state)` tells you if the state is
    the goal state.
3.  You can get possible next states as `game.nextstates()` or
    `game.nextstates(state)`.
4.  We can change the current state as `game.setState(state)` 
5.  The number of conflicts is given as `game.conflictcount()` or
    `game.conflictcount(state)`.  This is the most basic heuristic
    function.

For the NPuzzle game there is an extra heuristic function provided,
called `manhattan()` in addition to the default `puzzlecount()` aka.
`game.conflictcount()`.

+ **Task**
    1. Can you implement solvers which are faster than `randomsolver()`?
    2. How fast can you make it?
