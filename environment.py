from utils import *
import numpy as np
from itertools import permutations as perms
import random

# m is moon, s is sun, and b is blank
s = 'sun'
m = 'moon'
b = 'blank'

# initial state
#################
#   s   s   s   #
#   m   s   m   #
#   m   b   m   #
#################
init_state = (s, s, s, m, s, m, m, b, m)

# desired state
#################
#   b   m   s   #
#   m   s   m   #
#   s   m   s   #
#################
final_state = (b, m, s, m, s, m, s, m, s)

# actions as in polar coordination
# we use these as array index
right = 0
up = 1
left = 2
down = 3
actions = [right, up, left, down]

# rewards
not_valid_move = 'nvm'
reached_goal_state = 'rgs'
valid_move_penalty = 'vmp'

rewards = {
    not_valid_move: -1000,
    reached_goal_state: 100,
    valid_move_penalty: -10
}


class env:
    def __init__(self) -> None:
        self.reset()
        print('1. initializing state space... ', end='')
        self.init_state_space()
        print('DONE!')
        # REWARD TABLE (NOT USEFUL FOR THIS CASE)
        # print('initializing reward table... ', end='', flush=True)
        # self.init_reward_table()
        # print('DONE!')
        # for key, val in self.reward_table.items():
        #     print(key, val)

    def reset(self):
        self.board = init_state

    def init_state_space(self):
        self.state_space = list(perms(init_state))
        return 1

	# not used
    def init_reward_table(self):
        self.reward_table = {}
        for state in self.state_space:
            state_actions_reward = []
            for action in actions:
                if self.is_valid(state, action):
                    reward = rewards[valid_move_penalty]
                else:
                    reward = rewards[not_valid_move]
                state_actions_reward.append(reward)

            self.reward_table[state] = state_actions_reward

    def is_valid(self, state, action):
        try:
            _ = self.take_action(state, action)
        except:
            return False
        return True

    def take_action(self, state, action):
        state = convert_to_2d(state)
        if action == right:
            move = (0, 1)
        if action == up:
            move = (-1, 0)
        if action == left:
            move = (0, -1)
        if action == down:
            move = (1, 0)

        blank_location = np.where(state == b)
        i1 = blank_location[0][0]
        j1 = blank_location[1][0]

        i2, j2 = i1+move[0], j1+move[1]
        if i2 < 0 or j2 < 0:
            raise IndexError
        state[i1][j1], state[i2][j2] = state[i2][j2], state[i1][j1]
        return tuple(convert_to_1d(state))

    def step(self, action):
        old_state = self.board
        try:
            new_state = self.take_action(old_state, action)
            self.board = new_state
            if new_state == final_state:
                reward = rewards[reached_goal_state]
                done = True
            else:
                # reward = self.reward_table[old_state][action]
                reward = rewards[valid_move_penalty]
                done = False
        except:
            reward = rewards[not_valid_move]
            done = False
        finally:
            return (self.board, reward, done)
        # return (percept, reward, done, info)

    def print_board(self):
        ''' do not try to read this funcion'''
        char_mapping = {
            m: MOON_CHAR,
            s: SUN_CHAR,
            b: BLANK_CHAR
        }

        board = convert_to_2d(self.board)
        print(ul, 3*h, hd, 3*h, hd, 3*h, ur, sep='')  # upper border
        for i in range(3):
            for j in range(3):
                print(v, ' ', char_mapping[board[i][j]],
                      ' ', sep='', end='')  # cells
            print(v)
            if i != 2:
                print(vr, 3*h, cross, 3*h, cross, 3*h,
                      vl, sep='')  # middle horizontal
        print(ll, 3*h, hu, 3*h, hu, 3*h, lr, sep='')  # lower border

    def encode(self, state):
        return self.state_space.index(state)
        # return index state in state space
        pass

    def random_action(self):
        return random.choice(actions)

    def swap_cell(self, loc1, loc2):
        i1, j1 = loc1
        i2, j2 = loc2
        self.board[i1][j1], self.board[i2][j2] = self.board[i2][j2], self.board[i1][j1]
