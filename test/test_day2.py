from src.day2 import part1, parse_game

test_input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""


def test_parse_game():
    game = parse_game("Game 4: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")

    assert game.number == 4
    assert len(game.guesses) == 3

    assert game.guesses[0].red == 4


def test_example_part1():
    assert part1(12, 13, 14, test_input) == 8
