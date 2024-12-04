def is_safe_part_1(row: list[int]) -> bool:
    if len(row) < 2:
        return False

    is_increasing = None

    for i in range(len(row) - 1):
        diff = row[i + 1] - row[i]

        if diff == 0 or abs(diff) > 3:
            return False

        if is_increasing is None:
            is_increasing = diff > 0
            continue

        if (diff > 0) != is_increasing:
            return False

    return True

def is_safe_part_2(row: list[int]) -> bool:
    if is_safe_part_1(row):
        return True
    
    for i in range(len(row)):
        test_row = row[:i] + row[i+1:]
        if is_safe_part_1(test_row):
            return True
    return False

def part_1(data: list[list[int]]) -> int:
    return sum(1 for row in data if is_safe_part_1(row))

def part_2(data: list[list[int]]) -> int:
    return sum(1 for row in data if is_safe_part_2(row))

def main():
    data = []
    with open("data.txt", "r") as f:
        for line in f:
            if line.strip():
                numbers = [int(x) for x in line.strip().split()]
                data.append(numbers)
    print(part_1(data))
    print(part_2(data))
if __name__ == "__main__":
    main()
