
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