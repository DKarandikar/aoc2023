import re
from dataclasses import dataclass


@dataclass
class Guess:
    red: None | int
    green: None | int
    blue: None | int


@dataclass
class Game:
    number: int
    guesses: list[Guess]


def get_or_null(t) -> None | int:
    try:
        return int(t.group(1))
    except (IndexError, AttributeError):
        return None


def parse_game(line: str) -> Game:
    parts = line.split(":")
    number = int(parts[0][4:])

    guesses = []
    guesses_str = parts[1].split(";")
    for g_str in guesses_str:
        r = re.search("(\d*) red", g_str)
        g = re.search("(\d*) green", g_str)
        b = re.search("(\d*) blue", g_str)
        guesses.append(Guess(
            get_or_null(r),
            get_or_null(g),
            get_or_null(b),
        ))

    return Game(number, guesses)


def check_game(red: int, green: int, blue: int, game: Game) -> bool:
    for guess in game.guesses:
        if guess.red and guess.red > red:
            return False
        if guess.green and guess.green > green:
            return False
        if guess.blue and guess.blue > blue:
            return False
    return True


def part1(red: int, green: int, blue: int, input: str):
    res = 0
    for line in input.split("\n"):
        game = parse_game(line)
        if check_game(red, green, blue, game):
            res += game.number
    return res


def main():
    with open("../data/day2.txt") as f:
        lines = f.read()

    print(f"Day 2 part 1 is: {part1(12, 13, 14, lines)}")


if __name__ == "__main__":
    main()
