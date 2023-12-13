from src.day13 import Pattern

test_input = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""


def test_parse():
    patterns = Pattern.from_str(test_input)

    assert len(patterns) == 2

    assert patterns[0].grid[0][0] == '#'
    assert patterns[1].grid[0][1] == '.'


def test_reflection():
    patterns = Pattern.from_str(test_input)

    assert [p.reflection() for p in patterns] == [('vert', 4), ('hor', 3)]


def test_score():
    patterns = Pattern.from_str(test_input)

    assert [p.score() for p in patterns] == [5, 400]
