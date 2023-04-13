#!/usr/bin/env python3

import matplotlib.pyplot as plt
from tqdm import tqdm
from NetworkAgent import Agent

import gymnasium as gym


def evaluate(agent,env,episodes=10,maxsteps=200):
    t_reward = 0.0
    for _ in range(episodes):
        state, _ = env.reset()  
        ep_reward = 0.0
        for _ in range(max_steps):
            action = agent.get_action(env, state) 
            newstate, reward, terminated, _ = env.step(action) 
            ep_reward += reward
            if terminated: break

            state = newstate
        t_reward += ep_reward
    return t_reward/episodes



env = gym.make('FrozenLake-v1', desc=None, map_name="4x4", is_slippery=True,render_mode="array")

done = False
observation, info = env.reset()

action = env.action_space.sample()
observation, reward, terminated, truncated, info = env.step(action)

agent = Agent( env )

for episode in range(500):
    obs, info = env.reset()
    done = False

    # play one episode
    while not done:
        action = agent.get_action(obs)
        next_obs, reward, terminated, truncated, info = env.step(action)

        # update the agent
        agent.update(obs, action, reward, terminated, next_obs)

        # update if the environment is done and the current obs
        done = terminated or truncated
        obs = next_obs

    print( f"{episode}: {reward}" )
    agent.decay_epsilon()

print( agent.getQtable() )

ev = evaluate(agent,env)
print( "Score: ", ev )
