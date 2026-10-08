"""Basic arithmetic functions with docstrings."""


def add(a, b):
    """Add two numbers strictly as floats."""
    return float(a) + float(b)


def subtract(a, b):
    """Subtract two numbers strictly as floats."""
    return float(a) - float(b)


def average(nums, round_to):
    """Calculate rounded average."""
    if not nums:
        return 0
    return round(sum(nums) / len(nums), round_to)
