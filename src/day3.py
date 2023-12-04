import re
from dataclasses import dataclass


@dataclass
class Number:
    x: int
    y: int
    number: int

    def neighbours(self):
        # Includes self locations
        length = len(str(self.number))
        return [(self.x - 1 + a, self.y - 1 + b) for a in range(2 + length) for b in range(3)]


@dataclass
class Symbol:
    x: int
    y: int
    symbol: str


@dataclass
class Schematic:
    numbers: list[Number]
    symbols: list[Symbol]


def parse_line(row: int, line: str) -> Schematic:
    symbols = []
    numbers = []
    so_far = ""
    for i in range(len(line)):
        if line[i] == "." or line[i] not in "0123456789":
            if so_far != "":
                numbers.append(Number(i - len(so_far), row, int(so_far)))
                so_far = ""
            if line[i] != ".":
                symbols.append(Symbol(i, row, line[i]))
        else:
            so_far += line[i]
    if so_far != "":
        numbers.append(Number(len(line) - len(so_far), row, int(so_far)))

    return Schematic(numbers, symbols)


def parse_schematic(input: str) -> Schematic:
    symbols = []
    numbers = []
    for i, line in enumerate(input.split("\n")):
        l = parse_line(i, line)
        symbols.extend(l.symbols)
        numbers.extend(l.numbers)

    return Schematic(numbers, symbols)


def part1(input: str):
    res = 0
    schematic = parse_schematic(input)
    symbol_lookup = [(s.x, s.y) for s in schematic.symbols]
    for number in schematic.numbers:
        ns = number.neighbours()
        if any([n in symbol_lookup for n in ns]):
            res += number.number

    return res


def main():
    with open("../data/day3.txt") as f:
        lines = f.read()

    print(f"Day 3 part 1 is: {part1(lines)}")


if __name__ == "__main__":
    main()
