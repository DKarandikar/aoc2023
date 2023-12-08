from src.day8 import Instructions

test_input1 = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

test_input2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""


def test_parse():
    instructions = Instructions.from_str(test_input1)

    assert instructions.network.nodes['AAA'].left == 'BBB'
    assert instructions.network.nodes['AAA'].right == 'CCC'


def test_steps():
    instructions = Instructions.from_str(test_input1)

    assert instructions.steps_to_zzz() == 2


def test_steps2():
    instructions = Instructions.from_str(test_input2)

    assert instructions.steps_to_zzz() == 6

