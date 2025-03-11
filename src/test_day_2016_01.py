import pytest
from day_2016_01 import compute_distance

def test_compute_distance():
    assert compute_distance(['R2', 'L3']) == 5  # 5 blocks away
    assert compute_distance(['R2', 'R2', 'R2']) == 2  # 2 blocks away
    assert compute_distance(['R5', 'L5', 'R5', 'R3']) == 12  # 12 blocks away
    assert compute_distance([]) == 0  # No movement, distance = 0
    assert compute_distance(['R5']) == 5  # Moving only east
