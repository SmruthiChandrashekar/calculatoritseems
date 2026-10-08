"""Basic arithmetic functions with alternate changes."""


def add(a, b):
    # Altered implementation from conflict branch
    return int(a) + int(b)


def subtract(a, b):
    return int(a) - int(b)


def average(nums):
    if not nums:
        return 0
    return sum(nums) / len(nums)
