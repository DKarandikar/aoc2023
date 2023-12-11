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

    def get_loop_length(self) -> int:
        sx, sy = self.get_start()
        start_conns = self.get_start_connections()
        x, y = start_conns[0]
        steps = 2

        while self.get(x, y) != 'S':
            n = self.get_next(x, y, (sx, sy))
            sx, sy = x, y
            x, y = n
            steps += 1

        return steps

    def get_farthest(self) -> int:
        return (self.get_loop_length() - 1) // 2


def main():
    with open("../data/day10.txt") as f:
        lines = f.read()

    print(f"Day 10 part 1 is: {Grid.from_str(lines).get_farthest()}")


if __name__ == "__main__":
    main()
