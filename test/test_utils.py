from src.utils import flip


def test_flip():
    assert flip([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
    assert flip([[1, 4], [2, 5], [3, 6]]) == [[1, 2, 3], [4, 5, 6]]
