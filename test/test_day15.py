from src.day15 import hash_aoc

test_input = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""


def test_hash():
    hashes = [hash_aoc(x) for x in test_input.split(",")]
    assert hashes[0] == 30
    assert hashes[1] == 253

    assert sum(hashes) == 1320
