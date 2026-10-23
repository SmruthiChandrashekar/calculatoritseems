"""Basic arithmetic functions with docstrings."""


def add(a, b):
    """Add two numbers strictly as floats."""
    return float(a) + float(b)


def subtract(a, b):
    """Subtract two numbers strictly as floats."""
    return float(a) - float(b)


def average(nums):
    if not nums:
        return 0
    return sum(nums) / len(nums)


def broken():
    return +++
