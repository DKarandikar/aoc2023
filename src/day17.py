from dataclasses import dataclass
from heapq import heappush, heappop, heapify

@dataclass
class HeatMap:
    grid: list[list[int]]

    @staticmethod
    def from_str(s: str) -> 'HeatMap':
        return HeatMap([[int(x) for x in y] for y in s.split("\n")])

    def explore_ultra(self) -> int:
        return self.explore(4, 10)

    def explore(self, min_steps=0, max_steps=3) -> int:
        queue = [(0, 0, 0, 's', 0)]  # dir can be stationary, r, l, u or d
        heapify(queue)
        visited = set()

        def add(heat_loss: int, x: int, y: int, direction: str, steps: int):
            if direction == 's':
                new_x, new_y = x, y
            elif direction == 'r':
                new_x, new_y = x + 1, y
            elif direction == 'l':
                new_x, new_y = x - 1, y
            elif direction == 'u':
                new_x, new_y = x, y - 1
            else:  # 'd'
                new_x, new_y = x, y + 1

            if 0 <= new_x < len(self.grid[0]) and 0 <= new_y < len(self.grid):
                heappush(
                    queue,
                    (heat_loss + self.grid[new_y][new_x], new_x, new_y, direction, steps)
                )

        while queue:
            heat_loss, x, y, direction, steps = heappop(queue)

            if steps >= min_steps and x == len(self.grid[0]) - 1 and y == len(self.grid) - 1:
                return heat_loss

            if (x, y, direction, steps) in visited:
                continue

            visited.add((x, y, direction, steps))

            if steps < max_steps and direction != 's':
                add(heat_loss, x, y, direction, steps + 1)

            if steps >= min_steps or direction == 's':
                for new_dir in ('l', 'r', 'u', 'd'):
                    if new_dir != direction:
                        if (new_dir, direction) not in [('u', 'd'), ('d', 'u'), ('l', 'r'), ('r', 'l')]:
                            add(heat_loss, x, y, new_dir, 1)

        raise RuntimeError("Didn't get to end")


def main():
    with open("../data/day17.txt") as f:
        lines = f.read()

    print(f"Day 17 part 1 is: {HeatMap.from_str(lines).explore()}")
    print(f"Day 17 part 2 is: {HeatMap.from_str(lines).explore_ultra()}")


if __name__ == "__main__":
    main()
