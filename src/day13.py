from dataclasses import dataclass
from typing import Literal

from src.utils import flip


def has_mirror_row(grid: list[list]) -> None | int:
    for i in range(len(grid) - 1):
        backwards = i
        forward = i + 1
        while backwards >= 0 and forward < len(grid):
            if grid[backwards] != grid[forward]:
                break
            backwards -= 1
            forward += 1
        else:
            return i


@dataclass
class Pattern:
    grid: list[list[str]]

    @staticmethod
    def from_str(s: str) -> list['Pattern']:
        grids = s.split('\n\n')

        return [Pattern([[x for x in y] for y in grid.split("\n")]) for grid in grids]

    def reflection(self) -> tuple[Literal['vert', 'hor'], int]:
        if (hor_i := has_mirror_row(self.grid)) is not None:
            return 'hor', hor_i

        if (vert_i := has_mirror_row(flip(self.grid))) is not None:
            return 'vert', vert_i

        raise RuntimeError(f"No reflection in grid: {self.grid}")

    def score(self) -> int:
        direction, i = self.reflection()
        match direction:
            case 'vert': return i + 1
            case 'hor': return 100 * (i + 1)


def main():
    with open("../data/day13.txt") as f:
        lines = f.read()

    print(f"Day 13 part 1 is: {sum(p.score() for p in Pattern.from_str(lines))}")


if __name__ == "__main__":
    main()
