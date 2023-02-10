# 3x3 Labyrinth

The player has to move from square (0,0) to (2,2) in a 3x3 labyrinth.
The layout is unknown, and the player can only see which moves are
possible from the current square.

## Task

To play the game, a Player class has to be implemented with a `move()`
which returns a move or `None`.
The argument `state` is a `State` object with the following important 
methods:

+ `moves()` returns a list of valid moves.
+ `isGoal()` return true if the state is the Goal.
+ `key()` returns a unique identifier which can be used as a key for a `dict`,
  or for comparing states.

Note that the agent has to return `None` if the goal state has been reached.

You can use the file `Template.py` as a starting point.  
It containes the code for a Player behaving randomly, and the code
to test the player on five different mazes.  You can run the test as

```sh
python3 Template.py
```

The script part of `Template.py` also shows how to play the game.
Feel free to copy and tweak to run your own tests.

The game logic is in the `Labyrinth` module.   You can make new mazes to test
by following the pattern from the `mazelist` object which is used in the test
script.

## Simulator Principles

It is interesting to note how the software is designed.
Most importantly, we have separated the agent and the environent.

The intelligent agent should be fully implemented in a Player object.
The `move()` method gives the actions as a function of the percepts
(called the state).  However, since it is an object, the Player can
maintain an internal state to learn over the course of the game.
The internal player state is not necessarily equal to the percept state.

The `Game` class defines the game.  When the game runs in the main
section of the scripts, this class is instantiated, and then a
Player object is passed to the `play()` method.  It is the `Game`
class which tells the agent when to move (act).

The `State` class is used only to pass information from the `Game` to
the Player.

This design makes it easy to implement and test different players while
ensuring that the rules of the game do not change.

## Sample Solution

The file `DFSPlayer.py` contains an implementation of Online DFS.
This file is structured and can be used in the same way as `Template.py`.

