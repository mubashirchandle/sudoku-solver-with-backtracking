from src.main import solve_grid


def test_solve_grid_easy():
    problem_input = [
        [2, 9, None, None, 3, None, None, 1, None],
        [None, None, None, None, 9, None, 8, None, 2],
        [None, 6, 7, 1, 8, 2, 3, 9, 5],
        [8, None, 4, 9, 7, None, None, None, None],
        [5, 3, 6, None, 4, None, 9, 2, 7],
        [None, None, None, None, 6, 3, 4, None, 8],
        [6, 1, 9, 7, 5, 8, 2, 4, None],
        [3, None, 2, None, 1, None, None, None, None],
        [None, 4, None, None, 2, None, None, 8, 6],
    ]
    expected_output = [
        [2, 9, 8, 5, 3, 6, 7, 1, 4],
        [1, 5, 3, 4, 9, 7, 8, 6, 2],
        [4, 6, 7, 1, 8, 2, 3, 9, 5],
        [8, 2, 4, 9, 7, 5, 6, 3, 1],
        [5, 3, 6, 8, 4, 1, 9, 2, 7],
        [9, 7, 1, 2, 6, 3, 4, 5, 8],
        [6, 1, 9, 7, 5, 8, 2, 4, 3],
        [3, 8, 2, 6, 1, 4, 5, 7, 9],
        [7, 4, 5, 3, 2, 9, 1, 8, 6],
    ]

    solve_grid(problem_input)
    assert problem_input == expected_output


def test_solve_grid_hard():
    problem_input = [
        [None, None, None, None, None, None, 4, 8, None],
        [None, 1, None, 9, None, 4, None, None, 3],
        [None, None, None, None, None, None, 6, None, 7],
        [3, None, None, None, 6, 8, None, 7, None],
        [None, None, None, None, None, None, None, None, None],
        [None, 7, None, 2, 4, None, None, None, 1],
        [8, None, 4, None, None, None, None, None, None],
        [1, None, None, 8, None, 3, None, 4, None],
        [None, 5, 9, None, None, None, None, None, None],
    ]
    expected_output = [
        [5, 2, 3, 6, 7, 1, 4, 8, 9],
        [6, 1, 7, 9, 8, 4, 2, 5, 3],
        [4, 9, 8, 3, 5, 2, 6, 1, 7],
        [3, 4, 5, 1, 6, 8, 9, 7, 2],
        [2, 8, 1, 7, 3, 9, 5, 6, 4],
        [9, 7, 6, 2, 4, 5, 8, 3, 1],
        [8, 3, 4, 5, 2, 7, 1, 9, 6],
        [1, 6, 2, 8, 9, 3, 7, 4, 5],
        [7, 5, 9, 4, 1, 6, 3, 2, 8],
    ]

    solve_grid(problem_input)
    assert problem_input == expected_output
