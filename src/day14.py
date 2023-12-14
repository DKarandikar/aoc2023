from dataclasses import dataclass

from src.utils import flip_str


def roll_left(row: str) -> str:
    groups = []
    current_group = [0, 0]
    for char in row:
        if char == 'O':
            current_group[0] += 1
        elif char == '.':
            current_group[1] += 1
        else:
            groups.append(current_group)
            current_group = [0, 0]

    groups.append(current_group)

    rv = ""
    for group in groups:
        rv += "O" * group[0]
        rv += "." * group[1]
        rv += '#'

    return rv[:-1]  # Trim final unnecessary #


@dataclass
class Rocks:
    grid: list[str]

    @staticmethod
    def from_str(s: str):
        return Rocks(s.split("\n"))

    def slide_north(self):
        rotated = flip_str(self.grid)
        rv = []
        for row in rotated:
            rv.append(roll_left(row))
        self.grid = flip_str(rv)
        return self

    def load_north(self) -> int:
        max_load = len(self.grid)

        rv = 0
        for i, row in enumerate(self.grid):
            rv += row.count("O") * (max_load - i)

        return rv


def main():
    with open("../data/day14.txt") as f:
        lines = f.read()

    print(f"Day 14 part 1 is: {Rocks.from_str(lines).slide_north().load_north()}")


if __name__ == "__main__":
    main()
