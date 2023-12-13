import copy
from dataclasses import dataclass
from typing import Literal

from src.utils import flip

Reflection = tuple[Literal['vert', 'hor'], int]


def has_mirror_row(grid: list[list], to_ignore: int = None) -> None | int:
    for i in range(len(grid) - 1):
        if to_ignore == i:
            continue
        backwards = i
        forward = i + 1
        while backwards >= 0 and forward < len(grid):
            if grid[backwards] != grid[forward]:
                break
            backwards -= 1
            forward += 1
        else:
            return i


def get_reflection(grid: list[list], to_ignore: Reflection = None) -> Reflection | None:
    to_ignore_direction = to_ignore[0] if to_ignore else None
    to_ignore_value = to_ignore[1] if to_ignore else None

    if (hor_i := has_mirror_row(grid, to_ignore_value if to_ignore_direction == 'hor' else None)) is not None:
        return 'hor', hor_i

    if (vert_i := has_mirror_row(flip(grid), to_ignore_value if to_ignore_direction == 'vert' else None)) is not None:
        return 'vert', vert_i

    return None


@dataclass
class Pattern:
    grid: list[list[str]]
    with_smudge: bool

    @staticmethod
    def from_str(s: str, with_smudge: bool = False) -> list['Pattern']:
        grids = s.split('\n\n')

        return [Pattern([[x for x in y] for y in grid.split("\n")], with_smudge) for grid in grids]

    def reflection(self, with_smudge_override: bool = None) -> Reflection:
        if with_smudge_override is not False and self.with_smudge:
            return self._smudge()

        if ref := get_reflection(self.grid):
            return ref
        raise RuntimeError(f"No reflection in grid: {self.grid}")

    def _smudge(self) -> Reflection:
        original_ref = self.reflection(False)
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if (new_ref := self._test_smudge(i, j, original_ref)) is not None:
                    return new_ref

        raise RuntimeError(f"No smudge reflection in grid: {self.grid}")

    def _test_smudge(self, i: int, j: int, original_ref) -> Reflection | None:
        new_grid = copy.deepcopy(self.grid)
        new_grid[i][j] = '.' if self.grid[i][j] == '#' else '#'
        return get_reflection(new_grid, original_ref)

    def score(self) -> int:
        direction, i = self.reflection()
        match direction:
            case 'vert': return i + 1
            case 'hor': return 100 * (i + 1)


def main():
    with open("../data/day13.txt") as f:
        lines = f.read()

    print(f"Day 13 part 1 is: {sum(p.score() for p in Pattern.from_str(lines))}")
    print(f"Day 13 part 2 is: {sum(p.score() for p in Pattern.from_str(lines, True))}")


if __name__ == "__main__":
    main()
