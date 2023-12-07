from src.day7 import Hand, HandList

test_input = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""


def test_parse():
    hands = HandList.from_str(test_input).hands

    assert hands[0].hand == "32T3K"
    assert hands[0].bid == 765


def test_ordering():
    hands = HandList.from_str(test_input).hands

    assert [x.bid for x in sorted(hands)] == [765, 220, 28, 684, 483]


def test_winnings():
    handList = HandList.from_str(test_input)

    assert handList.total_winnings() == 6440


def test_winnings_with_jokers():
    handList = HandList.from_str(test_input, True)

    assert handList.total_winnings() == 5905
