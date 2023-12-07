from dataclasses import dataclass


@dataclass
class Hand:
    hand: str
    bid: int
    score: float

    @staticmethod
    def from_str(s: str, with_jokers=False) -> 'Hand':
        parts = s.split(" ")
        return Hand(parts[0], int(parts[1]), Hand.score(parts[0], with_jokers))

    @staticmethod
    def to_hex(hand: str, joker_value='b') -> str:
        return (hand.replace("A", "e").replace("K", "d")
                .replace("Q", "c").replace("J", joker_value).replace("T", "a"))

    @staticmethod
    def score(hand: str, with_jokers=False) -> float:
        high_card_value = int(Hand.to_hex(hand, '1' if with_jokers else 'b'), 16)
        char_dict = {}
        for char in hand:
            char_dict[char] = char_dict.setdefault(char, 0) + 1

        # If we have jokers, then you always add your jokers to the largest group of cards
        if with_jokers:
            jokers = char_dict.pop('J', 0)
            values = sorted(char_dict.values())
            if jokers == 5:
                values = [5]
            else:
                values[-1] += jokers
        else:
            values = char_dict.values()

        if any([x > 4 for x in values]):
            type_ = 10
        elif any([x > 3 for x in values]):
            type_ = 9
        elif set(values) == {2, 3}:
            type_ = 8
        elif any([x > 2 for x in values]):
            type_ = 7
        elif sorted(values) == [1, 2, 2]:
            type_ = 6
        elif any([x > 1 for x in values]):
            type_ = 5
        else:
            type_ = 0

        return type_ + (high_card_value / 1000000)

    def __lt__(self, other):
        return self.score < other.score


@dataclass
class HandList:
    hands: list[Hand]

    def total_winnings(self) -> int:
        hands = sorted(self.hands)

        rv = 0
        for i, hand in enumerate(hands):
            rv += (i + 1) * hand.bid
        return rv

    @staticmethod
    def from_str(s: str, with_jokers=False) -> 'HandList':
        return HandList([Hand.from_str(x, with_jokers) for x in s.split("\n")])


def main():
    with open("../data/day7.txt") as f:
        lines = f.read()

    print(f"Day 7 part 1 is: {HandList.from_str(lines).total_winnings()}")
    print(f"Day 7 part 2 is: {HandList.from_str(lines, True).total_winnings()}")


if __name__ == "__main__":
    main()
