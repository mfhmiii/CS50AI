"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    Xcount = 0
    Ocount = 0

    for row in board:
        Xcount += row.count(X)
        Ocount += row.count(O)

    if Xcount <= Ocount:
        return X
    else:
        return O

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    possible_actions = set()
    playerTurn = player(board)

    for row_index, row in enumerate(board):
        for col_index, col in enumerate(row):
            if col == EMPTY:
                possible_actions.add((row_index, col_index))

    return possible_actions

    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    if action not in actions(board):
        raise Exception("Invalid move")

    row_index, col_index = action
    board_copy = copy.deepcopy(board)
    board_copy[row_index][col_index] = player(board)
    return board_copy

    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for player in (X, O) :

        # Check horizontal
        for row in board:
            if row.count(X) == 3 or row.count(O) == 3:
                return player

        # Check vertical
        for col_index in range(3):
            if board[0][col_index] == player and board[1][col_index] == player and board[2][col_index] == player:
                return player

        # Check diagonal
        if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            return player
        if board[0][2] == player and board[1][1] == player and board[2][0] == player:
            return player
    
    return None

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) != None:
        return True

    for row in board:
        if EMPTY in row:
            return False

    return True

    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    # max_val function
    def max_val(board) :
        optimal_move = ()

        if terminal(board):
            return utility(board), optimal_move
        else :
            v = -math.inf
            for action in actions(board):
                v2, _ = min_val(result(board, action))
                if v2 > v :
                    v = v2
                    optimal_move = action
            return v, optimal_move
    
    # min_val function
    def min_val(board) :
        optimal_move = ()
        if terminal(board):
            return utility(board), optimal_move
        else :
            v = math.inf
            for action in actions(board):
                v2, _ = max_val(result(board, action))
                if v2 < v :
                    v = v2
                    optimal_move = action
            return v, optimal_move

    # Optimize the move
    current_player = player(board)
    best_move = None
    
    if current_player == X:
        best_value = -math.inf
        for action in actions(board):
            value, _ = min_val(result(board, action))
            if value > best_value:
                best_value = value
                best_move = action
    else:
        best_value = math.inf
        for action in actions(board):
            value, _ = max_val(result(board, action))
            if value < best_value:
                best_value = value
                best_move = action
    
    return best_move
