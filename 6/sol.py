"""Day 6 of Advent of Code 2024.

Part 1: Find unique positions visited by a guard moving through a room with obstacles.
The guard moves in a straight line until hitting an obstacle, then turns right.

Part 2: Find positions where placing an obstacle would create a loop in the guard's path.
"""

class Guard:
    """A guard that patrols through a room following simple movement rules."""

    # Direction mappings
    DIRECTION_CHANGE = {
        "u": "r",  # up -> right
        "r": "d",  # right -> down
        "d": "l",  # down -> left
        "l": "u"   # left -> up
    }
    
    DIRECTION_VECTORS = {
        "u": [-1, 0],  # up
        "r": [0, 1],   # right
        "d": [1, 0],   # down
        "l": [0, -1]   # left
    }

    def __init__(self, start_pos: list[int]):
        """Initialize guard with starting position."""
        self.init_position = start_pos.copy()
        self.restart_loop_tracker()
        self.main_path = set()
        self.positions_seen = 1
        self.possible_move = None
        self.in_bounds = True

    def change_dir(self):
        """Rotate guard 90 degrees right."""
        self.dir = self.DIRECTION_CHANGE[self.dir]

    def find_next_move(self) -> list[int]:
        """Calculate next position based on current direction."""
        self.possible_move = [
            self.position[i] + self.DIRECTION_VECTORS[self.dir][i] 
            for i in range(2)
        ]
        return self.possible_move

    def accept_move(self, next_tile: str, part_1: bool = True) -> bool:
        """Process movement to next position."""
        self.position = self.possible_move
        
        if part_1:
            self._count_if_new(next_tile == ".")
            self.track_main_path(tuple(self.position))
            return False
        return self.track_potential_loop_path(tuple(self.position))

    def _count_if_new(self, is_new: bool):
        """Increment position counter if visiting new tile."""
        self.positions_seen += is_new

    def restart_loop_tracker(self):
        """Reset guard to initial state."""
        self.position = self.init_position.copy()
        self.dir = "u"
        self.position_visits = {(self.position[0], self.position[1], self.dir)}
        self.in_bounds = True

    def track_main_path(self, pos: tuple[int, int]):
        """Record position in main patrol path."""
        if pos != tuple(self.init_position):
            self.main_path.add(pos)

    def track_potential_loop_path(self, pos: tuple[int, int]) -> bool:
        """Check if current position creates a loop."""
        current = pos + tuple(self.dir)
        if current not in self.position_visits:
            self.position_visits.add(current)
            return False
        return True


class AdventDay6:
    """Solution for Day 6 puzzle."""

    def __init__(self):
        """Initialize room map and guard."""
        self.room_map = {}
        self._load_map()
        self.part1 = 0
        self.part2 = 0

    def _load_map(self):
        """Load room map from input file."""
        with open("data.txt", "r") as f:
            for i, line in enumerate(f.readlines()):
                for j, char in enumerate(line):
                    if char == "\n":
                        continue
                    if char == "^":
                        self.guard = Guard([i, j])
                        char = "S"
                    self.room_map[(i, j)] = char

    def get_patrol_route(self, part_1: bool = True):
        """Simulate guard's patrol route."""
        while self.guard.in_bounds:
            try:
                next_pos = tuple(self.guard.find_next_move())
                next_tile = self.room_map[next_pos]
                
                if next_tile != "#":
                    loop_found = self.guard.accept_move(next_tile, part_1)
                    self.room_map[next_pos] = "!"
                    if not part_1 and loop_found:
                        self.part2 += 1
                        break
                else:
                    self.guard.change_dir()
            except KeyError:
                self.guard.in_bounds = False
        
        if part_1:
            self.part1 = self.guard.positions_seen

    def find_potential_loops(self):
        """Test each position for potential loops."""
        for test_pos in self.guard.main_path:
            # Place test obstacle
            self.room_map[test_pos] = "#"
            self.guard.restart_loop_tracker()
            self._reset_map()
            self.get_patrol_route(part_1=False)
            # Remove test obstacle
            self.room_map[test_pos] = "."

    def _reset_map(self):
        """Reset visited positions on map."""
        for pos, tile in self.room_map.items():
            if tile == "!":
                self.room_map[pos] = "."


if __name__ == "__main__":
    solution = AdventDay6()
    solution.get_patrol_route()
    solution.find_potential_loops()
    print(solution.part1, solution.part2)
