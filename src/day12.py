import functools


@functools.cache
def count(s: str, groups: tuple, so_far=0) -> int:
    if s == '':
        if groups == () and so_far == 0:
            return 1
        if len(groups) == 1 and groups[0] == so_far:
            return 1
        return 0

    if s[0] == '?':
        return count('#' + s[1:], groups, so_far) + count('.' + s[1:], groups, so_far)

    if s[0] == '#':
        return count(s[1:], groups, so_far + 1)

    # so s[0] == '.'
    if groups and groups[0] == so_far:
        return count(s[1:], groups[1:])

    if so_far == 0:
        return count(s[1:], groups)

    return 0


class HotSprings:
    def __init__(self, row: str, groups: tuple):
        self.row = row
        self.groups = groups

    @staticmethod
    def from_str(s: str):
        parts = s.split(" ")
        return HotSprings(parts[0], tuple(int(x) for x in parts[1].split(",")))

    def arrangements(self) -> int:
        return count(self.row, self.groups)


def main():
    with open("../data/day12.txt") as f:
        lines = f.read()

    print(f"Day 12 part 1 is: {sum([HotSprings.from_str(line).arrangements() for line in lines.split('\n')])}")


if __name__ == "__main__":
    main()
