"""
Consistency check.

This module contains functions to check if a sudoku is consistent.
"""
import numpy as np


def check_global_consistency(sudoku):
    """Check for any inconsistencies in the sudoku."""
    if not check_rows(sudoku):
        return False
    if not check_rows(sudoku.T):
        return False
    if not check_blocks(sudoku):
        return False

    return True


def check_rows(sudoku):
    """Check for any inconsistencies in the rows of the sudoku."""
    for i in range(9):
        if not check_local_consistecy(sudoku[i, :]):
            return False
    return True


def check_blocks(sudoku):
    """Check for any inconsistenciesin the 3x3 blocks of the sudoku."""
    for i in (0, 3, 6):
        for j in (0, 3, 6):
            if not check_local_consistecy(sudoku[i:i+3, j:j+3]):
                return False
    return True


def check_local_consistecy(block):
    """Check if every number appears in list at most once."""
    if isinstance(block, np.ndarray):
        block = list(block.flatten())

    for i in range(1, 10):
        if block.count(i) > 1:
            return False
    return True
