from src.day11 import Universe, flip

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


def test_flip():
    assert flip([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
    assert flip([[1, 4], [2, 5], [3, 6]]) == [[1, 2, 3], [4, 5, 6]]


def test_sum_lengths():
    visible = Universe.from_str(test_input)

    assert visible.sum_lengths() == 374


def test_distance():
    visible = Universe.from_str(test_input)

    assert visible.distance(visible.galaxies[0], visible.galaxies[6]) == 15
    assert visible.distance(visible.galaxies[2], visible.galaxies[5]) == 17
    assert visible.distance(visible.galaxies[7], visible.galaxies[8]) == 5
