"""Basic arithmetic functions."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def average(nums):
    if not nums:
        return 0
    return sum(nums) / len(nums)
