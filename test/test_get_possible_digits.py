import pytest
from src.main import get_possible_digits


@pytest.mark.parametrize(
    "row, col, expected", [(0, 0, [3, 7, 9]), (1, 1, [5])],
)
def test_get_possible_digits(row, col, expected):
    grid = [
        [None, 1, None, 4, 2, 6, 8, None, None],
        [None, 5, None, None, None, 1, None, None, 3],
        [None, 6, 2, 3, None, 5, 4, None, 1],
        [6, None, None, 5, None, None, 2, None, None],
        [1, 4, 3, 2, None, 8, 9, 7, 5],
        [None, None, 5, None, None, 4, None, None, 8],
        [5, None, 6, 1, None, 2, 7, 8, None],
        [2, None, None, 9, None, None, None, 4, None],
        [None, None, 4, 6, 8, 3, None, 1, None],
    ]

    possibilities = get_possible_digits(grid, row, col)

    if expected is None:
        assert possibilities is None
    else:
        assert possibilities == expected
