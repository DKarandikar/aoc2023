import math

from src.day6 import Race

test_input = """Time:      7  15   30
Distance:  9  40  200"""


def test_parse():
    races = Race.from_str(test_input)

    assert len(races) == 3
    assert races[0].time == 7


def test_solve():
    races = Race.from_str(test_input)

    print(races[2].solve())

    assert math.ceil(races[0].solve()) == 2
    assert math.ceil(races[1].solve()) == 4
    assert math.ceil(races[2].solve()) == 11


def test_error():
    races = Race.from_str(test_input)

    assert races[0].error_margin() == 4
    assert races[1].error_margin() == 8
    assert races[2].error_margin() == 9


def test_error_single():
    race = Race.from_str_single(test_input)

    assert race.error_margin() == 71503
