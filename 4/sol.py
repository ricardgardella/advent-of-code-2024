import re
def __count_diagonals(data: str) -> int:
    lines = data.strip().split('\n')
    rows = len(lines)
    cols = len(lines[0])
    xmas_count = 0
    
    # Check diagonals going down-right
    for i in range(rows-3):
        for j in range(cols-3):
            diagonal = ''
            for k in range(4):
                diagonal += lines[i+k][j+k]
            if diagonal == 'XMAS':
                xmas_count += 1
                
    # Check diagonals going down-left
    for i in range(rows-3):
        for j in range(3, cols):
            diagonal = ''
            for k in range(4):
                diagonal += lines[i+k][j-k]
            if diagonal == 'XMAS':
                xmas_count += 1

    # Check diagonals going up-right
    for i in range(3, rows):
        for j in range(cols-3):
            diagonal = ''
            for k in range(4):
                diagonal += lines[i-k][j+k]
            if diagonal == 'XMAS':
                xmas_count += 1
                
    # Check diagonals going up-left
    for i in range(3, rows):
        for j in range(3, cols):
            diagonal = ''
            for k in range(4):
                diagonal += lines[i-k][j-k]
            if diagonal == 'XMAS':
                xmas_count += 1
                
    return xmas_count

def __count_vertical(data: str) -> int:
    lines = data.strip().split('\n')
    rows = len(lines)
    cols = len(lines[0])
    xmas_count = 0
    
    # Check vertical (down)
    for j in range(cols):
        vertical = ''
        for i in range(rows):
            vertical += lines[i][j]
        xmas_count += len(re.findall('XMAS', vertical))
        xmas_count += len(re.findall('XMAS', vertical[::-1]))  # Check upward
    
    return xmas_count

def __count_horizontal(data: str) -> int:
    lines = data.strip().split('\n')
    xmas_count = 0
    pattern = r"XMAS"
    
    # Check each line for horizontal patterns (forward and backward)
    for line in lines:
        xmas_count += len(re.findall(pattern, line))
        xmas_count += len(re.findall(pattern, line[::-1]))
    
    return xmas_count

def part_1(data: str) -> int:
    xmas_count = 0
    xmas_count += __count_horizontal(data)
    xmas_count += __count_vertical(data)
    xmas_count += __count_diagonals(data)
    return xmas_count

def __check_x_mas(data: str, row: int, col: int) -> bool:
    lines = data.strip().split('\n')
    # Check if we can fit an X pattern at this position
    if row + 2 >= len(lines) or col - 1 < 0 or col + 1 >= len(lines[0]):
        return False
    
    # Get the two diagonals
    diagonal1 = lines[row][col-1] + lines[row+1][col] + lines[row+2][col+1]  # down-right
    diagonal2 = lines[row][col+1] + lines[row+1][col] + lines[row+2][col-1]  # down-left
    
    # Check if either diagonal is "MAS" (forward or backward)
    valid_patterns = {"MAS", "SAM"}
    return (diagonal1 in valid_patterns and diagonal2 in valid_patterns)

def part_2(data: str) -> int:
    rows,cols = len(data.strip().split('\n')),len(data.strip().split('\n')[0])
    xmas_count = 0
    for i in range(rows):
        for j in range(cols):
            if __check_x_mas(data, i, j):
                xmas_count += 1
    return xmas_count

def main():
    data = []
    with open("data.txt", "r") as f:
        data = f.read()
    print(part_1(data))
    print(part_2(data))
if __name__ == "__main__":
    main()
