from src.day16 import Grid, State, Beam

test_input = """.|...\\....
|.-.\\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|...."""


def test_energized():
    grid = Grid.from_str(test_input)

    assert grid.calculate_energized() == 46


def test_best_energized():
    grid = Grid.from_str(test_input)

    assert grid.calculate_best_energized() == 51


def test_do_step_dot():
    grid = Grid.from_str(test_input)
    state = State([Beam((0, 0), 'r')], 0, 10, 10)

    next_state = grid.do_step(state)

    assert next_state.next == [Beam((1, 0), 'r')]
    assert next_state.existing == 1


def test_do_step_split():
    grid = Grid.from_str(test_input)
    state = State([Beam((1, 0), 'r')], 0, 10, 10)

    next_state = grid.do_step(state)

    assert next_state.next == [Beam((1, 1), 'd')]
    assert next_state.existing == 16
