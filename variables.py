""" Common variables (global) """
import numpy as np

INITIAL_GAME_STATE = np.array(
    [['_', '_', '_'],
     ['_', '_', '_'],
     ['_', '_', '_']])

# store game_field in global variable
game_field = INITIAL_GAME_STATE.copy()

# history of moves
game_moves = []
