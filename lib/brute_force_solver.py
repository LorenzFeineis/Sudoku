"""
Define global variables for this project.
"""
from typing import List, Tuple


import random
import numpy as np
import sys
sys.setrecursionlimit(10000)

class Step():
    def __init__(self,
    sudoku: np.ndarray,
    current_coordinate: Tuple[int,int],
    current_value: int,
    available_values: List[int]):
        self.sudoku=sudoku
        self.current_coordinate = current_coordinate
        self.current_value=current_value
        self.available_values = available_values



def brute_force_sudoku_solver(sudoku:np.ndarray, steps: List[Step]=[]) ->np.ndarray:
    """Solve a sudoku using brute force."""
    # Search the first field with value 0
    # previous_steps = [(last_field, last_value)]
    next_coordinate = None
    for i in range(9):
        if next_coordinate:
            break
        for j in range(9):
            if sudoku[i, j] == 0:
                next_coordinate = (i, j)
                break

    # If there is no field with value 0 return the solved sudoku
    if not next_coordinate:
        return sudoku

    if not consistency_check(sudoku):
        # inconsistency detected
        # Go back to the last branch and remember this inconsistency

        while len(steps[-1].available_values) == 1:
            steps.pop(-1)
        last_step = steps.pop(-1)
        new_available_values =  last_step.available_values
        new_available_values.remove(last_step.current_value)
        new_value = random.choice(new_available_values)
        new_sudoku = last_step.sudoku.copy()
        new_sudoku[last_step.current_coordinate] = new_value

        next_step = Step(new_sudoku, last_step.current_coordinate, new_value, new_available_values)
        steps.append(next_step)


    else:
        # Assign to field a value from available_values
        # and continue the recursion
        available_values = possible_values_for_field(sudoku, next_coordinate)
        new_sudoku = sudoku.copy()
        value = random.choice(available_values)
        new_sudoku[next_coordinate] = value
        step = Step(sudoku, next_coordinate, value, available_values)
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



def create_new_sudoku():

    empty_sudoku = np.array([[0 for i in range(9)] for i in range(9)])
    new_sudoku = brute_force_sudoku_solver(empty_sudoku)
    print(new_sudoku)

if __name__=='__main__':
    create_new_sudoku()