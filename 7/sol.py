from typing import Dict, List, Tuple


def calibrate(target: int, nums: list[int], current: int) -> int:
    """
    Recursively try different operator combinations.
    target: The value we're trying to reach
    nums: Remaining numbers to process
    current: Current running total
    """
    # Base case - no more numbers to process
    if not nums:
        if current == target:
            return target
        else:
            return 0

    # Try multiplication and addition with the next number
    num = nums[0]
    remaining = nums[1:]

    # Optimization: skip if both operations would exceed target
    if current * num > target and current + num > target:
        return 0

    # Try multiplication
    if calibrate(target, remaining, current * num) == target:
        return target

    # Try addition
    if calibrate(target, remaining, current + num) == target:
        return target

    return 0


def calibrate_with_concatenation(target: int, nums: list[int], current: int) -> int:
    """
    Recursively try different operator combinations.
    target: The value we're trying to reach
    nums: Remaining numbers to process
    current: Current running total
    """
    # Base case - no more numbers to process
    if not nums:
        if current == target:
            return target
        else:
            return 0

    # Try multiplication and addition with the next number
    num = nums[0]
    remaining = nums[1:]
    concat = int(str(current) + str(num))
    if current * num > target and current + num > target and concat > target:
        return 0

    if calibrate_with_concatenation(target, remaining, current * num) == target:
        return target
    if calibrate_with_concatenation(target, remaining, current + num) == target:
        return target
    if calibrate_with_concatenation(target, remaining, concat) == target:
        return target

    return 0


def part_1(data: Dict[int, List[int]]) -> int:
    total = 0
    for key, value in data.items():
        total += calibrate(key, value[1:], value[0])
    return total

def part_2(data: Dict[int, List[int]]) -> int:
    total = 0
    for key, value in data.items():
        total += calibrate_with_concatenation(key, value[1:], value[0])
    return total


def main():
    data = {}
    with open("data.txt", "r") as f:
        data = f.read()
    data = data.split("\n")
    data = [line.split(" ") for line in data if line != ""]
    data = {int(line[0].replace(":", "")): [int(num) for num in line[1:]] for line in data}
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
