import pytest

from src.day17 import HeatMap

test_input = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""

test_input2 = """111111111111
999999999991
999999999991
999999999991
999999999991"""


def test_explore():
    heat_map = HeatMap.from_str(test_input)

    assert heat_map.explore() == 102


@pytest.mark.parametrize("t_input,expected", [(test_input, 94), (test_input2, 71)])
def test_explore_ultra(t_input, expected):
    heat_map = HeatMap.from_str(t_input)

    assert heat_map.explore_ultra() == expected
