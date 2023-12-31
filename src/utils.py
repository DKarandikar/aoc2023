def flip(grid: list[list]):
    cols = [[] for _ in range(len(grid[0]))]
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            cols[x].append(char)
    return cols


def flip_str(grid: list[str]):
    cols = ["" for _ in range(len(grid[0]))]
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            cols[x] += char
    return cols
