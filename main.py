"""
Use backtracking approach to solve Sudoku puzzles.
"""


def get_puzzle_state_from_user():
    """
    Prompts the user to enter their puzzle and returns it in a list.

    Returns
    -------
    grid (list<list<int>>): A list of list of ints with each sub-list denoting
                            a row.
    """
    print("Please enter your puzzle state.")
    print("Enter the digits in a row-wise fashion with each digit separated")
    print("by a single space. For empty squares, use 0.")
    print()
    grid = []
    for i in range(9):
        row = input()
        try:
            digits = list(map(int, row.split()))
        except ValueError:
            return

        if len(digits) < 9:
            return
        for digit in digits:
            if digit > 9 or digit < 0:
                return

        digits = [digit if digit != 0 else None for digit in digits]
        grid.append(digits)

    return grid


if __name__ == "__main__":
    grid = get_puzzle_state_from_user()

    if not grid:
        print("Invalid input detected.")
    else:
        for row in grid:
            print(row)
