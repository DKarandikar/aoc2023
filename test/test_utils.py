from src.utils import flip, flip_str


def test_flip():
    assert flip([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
    assert flip([[1, 4], [2, 5], [3, 6]]) == [[1, 2, 3], [4, 5, 6]]


def test_flip_str():
    assert flip_str(['123', '456']) == ['14', '25', '36']
    assert flip_str(['14', '25', '36']) == ['123', '456']
