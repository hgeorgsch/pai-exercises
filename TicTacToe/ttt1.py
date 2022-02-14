#! /usr/bin/env python3

import TicTacToe as ttt
from Player import Player 
from Template import Player as TPlayer

g = ttt.Game()
g.play(Player(),TPlayer())
