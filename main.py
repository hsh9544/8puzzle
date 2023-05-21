from environment import *
import time
import sys

PROGRESS_BAR_LENGTH = 50

alpha = 0.7     # learning rate
gamma = 0.9     # discount factor
epsilon = 0.1   # exploration rate

episodes = 1000
episode_length = 1000  # zero is infinite

game_board = env()

# initializing Q-table
Q_table = {}
Q_values = [0, 0, 0, 0]  # init values
for state in game_board.state_space:
    Q_table[state] = Q_values[:]

# progress bar
print(f'2. running {episodes} episodes for training...')
print(PROGRESS_BAR_LENGTH*'|', end='')
sys.stdout.write('\r')

# run every episode
for i in range(episodes):

    verbose = False # not printing anything
    exploration = True
    if i+1 == episodes:  # last episode
        verbose = True
        exploration = False
        flag = True

    game_board.reset()
    done = False

    # filling progress bar
    if not i % (episode_length//PROGRESS_BAR_LENGTH):
        print(Full_BLOCK_CHAR, end='', flush=True)

    # run an episode
    counter = 0  # keeps track of episode length
    while 1:

        counter += 1
        if counter == episode_length:
            break

        state = game_board.board

        # prints the final episode
        if verbose:
            if flag:
                print(' DONE!')
                print("3. let's see the result.")
                flag = False

            print()
            print(f'   STATE {counter}')
            game_board.print_board()
            # print(Q_table[state])
            time.sleep(0.2)
            # cs()

        if done:
            break

        # choose action and explore/exploit
        actions: list = Q_table[state]
        Q_based_actions = [i for i, x in enumerate(
            actions) if x == max(actions)]
        Q_based_action = random.choice(Q_based_actions)
        random_action = game_board.random_action()

        if exploration:
            exploration_rate = epsilon
        else:
            exploration_rate = 0

        chance = random.random()
        if chance < exploration_rate:  # explore
            action = random_action
        else:                          # exploit
            action = Q_based_action

        # run an epoch
        new_state, reward, done = game_board.step(action)

        # update Q table
        Q_table[state][action] = (
            1-alpha)*Q_table[state][action] + alpha*(reward + gamma * max(Q_table[new_state]))
        # handling borders
        if reward == rewards[not_valid_move]:
            Q_table[state][action] = -1000
