from dataclasses import dataclass


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
class Network:
    nodes: dict[str, Node]


@dataclass
class Instructions:
    sequence: str
    network: Network

    @staticmethod
    def from_str(s: str):
        lines = s.split("\n")
        sequence = lines[0]

        nodes = {}
        for line in lines[2:]:
            node = Node.from_str(line)
            nodes[node.label] = node

        return Instructions(sequence, Network(nodes))

    def steps_to_zzz(self):
        current = 'AAA'
        command_tick = 0
        while current != 'ZZZ':
            command = self.sequence[command_tick % len(self.sequence)]
            command_tick += 1

            node = self.network.nodes[current]
            current = node.left if command == 'L' else node.right

        return command_tick


def main():
    with open("../data/day8.txt") as f:
        lines = f.read()

    print(f"Day 8 part 1 is: {Instructions.from_str(lines).steps_to_zzz()}")


if __name__ == "__main__":
    main()
