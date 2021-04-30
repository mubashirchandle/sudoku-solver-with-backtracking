import pytest
from src.main import get_puzzle_state_from_user


def test_get_puzzle_state_from_user_valid(monkeypatch):
    user_input = iter(
        [
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
    )
    monkeypatch.setattr("builtins.input", lambda _="": next(user_input))

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

    assert get_puzzle_state_from_user() == expected_output


def test_get_puzzle_state_from_user_invalid_non_digit(monkeypatch):
    user_input = iter(
        [
            "0 1 0 4 2 6 8 0 0",
            "0 5 0 0 0 1 0 0 3",
            "0 6 2 3 0 a 4 0 1",
            "6 0 0 5 0 0 2 0 0",
            "1 4 3 2 0 8 9 7 5",
            "0 0 5 0 0 4 0 0 8",
            "5 0 6 1 0 2 7 8 0",
            "2 0 0 9 0 0 0 4 0",
            "0 0 4 6 8 3 0 1 0",
        ]
    )
    monkeypatch.setattr("builtins.input", lambda _="": next(user_input))

    assert get_puzzle_state_from_user() == None


@pytest.mark.parametrize(
    "user_input", ["0 1 0 4 2 6 8 0", "", "0 1 0 4 2 6 8 0 9 8",],
)
def test_get_puzzle_state_from_user_invalid_length(user_input, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _="": user_input)

    result = get_puzzle_state_from_user()
    assert result is None


def test_get_puzzle_state_from_user_valid_whitespace(monkeypatch):
    user_input = iter(
        [
            "  0 1 0 4 2 6 8 0 0",
            "0 5 0 0 0 1 0 0 3   ",
            "0 6 2 3 0 5 4     0 1",
            "6 0           0 5 0 0 2 0 0",
            "1 4 3 2 0 8 9    7 5",
            "0 0 5 0 0 4 0 0 8",
            "5 0 6 1 0 2 7 8 0",
            "2 0 0 9 0 0 0 4 0",
            "0 0 4 6 8 3 0 1 0",
        ]
    )

    monkeypatch.setattr("builtins.input", lambda _="": next(user_input))

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

    result = get_puzzle_state_from_user()
    assert result == expected_output
