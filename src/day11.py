import itertools
from dataclasses import dataclass


def flip(grid: list[list]):
    cols = [[] for _ in range(len(grid[0]))]
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            cols[x].append(char)
    return cols


class Universe:
    def __init__(self, grid: list[list[str]]):
        self.grid = grid
        self.empty_rows, self.empty_columns = self.calculate_empty()
        self.galaxies = self.calc_galaxies()

    @staticmethod
    def from_str(s: str):
        lines = s.split("\n")
        return Universe([[x for x in y] for y in lines])

    def calculate_empty(self) -> tuple[list[int], list[int]]:
        rows = []
        for i, line in enumerate(self.grid):
            if not any(x == '#' for x in line):
                rows.append(i)

        flipped = flip(self.grid)
        cols = []
        for i, line in enumerate(flipped):
            if not any(x == '#' for x in line):
                cols.append(i)

        return rows, cols

    def calc_galaxies(self) -> list[tuple[int, int]]:
        rv = []

        for column, line in enumerate(self.grid):
            for row, char in enumerate(line):
                if char == '#':
                    rv.append((row, column))

        return rv

    def distance(self, galaxy1: tuple[int, int], galaxy2: tuple[int, int]) -> int:
        xs = sorted([galaxy1[0], galaxy2[0]])
        ys = sorted([galaxy1[1], galaxy2[1]])

        special_rows = list(filter(lambda y: ys[0] < y < ys[1], self.empty_rows))
        special_cols = list(filter(lambda x: xs[0] < x < xs[1], self.empty_columns))

        return (xs[1] - xs[0]) + (ys[1] - ys[0]) + len(special_rows) + len(special_cols)

    def sum_lengths(self) -> int:
        pairs = itertools.combinations(self.galaxies, 2)

        rv = 0
        for pair in pairs:
            rv += self.distance(pair[0], pair[1])

        return rv


def main():
    with open("../data/day11.txt") as f:
        lines = f.read()

    print(f"Day 11 part 1 is: {Universe.from_str(lines).sum_lengths()}")


if __name__ == "__main__":
    main()
