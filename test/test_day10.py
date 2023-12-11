from src.day10 import Grid

test_input="""7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ"""


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

    assert grid.get_loop_length() == 17
