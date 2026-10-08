from calc import add, subtract, average


def generate_report(numbers):
    total = sum(numbers)
    avg = average(numbers)
    return {
        "count": len(numbers),
        "total": total,
        "average": avg
    }


if __name__ == "__main__":
    sample_data = [10, 20, 30, 40]
    result = generate_report(sample_data)
    print("Report Summary:")
    for key, val in result.items():
        print(f"  {key}: {val}")
