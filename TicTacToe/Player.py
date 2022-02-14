
import TicTacToe as ttt

import sys

class Player:
    def __init__(self):
        self.dict = {}
    def get(self,s):
        return self.dict.get(s.key())
    def put(self,state):
        self.dict[state.key()] = state
    def move(self,state):
        s = self.get(state)
        if s == None:
            s = self.minimax(state)
        m = s.getMove()
        return m
    def minimax(self,state):
        root = self.get(state)
        if root == None:
          root = PState(state)
          w = root.isWin()
          player = root.toMove()
          if player == None:
              root.value = ttt.getvalue(w)
          elif w == None:
              target = ttt.getvalue(player)
              mlist =  root.moves()
              nlist = []
              if mlist == []:
                  root.value = 0
              for m in mlist:
                 b = root.moveCopy(m)
                 node = self.minimax(b)
                 root.addchild(m,node)
                 nlist.append( ( m,node,node.value ) )
              bestmove = max(nlist,key=lambda x : target*x[2] )
              (root.move,t,root.value) = bestmove
          else:
              root.value = ttt.getvalue(w)
        print("value",root.value,file=sys.stderr)
        return root


class PState:
    def __init__(self,state):
        self.state = state
        self.child = {}
        self.value = None
        self.move = None
    def moveCopy(self,m):
        return self.state.moveCopy(m)
    def getMove(self):
        return self.move
    def addchild(self,m,s):
        self.child[m] = s
    def isWin(self):
        return self.state.isWin()
    def getArray(self):
        return self.state.getArray()
    def key(self):
        return self.state.key()
    def toMove(self):
        return self.state.toMove()
    def moves(self):
        return self.state.moves()
