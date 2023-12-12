from src.day12 import HotSprings

test_input = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""


def test_parse():
    springs = HotSprings.from_str(test_input.split("\n")[0])

    assert springs.row == "???.###"
    assert springs.groups == (1, 1, 3)


def test_arrangements():
    assert HotSprings.from_str(test_input.split("\n")[0]).arrangements() == 1
    assert HotSprings.from_str(test_input.split("\n")[1]).arrangements() == 4
    assert HotSprings.from_str(test_input.split("\n")[2]).arrangements() == 1
    assert HotSprings.from_str(test_input.split("\n")[3]).arrangements() == 1
    assert HotSprings.from_str(test_input.split("\n")[4]).arrangements() == 4
    assert HotSprings.from_str(test_input.split("\n")[5]).arrangements() == 10


def test_arrangements_folded():
    assert HotSprings.from_str_folded(test_input.split("\n")[0]).arrangements() == 1
    assert HotSprings.from_str_folded(test_input.split("\n")[1]).arrangements() == 16384
    assert HotSprings.from_str_folded(test_input.split("\n")[2]).arrangements() == 1
    assert HotSprings.from_str_folded(test_input.split("\n")[3]).arrangements() == 16
    assert HotSprings.from_str_folded(test_input.split("\n")[4]).arrangements() == 2500
    assert HotSprings.from_str_folded(test_input.split("\n")[5]).arrangements() == 506250
