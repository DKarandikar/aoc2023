import itertools
import re
from dataclasses import dataclass


class HotSprings:
    def __init__(self, row: str, groups: list[int]):
        self.row = row
        self.groups = groups
        self.r = re.compile(f"^[^#]*{'[^#]+'.join(['(#|\?)' * x for x in self.groups])}[^#]*$")

    @staticmethod
    def from_str(s: str):
        parts = s.split(" ")
        return HotSprings(parts[0], [int(x) for x in parts[1].split(",")])

    def matches(self, s: str):
        return bool(self.r.search(s))

    def determine_char(self, s: str) -> str | None:
        for i, char in enumerate(s):
            if char == '?':
                with_hash = s[:i] + '#' + s[i+1:]
                with_dot = s[:i] + '.' + s[i + 1:]
                if self.matches(with_hash) and not self.matches(with_dot):
                    return with_hash
                elif self.matches(with_dot) and not self.matches(with_hash):
                    return with_dot

        return None

    def determine_best(self) -> str:
        current = self.row
        prev = None
        while current is not None:
            prev = "" + current
            current = self.determine_char(prev)

        return prev

    def enumerate(self, s: str) -> int:
        count = s.count('?')
        options = itertools.product('.#', repeat=count)
        rv = 0
        for option in options:
            test_s = "" + s
            tick = 0
            for i, char in enumerate(s):
                if char == '?':
                    test_s = test_s[:i] + option[tick] + test_s[i + 1:]
                    tick += 1

            if self.matches(test_s):
                rv += 1

        return rv

    def arrangements(self) -> int:
        best = self.determine_best()
        if '?' not in best:
            return 1

        return self.enumerate(best)


def main():
    with open("../data/day12.txt") as f:
        lines = f.read()

    print(f"Day 12 part 1 is: {sum([HotSprings.from_str(line).arrangements() for line in lines.split('\n')])}")


if __name__ == "__main__":
    main()
