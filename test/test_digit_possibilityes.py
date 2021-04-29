from unittest import TestCase, mock

from main import get_possible_digits


class TestDigitPossibilities(TestCase):
    """Unittests for validating the user input."""

    def test_possible_digits(self):
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

        possibilities = get_possible_digits(grid, 0, 0)
        self.assertEqual(possibilities, [3, 7, 9])
