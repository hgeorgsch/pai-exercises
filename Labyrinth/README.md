# 3x3 Labyrinth

The player has to move from square (0,0) to (2,2) in a 3x3 labyrinth.
The layout is unknown, and the player can only see which moves are
possible from the current square.

## Task

Implement a class with a method `move(state)` which returns a move
or `None`.

The argument `state` is a `State` object with the following important 
methods:

+ `moves()` returns a list of valid moves.
+ `isGoal()` return true if the state is the Goal.
+ `key()` returns a unique identifier which can be used as a key for a `dict`,
  or for comparing states.

Note that the agent has to return `None` if the goal state has been reached.

You can use the file `Template.py` as a starting point.  This also includes
a test on five different mazes.  You can run the test as

```sh
python3 Template.py
```

The script part of `Template.py` also shows how to play the game.
Feel free to copy and tweak to run your own tests.

The game logic is in the `Labyrinth` module.   You can make new mazes to test
by following the pattern from the `mazelist` object which is used in the test
script.

## Sample Solution

The file `DFSPlayer.py` contains an implementation of Online DFS.
This file is structured and can be used in the same way as `Template.py`.

