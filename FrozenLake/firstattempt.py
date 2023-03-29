#!/usr/bin/env python3

import gymnasium as gym
import time
env = gym.make('FrozenLake-v1', desc=None, map_name="4x4", is_slippery=True,render_mode="human")
env.reset()

state, info = env.reset()
print( "State ", state )
print( "Info ", info )

done = False
utilities = [0.41,0.38,0.35,0.34,0.43,0,0.12,0,0.45,0.48,0.43,0,0,0.59,0.71,1]
reward = 0

def expected(s,a):
    r = s
    if a == 0:
        if s%4 > 0: r -= 1
    elif a == 1:
        if s < 12: r += 4
    elif a == 2:
        if s%4 < 3: r += 1
    elif a == 3:
        if s > 3: r -= 4
    return r

while not done:
    actionlist = range(4)
    newstates = [ expected( state, a ) for a in actionlist ]
    newutility = [ utilities[s] for s in newstates ]
    print(newstates)
    print(newutility)

    maxval = max( newutility )
    action = newutility.index(maxval)
    newstate = newstates[action]

    print( f"State {state} [{utilities[state]}] -> {newstates[action]} [{utilities[newstate]}] ({action}); reward {reward}" )

    state, reward, terminated, truncated, info = env.step(action)

    done = terminated or truncated

    time.sleep(1)

