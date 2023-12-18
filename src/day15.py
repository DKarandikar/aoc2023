def hash_aoc(s: str) -> int:
    val = 0
    for c in s:
        val += ord(c)
        val *= 17
        val %= 256
    return val


def main():
    with open("../data/day15.txt") as f:
        lines = f.read()

    print(f"Day 15 part 1 is: {sum([hash_aoc(x) for x in lines.split(",")])}")


if __name__ == "__main__":
    main()
