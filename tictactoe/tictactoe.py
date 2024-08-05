"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None

# Counter for determining player turn
Counter = 0


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board, num=0):
    """
    Returns player who has the next turn on a board.
    """
    counter_x = 0
    counter_o = 0

    for i in range(len(board)):
        counter_x += board[i].count("X")
        counter_o += board[i].count("O")

    if counter_x == counter_o:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    # First check and return None if the game has ended
    if terminal(board):
        return None

    moves = set()

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                moves.add((i, j))
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    row, col = action

    # Creating a deepcopy of the copy so AI can make different independent boards
    new_board = copy.deepcopy(board)

    # Check if the action is valid
    if new_board[row][col] != EMPTY:
        raise Exception("Invalid Move")

    new_board[row][col] = player(board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    new_board = copy.deepcopy(board)
    n = len(board[0])

    for row in board:
        if len(set(row)) == 1:
            return row[0]

    for i in range(len(board)):
        vertical_checker = [board[j][i] for j in range(n)]

        if len(set(vertical_checker)) == 1:
            return vertical_checker[0]
        else:
            vertical_checker = []

    right_diagonal = [board[i][i] for i in range(n)]
    if len(set(right_diagonal)) == 1:
        return right_diagonal[0]

    left_diagonal = [board[n - 1 - i][i] for i in range(n - 1, -1, -1)]
    if len(set(left_diagonal)) == 1:
        return left_diagonal[0]

    return False


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    elif any(EMPTY in line for line in board):
        return False
    else:
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # Check who's move it is
    turn = winner(board)

    if turn == X:
        return 1
    elif turn == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # First check if center of board is free and play that card.
    # Create a dict object to store all actions and their values
    # max_score and min_score are used to optimize the number of actions minimax goes through.
    # steps is used to track the number of steps taken to achieve a goal.

    if board[1][1] == EMPTY:
        return (1, 1)
    checker = {}
    max_score = math.inf
    min_score = -math.inf
    steps = 0

    if player(board) == X:

        for action in actions(board):

            # Collects all the low response value of O player into checker dictionary
            new_steps, min_score = min_value(result(board, action), min_score, steps)
            if new_steps == 0 and min_score == 1:
                return action
            checker[new_steps] = [min_score, action]

        # Selects the maximum action among the low response values of O player
        return checker[max(checker)][1]

    else:

        for action in actions(board):

            # Collects all the high response value of X player into checker dictionary as {checker: action}
            new_steps, max_score = max_value(result(board, action), max_score, steps)
            if new_steps == 0 and min_score == -1:
                return action

            checker[new_steps] = [max_score, action]

        # Selects the minimum action among the high response values of O player
        return checker[min(checker)][1]


def max_value(board, max_score, steps):
    if terminal(board):
        return [steps, utility(board)]

    v = -math.inf
    steps += 1

    for action in actions(board):
        steps, boo = min_value(result(board, action), max_score, steps)
        v = max(v, boo)
        if v >= max_score:
            return [steps, v]

    return [steps, v]


def min_value(board, min_score, steps):

    if terminal(board):
        return [steps, utility(board)]

    v = math.inf
    steps += 1

    for action in actions(board):
        steps, boo = max_value(result(board, action), min_score, steps)
        v = min(v, boo)
        if v <= min_score:
            return [steps, v]

    return [steps, v]
