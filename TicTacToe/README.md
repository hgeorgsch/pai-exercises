# An Intelligent Agent to play Tic Tac Toe

Your task is to implement a robot player for tic tac toe.

# The Template

The file `Template.py` implements a random agent, making moves
uniformly at random.  You can use this as a template for your 
solution.

The file defines a class `Player` with a method `move(state)`,
which takes a `State` object and returns the $(x,y)$ coordinate
for the next mark to be placed on the board.  
The reason for implementing the playe as a class, and not just
a function, is to calculate an optimal strategy when making the
first move, and the caching these calculations.

The `State` object is defined in the file `TicTacToe.py`.
The most important methods are documented, and you can access
this within ipython.

```
In [1]: import TicTacToe

In [2]: help(TicTacToe.State)
```

The most important methods from you are going to be `moves()`
(as shown in the template) and `getArray()` to get an array
representation of the current board.

# Testing the Game

Three scripts have been provided to play the game.
Firstly, `ttt.py` plays the Template player against itself.
Secondly, `ttt1.py` and `ttt2.py` plays the Template player against
a more intelligent player implemented in `Player.py`, respectively as
second and first player.

# Sample Solution

You can use `Player.py` as a sample solution.  It is not documented,
and it may be a challenging, but fruitful, exercise to work out how
it works.
