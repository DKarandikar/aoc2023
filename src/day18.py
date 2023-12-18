from dataclasses import dataclass
from typing import Literal


@dataclass
class PlanLine:
    direction: Literal['D', 'L', 'R', 'U']
    distance: int
    colour: str

    @staticmethod
    def from_str(s: str, true_instructions=False) -> 'PlanLine':
        parts = s.split(" ")
        if not true_instructions:
            return PlanLine(parts[0], int(parts[1]), parts[2])

        hex = int(parts[2][2:-2], 16)
        match parts[2][-2]:
            case '0': return PlanLine('R', hex, '')
            case '1': return PlanLine('D', hex, '')
            case '2': return PlanLine('L', hex, '')
            case '3': return PlanLine('U', hex, '')



@dataclass
class Lagoon:
    input: list[PlanLine]

    @staticmethod
    def from_str(s: str, true_instructions=False) -> 'Lagoon':
        return Lagoon([PlanLine.from_str(s, true_instructions) for s in s.split("\n")])

    def area(self) -> int:
        origin = (0, 0)
        vertexes = [origin]

        for plan in self.input:
            current = vertexes[-1]
            if plan.direction == 'U':
                next_vertex = (current[0], current[1] + plan.distance)
            elif plan.direction == 'D':
                next_vertex = (current[0], current[1] - plan.distance)
            elif plan.direction == 'R':
                next_vertex = (current[0] + plan.distance, current[1])
            else:
                next_vertex = (current[0] - plan.distance, current[1])
            vertexes.append(next_vertex)

        edges = 0
        area = 0

        for i in range(len(vertexes) - 1):
            edges += abs((vertexes[i+1][0] - vertexes[i][0]) + (vertexes[i+1][1] - vertexes[i][1]))
            area += (vertexes[i+1][0] - vertexes[i][0])*(vertexes[i+1][1] + vertexes[i][1])

        return 1 + (edges + area) // 2


def main():
    with open("../data/day18.txt") as f:
        lines = f.read()

    print(f"Day 18 part 1 is: {Lagoon.from_str(lines).area()}")
    print(f"Day 18 part 1 is: {Lagoon.from_str(lines, True).area()}")


if __name__ == "__main__":
    main()
