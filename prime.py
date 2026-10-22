"""Generate prime factors."""


def generate_prime_factors(number):
    """Return prime factors of an integer."""
    if not isinstance(number, int):
        raise ValueError("Input must be an integer")

    factors = []
    divisor = 2

    while divisor * divisor <= number:
        while number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        divisor += 1

    if number > 1:
        factors.append(number)

    return factors
