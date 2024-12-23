from collections import defaultdict
from itertools import combinations
from typing import Dict, Set, List, Tuple


def find_antinodes(grid: List[str], extend_lines: bool = False) -> int:
    """
    Find antinodes in the grid based on symbol patterns.
    Args:
        grid: List of strings representing the grid
        extend_lines: If True, extends lines through the grid (part 2)
    """
    # Build location map of symbols
    locations: Dict[str, Set[Tuple[int, int]]] = defaultdict(set)
    m, n = len(grid), len(grid[0])
    for r in range(m):
        for c in range(n):
            if grid[r][c] != ".":
                locations[grid[r][c]].add((r, c))

    # Find antinodes
    antinodes: Set[Tuple[int, int]] = set()
    for symbol_locations in locations.values():
        for (a, b), (c, d) in combinations(symbol_locations, 2):
            dr = a - c
            dc = b - d

            if extend_lines:
                # Extend lines in both directions
                row, col = a, b
                while row in range(m) and col in range(n):
                    antinodes.add((row, col))
                    row += dr
                    col += dc

                row, col = c, d
                while row in range(m) and col in range(n):
                    antinodes.add((row, col))
                    row -= dr
                    col -= dc
            else:
                # Just check immediate next positions
                for r, c in [(a + dr, b + dc), (c - dr, d - dc)]:
                    if r in range(m) and c in range(n):
                        antinodes.add((r, c))

    return len(antinodes)


def part1(puzzle_input: str) -> int:
    grid = puzzle_input.split()
    return find_antinodes(grid, extend_lines=False)


def part2(puzzle_input: str) -> int:
    grid = puzzle_input.split()
    return find_antinodes(grid, extend_lines=True)


def main() -> None:
    with open("data.txt", "r") as f:
        data = f.read()
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
