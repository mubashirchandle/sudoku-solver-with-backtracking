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


def is_digit_placement_valid(grid, digit, row, col):
    """Checks if the digit can be placed in the given row and col."""

    for i in range(9):
        if grid[row][i] == digit:
            return False
        if grid[i][col] == digit:
            return False

    sub_square = grid[(row // 3) * 3 : (row // 3) * 3 + 3]
    sub_square = [x[(col // 3) * 3 : (col // 3) * 3 + 3] for x in sub_square]
    sub_square = [digit for x in sub_square for digit in x]

    if digit in sub_square:
        return False

    return True


def get_possible_digits(grid, row, col):
    """
    Returns a list of all the possible digits that can be placed in the given
    row and col.
    """
    possible_digits = []
    for digit in range(1, 10):
        if is_digit_placement_valid(grid, digit, row, col):
            possible_digits.append(digit)
    return possible_digits


if __name__ == "__main__":
    grid = get_puzzle_state_from_user()

    if not grid:
        print("Invalid input detected.")
    else:
        print_grid(grid)

        for row in range(9):
            print(f"Row #{row + 1}")
            for col in range(9):
                if grid[row][col] is not None:
                    continue

                print(f"\tCol #{col + 1}: ", end="")
                print(get_possible_digits(grid, row, col))
