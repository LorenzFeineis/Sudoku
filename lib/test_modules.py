import pytest
from brute_force_solver import brute_force_sudoku_solver
import consistency
import numpy as np

def test_sudoku_generation():

    """Test generation of a sudoku with brute force."""
    empty_sudoku = np.array([[0 for i in range(9)] for i in range(9)])
    new_sudoku = brute_force_sudoku_solver(empty_sudoku)
    
    assert type(new_sudoku) == np.ndarray
    consistency.check_global_consistency(new_sudoku)

def test_consistency_functions():

    inconsistent_sudoku = np.array([ [i+1 for i in range(9)] for j in range(9)])

    with pytest.raises(ValueError):
        consistency.check_blocks(inconsistent_sudoku)
        consistency.check_local_consistecy(inconsistent_sudoku)
        consistency.check_rows(inconsistent_sudoku)
        consistency.check_global_consistency(inconsistent_sudoku)