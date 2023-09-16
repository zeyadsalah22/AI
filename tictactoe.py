"""
Tic Tac Toe Player
"""
import copy
import math

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
    cx = 0
    co = 0
    c = 0
    for q in range(3):
        for p in range(3):
            if board[q][p] == X:
                cx += 1
            elif board[q][p] == O:
                co += 1
            else:
                c += 1
    if cx > co:
        return O
    else:
        return X
    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actionss = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actionss.add((i, j))
    return actionss

    # raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_copy = copy.deepcopy(board)
    if action not in actions(board):
        raise Exception('invalid action')
    else:
        board_copy[action[0]][action[1]] = player(board)
        return board_copy
    # raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for w in range(3):
        cx = 0
        co = 0
        for t in board[w]:
            if t == X:
                cx += 1
            elif t == O:
                co += 1
        if cx == 3:
            return X
        elif co == 3:
            return O
        cx = 0
        co = 0
        for u in range(3):
            if board[u][w] == X:
                cx += 1
            elif board[u][w] == O:
                co += 1
        if cx == 3:
            return X
        elif co == 3:
            return O
    if board[0][0] == board[1][1] == board[2][2] == X or board[0][2] == board[1][1] == board[2][0] == X:
        return X
    elif board[0][0] == board[1][1] == board[2][2] == O or board[0][2] == board[1][1] == board[2][0] == O:
        return O
    else:
        return None
    # raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        return True
    else:
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    return False
        return True
    # raise NotImplementedError


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
    # raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    elif player(board) == X:
        plays = []
        # board = result(board,action)
        for action in actions(board):
            # if min_value(result(board,action))==1:
            #   return action
            # elif min_value(result(board,action))==0:
            # z = action
            # return z
            plays.append([min_value(result(board, action)), action])
        return sorted(plays, key=lambda x: x[0], reverse=True)[0][1]
    elif player(board) == O:
        plays = []
        # board = result(board, action)
        for action in actions(board):
            #   if max_value(result(board, action)) == -1:
            #      return action
            # elif max_value(result(board, action)) == 0:
            #    z = action
            # return z
            plays.append([max_value(result(board, action)), action])
        return sorted(plays, key=lambda x: x[0])[0][1]


def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for actiion in actions(board):
        v = max(v, min_value(result(board, actiion)))
    return v


def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for actioon in actions(board):
        v = min(v, max_value(result(board, actioon)))
    return v
