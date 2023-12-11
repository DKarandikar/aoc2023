from dataclasses import dataclass


@dataclass
class Grid:
    pipes: list[list[str]]

    @staticmethod
    def from_str(s: str):
        lines = s.split("\n")
        return Grid([[x for x in y] for y in lines])

    def get_start(self) -> tuple[int, int]:
        for y, line in enumerate(self.pipes):
            for x, c in enumerate(line):
                if c == 'S':
                    return x, y

        raise RuntimeError("No start in grid")

    def get(self, x: int, y: int) -> str | None:
        """ (0, 0) is top left"""
        try:
            return self.pipes[y][x]
        except IndexError:
            return None

    def get_connected(self, x: int, y: int) -> list[tuple[int, int]]:
        """ For x,y get the connected tiles for valid pipes """
        c = self.get(x, y)
        match c:
            case '|': return [(x, y + 1), (x, y - 1)]
            case '-': return [(x + 1, y), (x - 1, y)]
            case 'L': return [(x + 1, y), (x, y - 1)]
            case 'J': return [(x - 1, y), (x, y - 1)]
            case '7': return [(x - 1, y), (x, y + 1)]
            case 'F': return [(x + 1, y), (x, y + 1)]

        return []

    def get_next(self, x: int, y: int, prev: tuple[int, int]) -> tuple[int, int]:
        conns = self.get_connected(x, y)
        for conn in conns:
            if conn != prev:
                return conn

        raise RuntimeError(f"No valid next for: {x, y}")

    def get_start_connections(self) -> list[tuple[int, int]]:
        start = self.get_start()
        valid_next = []

        up = self.get(start[0], start[1] - 1)
        down = self.get(start[0], start[1] + 1)
        left = self.get(start[0] - 1, start[1])
        right = self.get(start[0] + 1, start[1])

        if up in ('|', '7', 'F'):
            valid_next.append((start[0], start[1] - 1))
        if down in ('|', 'J', 'L'):
            valid_next.append((start[0], start[1] + 1))
        if left in ('-', 'L', 'F'):
            valid_next.append((start[0] - 1, start[1]))
        if right in ('-', '7', 'J'):
            valid_next.append((start[0] + 1, start[1]))

        return valid_next

    def get_start_character(self) -> str:
        """ Get the pipe shape that S corresponds to"""
        conns = self.get_start_connections()
        if (abs(conns[0][0] - conns[1][0])) == 2:
            return '-'
        if (abs(conns[0][1] - conns[1][1])) == 2:
            return '|'
        x, y = self.get_start()
        from_origin = set((c[0] - x, c[1] - y) for c in conns)

        if from_origin == {(0, 1), (1, 0)}:
            return 'F'
        if from_origin == {(0, 1), (-1, 0)}:
            return '7'
        if from_origin == {(0, -1), (1, 0)}:
            return 'L'
        if from_origin == {(0, -1), (-1, 0)}:
            return 'J'

        raise RuntimeError("Invalid Start")

    def get_loop(self) -> list[tuple[int, int]]:
        sx, sy = self.get_start()
        start_conns = self.get_start_connections()
        x, y = start_conns[0]
        loop = [(x, y)]

        while self.get(x, y) != 'S':
            n = self.get_next(x, y, (sx, sy))
            sx, sy = x, y
            x, y = n
            loop.append((x, y))

        return loop

    def get_loop_length(self) -> int:
        return len(self.get_loop())

    def get_farthest(self) -> int:
        return self.get_loop_length() // 2

    def loop_only_grid(self):
        loop = self.get_loop()
        sx, sy = self.get_start()
        clean = [['.'] * len(line) for line in self.pipes]
        for coord in loop:
            clean[coord[1]][coord[0]] = self.get(coord[0], coord[1])
        clean[sy][sx] = self.get_start_character()
        return clean

    def enclosed(self) -> int:
        """
        To determine how much area is enclosed, first clean the grid, so it's just the loop and '.'s
        Then count along each line keeping track of inside or outside
        Vertical lines are trivial, the tricky case are FJL7 combinations may be U/n, or they may be vertical
        lines also, so need to keep track of these
        """
        clean = self.loop_only_grid()
        count = 0
        recent = None
        for row in clean:
            outside = True
            for char in row:
                if char == '|':
                    outside = not outside
                if char in ('F', 'L'):
                    recent = char
                if char in ('7', 'J'):
                    # If FJ or L7, then this forms a boundary, otherwise it forms a U/n and doesn't change outside state
                    if recent and ((recent, char) == ('F', 'J') or (recent, char) == ('L', '7')):
                        outside = not outside
                        recent = None
                    else:
                        recent = None
                elif char == '.':
                    if not outside:
                        count += 1

        return count


def main():
    with open("../data/day10.txt") as f:
        lines = f.read()

    print(f"Day 10 part 1 is: {Grid.from_str(lines).get_farthest()}")
    print(f"Day 10 part 2 is: {Grid.from_str(lines).enclosed()}")


if __name__ == "__main__":
    main()
