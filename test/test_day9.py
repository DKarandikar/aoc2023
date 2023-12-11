from src.day9 import Pattern

test_input = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""


def test_parse():
    pattern = Pattern.from_str(test_input.split("\n")[0])

    assert pattern.numbers == [0, 3, 6, 9, 12, 15]


def test_next():
    pattern1 = Pattern.from_str(test_input.split("\n")[0])
    pattern2 = Pattern.from_str(test_input.split("\n")[1])
    pattern3 = Pattern.from_str(test_input.split("\n")[2])

    assert pattern1.next() == 18
    assert pattern2.next() == 28
    assert pattern3.next() == 68
