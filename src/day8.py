import math
from dataclasses import dataclass
from typing import Callable


@dataclass
class Node:
    label: str
    left: str
    right: str

    @staticmethod
    def from_str(s: str):
        parts = s.split(" = ")
        label = parts[0]
        lr = parts[1].split(", ")
        return Node(label, lr[0][1:], lr[1][:-1])


@dataclass
class Instructions:
    sequence: str
    nodes: dict[str, Node]

    @staticmethod
    def from_str(s: str):
        lines = s.split("\n")
        sequence = lines[0]

        nodes = {}
        for line in lines[2:]:
            node = Node.from_str(line)
            nodes[node.label] = node

        return Instructions(sequence, nodes)

    def steps(self, start: str = "AAA", end_fn: Callable[[str], bool] = lambda x: x == 'ZZZ'):
        current = start
        command_tick = 0

        while not end_fn(current):
            command = self.sequence[command_tick % len(self.sequence)]
            command_tick += 1

            node = self.nodes[current]
            current = node.left if command == 'L' else node.right

        return command_tick

    def ghost_steps(self):
        starting_points = [x.label for x in filter(lambda x: x.label[-1] == "A", self.nodes.values())]

        steps = [self.steps(x, lambda x: x[-1] == 'Z') for x in starting_points]

        return math.lcm(*steps)


def main():
    with open("../data/day8.txt") as f:
        lines = f.read()

    print(f"Day 8 part 1 is: {Instructions.from_str(lines).steps()}")
    print(f"Day 8 part 2 is: {Instructions.from_str(lines).ghost_steps()}")


if __name__ == "__main__":
    main()
