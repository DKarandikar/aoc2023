import re
from dataclasses import dataclass


@dataclass
class Card:
    winning: list[int]
    yours: list[int]

    @staticmethod
    def from_str(line: str):
        parts = line.split(":")
        sub_parts = parts[1].split("|")
        winning = [int(x) for x in filter(lambda x: x != "", sub_parts[0].split(" "))]
        yours = [int(x) for x in filter(lambda x: x != "", sub_parts[1].split(" "))]
        return Card(winning, yours)

    def score(self) -> int:
        res = 0
        for winning in self.winning:
            if winning in self.yours:
                res = 1 if res == 0 else res * 2

        return res


def main():
    with open("../data/day4.txt") as f:
        lines = f.readlines()

    print(f"Day 4 part 1 is: {sum([Card.from_str(line).score() for line in lines])}")


if __name__ == "__main__":
    main()
