import gym
import universe

env = gym.make('flashgames.DuskDrive-v0')
env.configure(remotes='vnc://localhost:5900+15900')  # automatically creates a local docker container
observation_n = env.reset()

while True:
    action_n = [[('KeyEvent', 'ArrowUp', True)] for ob in observation_n]  # your agent here
    observation_n, reward_n, done_n, info = env.step(action_n)
    env.render()
