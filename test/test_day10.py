from src.day10 import Grid

test_input = """7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ"""

test_input2 = """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
..........."""

test_input3 = """..........
.S------7.
.|F----7|.
.||....||.
.||....||.
.|L-7F-J|.
.|..||..|.
.L--JL--J.
.........."""

test_input4 = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L"""


def test_parse():
    grid = Grid.from_str(test_input)

    assert grid.get(0, 2) == 'S'


def test_next():
    grid = Grid.from_str(test_input)

    assert grid.get_next(0, 3, (0, 2)) == (0, 4)


def test_start():
    grid = Grid.from_str(test_input)

    assert grid.get_start() == (0, 2)


def test_start_conns():
    grid = Grid.from_str(test_input)

    assert grid.get_start_connections() == [(0, 3), (1, 2)]


def test_loop_length():
    grid = Grid.from_str(test_input)

    assert grid.get_loop_length() == 16


def test_start_char():
    grid = Grid.from_str(test_input)

    assert grid.get_start_character() == 'F'


def test_enclosed():
    grid1 = Grid.from_str(test_input)
    grid2 = Grid.from_str(test_input2)
    grid3 = Grid.from_str(test_input3)
    grid4 = Grid.from_str(test_input4)

    assert grid1.enclosed() == 1
    assert grid2.enclosed() == 4
    assert grid3.enclosed() == 4
    assert grid4.enclosed() == 10
