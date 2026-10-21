
"""Tests for prime factor generation."""

import pytest

from prime import generate_prime_factors


def test_invalid_input():
    """Check that non-integer input raises ValueError."""
    with pytest.raises(ValueError):
        generate_prime_factors("hello")
        
def test_one():
    """Check that 1 returns an empty list."""
    assert generate_prime_factors(1) == []
def test_two():
    """Check that 2 returns [2]."""
    assert generate_prime_factors(2) == [2]
def test_six():
    """Check that 6 returns [2, 3]."""
    assert generate_prime_factors(6) == [2, 3]

def test_three():
    """Check that 3 returns [3]."""
    assert generate_prime_factors(3) == [3]


def test_four():
    """Check that 4 returns [2, 2]."""
    assert generate_prime_factors(4) == [2, 2]

def test_eight():
    """Check that 8 returns [2, 2, 2]."""
    assert generate_prime_factors(8) == [2, 2, 2]

def test_nine():
    """Check that 9 returns [3, 3]."""
    assert generate_prime_factors(9) == [3, 3]

def test_ten():
    """Check that 10 returns [2, 5]."""
    assert generate_prime_factors(10) == [2, 5]

def test_twelve():
    """Check that 12 returns [2, 2, 3]."""
    assert generate_prime_factors(12) == [2, 2, 3]