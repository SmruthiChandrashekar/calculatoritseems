"""Report generator using calculator functions."""

from calc import add, subtract, average


def generate_report(numbers):
    total = sum(numbers)
    avg = average(numbers)
    return {
        "count": len(numbers),
        "total": total,
        "average": avg,
    }


if __name__ == "__main__":
    sample = [10, 20, 30, 40]
    print(generate_report(sample))
