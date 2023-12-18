from dataclasses import dataclass
from typing import Iterable


@dataclass
class Lens:
    label: str
    focal: int


@dataclass
class Box:
    lens: list[Lens]

    def remove(self, label: str):
        self.lens = list(filter(lambda lens: lens.label != label, self.lens))

    def add(self, label: str, focal: int):
        for lens in self.lens:
            if lens.label == label:
                lens.focal = focal
                break
        else:
            self.lens.append(Lens(label, focal))

    def score(self) -> int:
        rv = 0
        for i, lens in enumerate(self.lens):
            rv += (i + 1) * lens.focal
        return rv


def hash_aoc(s: str) -> int:
    val = 0
    for c in s:
        val += ord(c)
        val *= 17
        val %= 256
    return val


def run_instructions(instructions: Iterable[str]) -> int:
    box_map: dict[int, Box] = {}
    for instruction in instructions:
        if '-' in instruction:
            parts = instruction.split('-')
        else:
            parts = instruction.split('=')
        label = parts[0]

        h = hash_aoc(label)
        box = box_map.setdefault(h, Box([]))

        if '-' in instruction:
            box.remove(label)
        else:
            box.add(label, int(parts[1]))

    rv = 0
    for k, v in box_map.items():
        rv += (k + 1) * v.score()

    return rv


def main():
    with open("../data/day15.txt") as f:
        lines = f.read()

    print(f"Day 15 part 1 is: {sum([hash_aoc(x) for x in lines.split(",")])}")
    print(f"Day 15 part 2 is: {run_instructions(lines.split(","))}")


if __name__ == "__main__":
    main()
