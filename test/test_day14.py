from src.day14 import Rocks, roll_left

test_input = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""

test_input_north = """OOOO.#.O..
OO..#....#
OO..O##..O
O..#.OO...
........#.
..#....#.#
..O..#.O.O
..O.......
#....###..
#....#...."""


def test_parse():
    rocks = Rocks.from_str(test_input)

    assert rocks.grid[0][0] == 'O'


def test_roll():
    assert roll_left(".O#.OO.#O#.O.") == "O.#OO..#O#O.."
    assert roll_left(".O#.OO.#O#.O#") == "O.#OO..#O#O.#"
    assert roll_left(".O#.OO.#O#.O.#") == "O.#OO..#O#O..#"
    assert roll_left(".O#.OO.#O#.O.#O") == "O.#OO..#O#O..#O"
    assert roll_left(".O#.OO.#O#.O.#O.") == "O.#OO..#O#O..#O."


def test_roll_grid():
    rocks = Rocks.from_str(test_input)
    rocks.slide_north()

    assert rocks == Rocks.from_str(test_input_north)


def test_north_load():
    rocks = Rocks.from_str(test_input)
    rocks.slide_north()

    assert rocks.load_north() == 136
