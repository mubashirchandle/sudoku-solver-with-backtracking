from unittest import TestCase, mock

from main import get_puzzle_state_from_user


class TestUserInputValidation(TestCase):
    """Unittests for validating the user input."""

    @mock.patch("main.input", create=True)
    def test_valid_input_1(self, mocked_input):
        mocked_input.side_effect = [
            "0 1 0 4 2 6 8 0 0",
            "0 5 0 0 0 1 0 0 3",
            "0 6 2 3 0 5 4 0 1",
            "6 0 0 5 0 0 2 0 0",
            "1 4 3 2 0 8 9 7 5",
            "0 0 5 0 0 4 0 0 8",
            "5 0 6 1 0 2 7 8 0",
            "2 0 0 9 0 0 0 4 0",
            "0 0 4 6 8 3 0 1 0",
        ]
        expected_output = [
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

        grid = get_puzzle_state_from_user()
        self.assertEqual(grid, expected_output)

    @mock.patch("main.input", create=True)
    def test_valid_input_2(self, mocked_input):
        mocked_input.side_effect = [
            "8 7 9 0 0 0 6 0 0",
            "0 2 0 0 0 9 0 8 0",
            "4 6 0 3 7 8 0 9 0",
            "0 0 4 5 0 2 0 7 0",
            "0 0 5 8 4 7 9 0 0",
            "0 9 0 6 0 3 5 0 0",
            "0 1 0 7 2 6 0 5 9",
            "0 5 0 4 0 0 0 2 0",
            "0 0 2 0 0 0 8 1 6",
        ]
        expected_output = [
            [8, 7, 9, None, None, None, 6, None, None],
            [None, 2, None, None, None, 9, None, 8, None],
            [4, 6, None, 3, 7, 8, None, 9, None],
            [None, None, 4, 5, None, 2, None, 7, None],
            [None, None, 5, 8, 4, 7, 9, None, None],
            [None, 9, None, 6, None, 3, 5, None, None],
            [None, 1, None, 7, 2, 6, None, 5, 9],
            [None, 5, None, 4, None, None, None, 2, None],
            [None, None, 2, None, None, None, 8, 1, 6],
        ]

    @mock.patch("main.input", create=True)
    def test_invalid_input_non_digit_1(self, mocked_input):
        mocked_input.side_effect = [
            "/",
        ]

        grid = get_puzzle_state_from_user()
        self.assertEqual(grid, None)

    @mock.patch("main.input", create=True)
    def test_invalid_input_non_digit_2(self, mocked_input):
        mocked_input.side_effect = ["8 7 9 0 0 0 6 0 0", "a"]

        grid = get_puzzle_state_from_user()
        self.assertEqual(grid, None)

    @mock.patch("main.input", create=True)
    def test_invalid_input_over_range(self, mocked_input):
        mocked_input.side_effect = [
            "8 7 9 0 0 0 6 0 0",
            "0 2 0 0 0 9 0 8 0",
            "4 6 0 3 7 8 0 9 0",
            "0 0 4 5 0 2 0 7 0",
            "0 0 5 8 4 7 9 0 0",
            "0 9 0 6 0 3 5 0 0",
            "0 1 0 7 2 6 0 15 9",
            "0 5 0 4 0 0 0 2 0",
            "0 0 2 0 0 0 8 1 6",
        ]

        grid = get_puzzle_state_from_user()
        self.assertEqual(grid, None)

    @mock.patch("main.input", create=True)
    def test_invalid_input_under_range(self, mocked_input):
        mocked_input.side_effect = [
            "8 7 9 0 0 0 6 0 0",
            "0 2 0 0 0 9 0 8 0",
            "4 6 0 3 7 8 0 9 0",
            "0 0 4 5 0 2 0 7 0",
            "0 0 5 8 4 7 9 0 0",
            "0 9 0 6 0 3 5 0 0",
            "0 1 0 7 2 6 0 5 9",
            "0 5 0 4 0 0 0 -2 0",
            "0 0 2 0 0 0 8 1 6",
        ]

        grid = get_puzzle_state_from_user()
        self.assertEqual(grid, None)
