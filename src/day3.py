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

    def parts(self):
        parts = []
        symbol_lookup = [(s.x, s.y) for s in self.symbols]
        for number in self.numbers:
            ns = number.neighbours()
            if any([n in symbol_lookup for n in ns]):
                parts.append(number)
        return parts

    def part_sum(self):
        return sum([n.number for n in self.parts()])

    def gear_ratio_sum(self):
        res = 0
        for symbol in self.symbols:
            if symbol.symbol == "*":
                if (ratio := gear_ratio(symbol, self.numbers)) is not None:
                    res += ratio

        return res


def gear_ratio(symbol: Symbol, numbers: list[Number]) -> int | None:
    rel_numbers = list(filter(lambda n: symbol.y - 1 <= n.y <= symbol.y + 1, numbers))
    parts = []
    for number in rel_numbers:
        if (symbol.x, symbol.y) in number.neighbours():
            parts.append(number)

    if len(parts) == 2:
        return parts[0].number * parts[1].number


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


def main():
    with open("../data/day3.txt") as f:
        lines = f.read()

    schematic = parse_schematic(lines)
    print(f"Day 3 part 1 is: {schematic.part_sum()}")
    print(f"Day 3 part 2 is: {schematic.gear_ratio_sum()}")


if __name__ == "__main__":
    main()
