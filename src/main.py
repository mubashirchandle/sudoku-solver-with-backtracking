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
    for _ in range(9):
        row = input()
        try:
            digits = list(map(int, row.split()))
        except ValueError:
            return None

        if len(digits) < 9 or len(digits) > 9:
            return None
        for digit in digits:
            if digit > 9 or digit < 0:
                return None

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
        if i != col and grid[row][i] == digit:
            return False
        if i != row and grid[i][col] == digit:
            return False

    # Temporarily write some random value at the cell.
    old_value = grid[row][col]
    grid[row][col] = 0

    sub_square = grid[(row // 3) * 3 : (row // 3) * 3 + 3]
    sub_square = [x[(col // 3) * 3 : (col // 3) * 3 + 3] for x in sub_square]
    sub_square = [digit for x in sub_square for digit in x]

    if digit in sub_square:
        grid[row][col] = old_value  # Write the original value back.
        return False

    grid[row][col] = old_value  # Write the original value back.
    return True


def get_possible_digits(grid, row, col):
    """
    Returns a list of all the possible digits that can be placed in the given
    row and col.
    """
    # Only empty cells call be filled.
    if grid[row][col] is not None:
        return [grid[row][col]]

    possible_digits = []
    for digit in range(1, 10):
        if is_digit_placement_valid(grid, digit, row, col):
            possible_digits.append(digit)
    return possible_digits


def is_solved(grid):
    """Returns True if the given grid is solved correctly, False otherwise."""
    for row in range(9):
        for col in range(9):
            digit = grid[row][col]
            if digit is None:
                return False
            if not is_digit_placement_valid(grid, digit, row, col):
                return False

    return True


def has_empty_cells(grid):
    """Returns True if there is at least one empty cell in the given grid."""
    for row in range(9):
        for col in range(9):
            if grid[row][col] is None:
                return True

    return False


def get_all_possible_digits(grid):
    possibilities = {}
    for row in range(9):
        for col in range(9):
            possibilities[(row, col)] = get_possible_digits(grid, row, col)

    return possibilities


def solve_grid(grid):
    if is_solved(grid):
        return grid
    if not has_empty_cells(grid):
        raise ValueError(
            "The grid is not solved and also does not have any empty cells"
        )

    found = False
    i = 0
    while not found and i < 9:
        j = 0
        while not found and j < 9:
            if grid[i][j] is None:
                row = i
                col = j
                found = True
            j += 1
        i += 1

    digits = get_possible_digits(grid, row, col)

    for digit in digits:
        grid[row][col] = digit

        solve_grid(grid)
        if is_solved(grid):
            break

        grid[row][col] = None

    return grid


if __name__ == "__main__":
    user_grid = get_puzzle_state_from_user()

    if not user_grid:
        print("Invalid input detected.")
    else:
        print_grid(user_grid)

        print("\n\n")
        print("-" * 41)
        print("Solved Grid:")

        solve_grid(user_grid)
        print_grid(user_grid)
