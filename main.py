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


def print_grid(grid):
    """Prints the puzzle grid in a beautiful manner."""
    print("-" * 13 + " " + "-" * 13 + " " + "-" * 13)
    for i, row in enumerate(grid, 1):
        print("|", end=" ")
        for j, digit in enumerate(row, 1):
            if digit is None:
                print(" ", end=" |")
            else:
                print(digit, end=" |")
            if j < 9 and j % 3 == 0:
                print(" | ", end="")
            else:
                print(" ", end="")
        print()
        print("-" * 13 + " " + "-" * 13 + " " + "-" * 13)
        if i < 9 and i % 3 == 0:
            print("-" * 13 + " " + "-" * 13 + " " + "-" * 13)


if __name__ == "__main__":
    grid = get_puzzle_state_from_user()

    if not grid:
        print("Invalid input detected.")
    else:
        print_grid(grid)
