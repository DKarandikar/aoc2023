from dataclasses import dataclass


@dataclass
class Pattern:
    numbers: list[int]

    @staticmethod
    def from_str(line: str):
        return Pattern([int(x) for x in line.split()])

    def next(self):
        current_history = self.numbers
        histories = [current_history]
        while not all([x == 0 for x in current_history]):
            current_history = [current_history[i] - current_history[i-1] for i in range(1, len(current_history))]
            histories.append(current_history)

        rev = list(reversed(histories))
        for i, history in enumerate(rev):
            if all([x == 0 for x in history]):
                history.append(0)
            else:
                history.append(history[-1] + rev[i-1][-1])

        return histories[0][-1]


def main():
    with open("../data/day9.txt") as f:
        lines = f.read()

    print(f"Day 9 part 1 is: {sum(Pattern.from_str(x).next() for x in lines.split('\n'))}")


if __name__ == "__main__":
    main()
