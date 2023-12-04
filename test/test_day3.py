from src.day3 import parse_line, parse_schematic, part1

test_input = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


def test_parse_line():
    l = parse_line(0, test_input.split("\n")[0])

    assert l.symbols == []
    assert l.numbers[0].x == 0
    assert l.numbers[0].number == 467

    assert l.numbers[1].x == 5
    assert l.numbers[1].number == 114


def test_parse_schematic():
    s = parse_schematic(test_input)

    assert len(s.symbols) == 6


def test_neighbours():
    l = parse_line(2, test_input.split("\n")[2])
    n = l.numbers[0].neighbours()

    assert len(n) == 12

    l = parse_line(0, test_input.split("\n")[0])
    n = l.numbers[0].neighbours()

    assert len(n) == 15


def test_part1():
    r = part1(test_input)

    assert r == 4361
