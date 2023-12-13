from src.day11 import Universe

test_input = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""


def test_expand():
    visible = Universe.from_str(test_input)

    assert visible.empty_rows == [3, 7]
    assert visible.empty_columns == [2, 5, 8]


def test_sum_lengths():
    visible = Universe.from_str(test_input)

    assert visible.sum_lengths(2) == 374
    assert visible.sum_lengths(10) == 1030
    assert visible.sum_lengths(100) == 8410


def test_distance():
    visible = Universe.from_str(test_input)

    assert visible.distance(visible.galaxies[0], visible.galaxies[6], 2) == 15
    assert visible.distance(visible.galaxies[2], visible.galaxies[5], 2) == 17
    assert visible.distance(visible.galaxies[7], visible.galaxies[8], 2) == 5
