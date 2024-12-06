import re

def part_1(data: list[str]) -> int:
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    values = re.findall(pattern, data)
    return sum(int(x) * int(y) for x, y in values)

def part_2(data: list[str]) -> int:
    # Find all operations in sequence
    operations = re.findall(r"(?:mul\(\d+,\d+\)|don\'t\(\)|do\(\))", data)

    enabled = True  # Start with multiplications enabled
    total = 0

    for op in operations:
        if op == "don't()":
            enabled = False
        elif op == "do()":
            enabled = True
        elif enabled:  # Only process multiplications when enabled
            x, y = map(int, re.findall(r"\d+", op))
            total += x * y

    return total

def main():
    data = []
    with open("data.txt", "r") as f:
        data = f.read()
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
