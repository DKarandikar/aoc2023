from dataclasses import dataclass
from typing import Literal

Direction = Literal['r', 'l', 'u', 'd']


@dataclass
class Beam:
    location: tuple[int, int]
    dir: Direction

    def __str__(self):
        return f"{self.dir},{self.location[0]},{self.location[1]}"

    def __hash__(self):
        return hash(self.__str__())

    def step(self) -> 'Beam':
        x, y = self.location
        match self.dir:
            case 'r':
                return Beam((x + 1, y), self.dir)
            case 'l':
                return Beam((x - 1, y), self.dir)
            case 'u':
                return Beam((x, y - 1), self.dir)
            case 'd':
                return Beam((x, y + 1), self.dir)


@dataclass
class State:
    next: list[Beam]
    existing: dict[tuple[int, int], set[Direction]]

    def key(self) -> str:
        all_beams = [*self.next]

        for k, v in self.existing.items():
            for dir in v:
                all_beams.append(Beam(k, dir))

        return "".join(sorted([str(x) for x in set(all_beams)]))


@dataclass
class Grid:
    rows: list[str]

    @property
    def height(self):
        return len(self.rows)

    @property
    def width(self):
        return len(self.rows[0])

    @staticmethod
    def from_str(s: str) -> 'Grid':
        return Grid([x for x in s.split("\n")])

    def get(self, x: int, y: int) -> str:
        return self.rows[y][x]

    def calculate_best_energized(self):
        best = 0
        for x in range(self.width):
            val = self.calculate_energized(Beam((x, 0), 'd'))
            print(f"Done: {x}d")
            if val > best:
                best = val
        for x in range(self.width):
            val = self.calculate_energized(Beam((x, self.height - 1), 'u'))
            print(f"Done: {x}u")
            if val > best:
                best = val
        for y in range(self.height):
            val = self.calculate_energized(Beam((0, y), 'r'))
            print(f"Done: {y}r")
            if val > best:
                best = val
        for y in range(self.height):
            val = self.calculate_energized(Beam((self.width - 1, y), 'l'))
            print(f"Done: {y}l")
            if val > best:
                best = val
        return best

    def calculate_energized(self, initial_beam: Beam = Beam((0, 0), 'r')) -> int:
        state = State([initial_beam], {})
        so_far = {state.key()}
        while True:
            state = self.do_step(state)
            key = state.key()
            if key in so_far:
                break
            else:
                so_far.add(key)

        return len(state.existing)

    def beam_inside(self, b: Beam) -> bool:
        return (0 <= b.location[0] < self.width) and (0 <= b.location[1] < self.height)

    def do_step(self, s: State) -> State:
        new_state = State([], s.existing)
        for beam in s.next:
            dirs = new_state.existing.setdefault(beam.location, set())
            dirs.add(beam.dir)

            action = self.get(beam.location[0], beam.location[1])

            match action:
                case '.':
                    new_state.next.append(beam.step())

                case '|':
                    if beam.dir == 'r' or beam.dir == 'l':
                        new_state.next.append(Beam(beam.location, 'd').step())
                        new_state.next.append(Beam(beam.location, 'u').step())
                    else:
                        new_state.next.append(beam.step())

                case '-':
                    if beam.dir == 'u' or beam.dir == 'd':
                        new_state.next.append(Beam(beam.location, 'r').step())
                        new_state.next.append(Beam(beam.location, 'l').step())
                    else:
                        new_state.next.append(beam.step())

                case '/':
                    match beam.dir:
                        case 'd': new_state.next.append(Beam(beam.location, 'l').step())
                        case 'u': new_state.next.append(Beam(beam.location, 'r').step())
                        case 'l': new_state.next.append(Beam(beam.location, 'd').step())
                        case 'r': new_state.next.append(Beam(beam.location, 'u').step())

                case '\\':
                    match beam.dir:
                        case 'd': new_state.next.append(Beam(beam.location, 'r').step())
                        case 'u': new_state.next.append(Beam(beam.location, 'l').step())
                        case 'l': new_state.next.append(Beam(beam.location, 'u').step())
                        case 'r': new_state.next.append(Beam(beam.location, 'd').step())

        new_state.next = list(set(filter(lambda b: self.beam_inside(b), new_state.next)))

        return new_state


def main():
    with open("../data/day16.txt") as f:
        lines = f.read()

    print(f"Day 16 part 1 is: {Grid.from_str(lines).calculate_energized()}")
    print(f"Day 16 part 2 is: {Grid.from_str(lines).calculate_best_energized()}")


if __name__ == "__main__":
    main()
