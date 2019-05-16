"""
Tests for geom_analysis.py
"""

import geom_analysis as ga
import pytest

def test_calculate_distance():
    coord1 = [0, 0, 2]
    coord2 = [0, 0, 0]

    observed = ga.calculate_distance(coord1, coord2)

    assert observed == 2

def test_bond_check_true():
    bond1 = 0.9
    minimum_value = 0
    maximum_value = 1.5

    observed = ga.bond_check(bond1, minimum_value, maximum_value)

    assert observed == True

def test_bond_check_false():
    bond1 = 17.0
    minimum_value = 0
    maximum_value = 1.5

    observed = ga.bond_check(bond1, minimum_value, maximum_value)

    assert observed == False

def test_bond_check_error():
    bond_length = 'a'

    with pytest.raises(TypeError):
        observed = ga.bond_check(bond_length)
