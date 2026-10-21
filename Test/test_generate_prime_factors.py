
"""Tests for prime factor generation."""

import pytest

from prime import generate_prime_factors


def test_invalid_input():
    """Check that non-integer input raises ValueError."""
    with pytest.raises(ValueError):
        generate_prime_factors("hello")