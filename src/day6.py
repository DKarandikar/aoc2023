import math
from dataclasses import dataclass


@dataclass
class Race:
    record: int
    time: int

    @staticmethod
    def from_str(s: str) -> list['Race']:
        lines = s.split("\n")
        times = lines[0].split("Time:")[1].split()
        distances = lines[1].split("Distance:")[1].split()

        rv = []
        for i, time in enumerate(times):
            rv.append(Race(int(distances[i]), int(time)))

        return rv

    @staticmethod
    def from_str_single(s: str) -> 'Race':
        lines = s.split("\n")
        times = lines[0].split("Time:")[1].split()
        distances = lines[1].split("Distance:")[1].split()

        time = "".join(times)
        distance = "".join(distances)

        return Race(int(distance), int(time))

    def solve(self) -> float:
        """ Solve for minimum time to wait before letting go to beat the record, returns the lower solution"""
        # Analytically, x(t-x)=d to solve, so x^2 - tx + d = 0, so x = (t +/- sqrt(t^2 - 4d))/2

        winning_margin = 1  # Need to beat the current record
        return (1.0 * self.time - math.sqrt(self.time ** 2 - 4 * (self.record + winning_margin)))/2

    def error_margin(self) -> int:
        solution = math.ceil(self.solve())
        return self.time + 1 - 2 * solution


def main():
    with open("../data/day6.txt") as f:
        lines = f.read()

    print(f"Day 6 part 1 is: {math.prod([r.error_margin() for r in Race.from_str(lines)])}")
    print(f"Day 6 part 2 is: {Race.from_str_single(lines).error_margin()}")


if __name__ == "__main__":
    main()
