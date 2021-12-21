"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"

Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"

    [[-, -, o],
     [-, o, o],
     [x, x, x]]

     Return value should be "x wins!"

"""
from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    def is_player_win(board: List[List], player: str):
        n = len(board)

        # check rows
        for i in range(n):
            win = True
            for j in range(n):
                if board[i][j] != player:
                    win = False
                    break
            if win:
                return True

        # check columns
        for i in range(n):
            win = True
            for j in range(n):
                if board[j][i] != player:
                    win = False
                    break
            if win:
                return True

        # check main diagonal
        win = True
        for i in range(n):
            if board[i][i] != player:
                win = False
                break

        if win:
            return True

        # check side diagonal
        win = True
        for i in range(n):
            if board[i][n - i - 1] != player:
                win = False
                break

        if win:
            return True

    if is_player_win(board, 'x'):
        return 'x wins!'
    if is_player_win(board, 'o'):
        return 'o wins!'
    else:
        if '-' in [i for j in board for i in j]:
            return 'unfinished!'

    return 'draw!'


if __name__ == '__main__':
    print(tic_tac_toe_checker([['o', 'x', 'o'],
                               ['x', 'x', 'o'],
                               ['x', 'o', 'x']]))
