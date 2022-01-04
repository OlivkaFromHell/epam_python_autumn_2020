import pytest
from hw.hw3 import tic_tac_toe_checker

boards_x_win = [[['x', 'x', 'x'],
                 ['x', 'o', 'o'],
                 ['o', 'o', 'x']],

                [['x', 'o', 'o'],
                 ['x', 'x', 'x'],
                 ['o', 'o', 'x']],

                [['o', 'x', 'o'],
                 ['x', 'o', 'o'],
                 ['x', 'x', 'x']],

                [['x', 'x', 'o'],
                 ['x', 'o', 'o'],
                 ['x', 'o', 'x']],

                [['x', 'x', 'o'],
                 ['o', 'x', 'o'],
                 ['o', 'x', 'x']],

                [['o', 'x', 'x'],
                 ['x', 'o', 'x'],
                 ['o', 'o', 'x']],

                [['x', 'x', 'o'],
                 ['o', 'x', 'o'],
                 ['x', 'o', 'x']],

                [['-', '-', 'x'],
                 ['-', 'x', '-'],
                 ['x', 'o', 'o']],
                ]

boards_o_win = [[['x', 'x', 'o'],
                 ['x', 'o', 'o'],
                 ['o', 'x', 'x']],

                [['x', 'x', 'o'],
                 ['o', '-', 'o'],
                 ['x', 'x', 'o']],

                [['o', 'x', 'x'],
                 ['x', 'o', '-'],
                 ['x', 'o', 'o']],
                ]

boards_unfinished = [[['-', '-', '-'],
                      ['-', '-', '-'],
                      ['-', '-', '-']],

                     [['x', '-', '-'],
                      ['o', 'x', '-'],
                      ['o', '-', '-']],

                     [['o', 'x', 'x'],
                      ['-', '-', '-'],
                      ['x', 'o', 'o']],
                     ]

boards_draw = [[['x', 'o', 'x'],
                ['x', 'o', 'o'],
                ['o', 'x', 'x']],

               [['x', 'x', 'o'],
                ['o', 'o', 'x'],
                ['x', 'x', 'o']],

               [['o', 'x', 'x'],
                ['x', 'o', 'o'],
                ['x', 'o', 'x']],
               ]


@pytest.mark.parametrize('board', [*boards_x_win])
def test_x_win_case(board):
    assert tic_tac_toe_checker(board) == 'x wins!'


@pytest.mark.parametrize('board', [*boards_o_win])
def test_o_win_case(board):
    assert tic_tac_toe_checker(board) == 'o wins!'


@pytest.mark.parametrize('board', [*boards_unfinished])
def test_unfinished_case(board):
    assert tic_tac_toe_checker(board) == 'unfinished!'


@pytest.mark.parametrize('board', [*boards_draw])
def test_draw_case(board):
    assert tic_tac_toe_checker(board) == 'draw!'
