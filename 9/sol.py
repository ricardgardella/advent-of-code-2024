import sys
import pyperclip as pc

def pr(s):
    print(s)
    pc.copy(s)

sys.setrecursionlimit(10**6)
sys.set_int_max_str_digits(20000)

infile = "9/data.txt"
data = open(infile).read().strip()

def parse_input():
    files = []
    spaces = []
    current_num = ""
    is_file = True
    
    for c in data:
        if c.isspace():
            if current_num:
                num = int(current_num)
                if is_file:
                    files.append(num)
                else:
                    spaces.append(num)
                current_num = ""
                is_file = not is_file
        else:
            current_num += c
    
    # Handle last number
    if current_num:
        num = int(current_num)
        if is_file:
            files.append(num)
        else:
            spaces.append(num)
    
    return files, spaces

def calculate_score(positions):
    return sum(pos * file_id for file_id, pos in enumerate(positions))

def solve(part2):
    files, spaces = parse_input()
    positions = []
    current_pos = 0
    
    # Initial placement of files
    for i, size in enumerate(files):
        if part2:
            positions.append(current_pos)
            current_pos += size + spaces[i]
        else:
            # For part 1, split files into size-1 chunks
            for _ in range(size):
                positions.append(current_pos)
                current_pos += 1
            current_pos += spaces[i]
    
    # Process each gap from right to left
    total_files = len(positions)
    for i in range(total_files - 1, -1, -1):
        current_pos = positions[i]
        
        # Find the leftmost available space
        available_space = 0
        for j in range(i):
            gap_size = positions[j+1] - (positions[j] + 1)
            if gap_size > 0:
                available_space = positions[j] + 1
                positions[i] = available_space
                break
    
    return calculate_score(positions)

p1 = solve(False)
p2 = solve(True)
pr(p1)
pr(p2)
