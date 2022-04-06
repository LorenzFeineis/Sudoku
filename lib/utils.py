"""
UTILS.

Define global variables for this project.
"""
import random
import numpy as np
import sys
sys.setrecursionlimit(10000)


def main():
    """Test generation of a sudoku with brute force."""
    empty_sudoku = np.array([[0 for i in range(9)] for i in range(9)])
    print(brute_force_sudoku_solver(empty_sudoku))


def brute_force_sudoku_solver(sudoku, steps=[]):
    """Solve a sudoku using brute force."""
    # Search the first field with value 0
    # previous_steps = [(last_field, last_value)]
    field = 0
    for i in range(9):
        if field:
            break
        for j in range(9):
            if sudoku[i, j] == 0:
                field = (i, j)
                break

    # If there is no field with value 0 return the solved sudoku
    if not field:
        return sudoku

    if not consistency_check(sudoku):
        # inconsistency detected
        # Go back to the last branch and remember this inconsistency

        while len(steps[-1][3]) == 1:
            steps.pop(-1)
        sudoku, field, value, available_values = steps.pop(-1)
        available_values.remove(value)
        value = random.choice(available_values)
        new_sudoku = sudoku.copy()
        new_sudoku[field] = value
        step = (sudoku, field, value, available_values)
        steps.append(step)
    else:
        # Assign to field a value from available_values
        # and continue the recursion
        available_values = possible_values_for_field(sudoku, field)
        new_sudoku = sudoku.copy()
        value = random.choice(available_values)
        new_sudoku[field] = value
        step = (sudoku, field, value, available_values)
        steps.append(step)
    return brute_force_sudoku_solver(new_sudoku, steps)


def possible_values_for_field(sudoku, field=(0, 0)):
    """Return a list of all possible values for the sudoku[field]."""
    if sudoku[field] != 0:
        return []

    row, column = field
    current_block = sudoku[3 * (row//3)    : 3 + 3 * (row//3),
                           3 * (column//3) : 3 + 3 * (column//3)]

    not_available_values = []
    available_values = list(range(1, 10))
    for i in range(9):
        if sudoku[row, i] != 0:
            not_available_values.append(sudoku[row, i])

        if sudoku[i, column] != 0:
            not_available_values.append(sudoku[i, column])

        if current_block.flatten()[i] != 0:
            not_available_values.append(current_block.flatten()[i])

    for value in list(range(1, 10)):
        if value in not_available_values:
            available_values.remove(value)

    return available_values


def possible_values_per_field(sudoku):
    """Return a nested list with the available values for each field."""
    return [[possible_values_for_field(sudoku, (i, j)) for i in range(9)]
            for j in range(9)]


def consistency_check(sudoku):
    """Check if an unassigned field exists with no available value."""
    for i in range(9):
        for j in range(9):
            if sudoku[i, j] == 0:
                if len(possible_values_for_field(sudoku, (i, j))) == 0:
                    return False
    return True


if __name__ == '__main__':
    main()
