import re
from dataclasses import dataclass


@dataclass
class Card:
    number: int
    winning: list[int]
    yours: list[int]

    @staticmethod
    def from_str(line: str):
        parts = line.split(":")
        number = int(parts[0].split("Card ")[1])
        sub_parts = parts[1].split("|")
        winning = [int(x) for x in filter(lambda x: x != "", sub_parts[0].split(" "))]
        yours = [int(x) for x in filter(lambda x: x != "", sub_parts[1].split(" "))]
        return Card(number, winning, yours)

    def score(self) -> int:
        res = 0
        for winning in self.winning:
            if winning in self.yours:
                res = 1 if res == 0 else res * 2

        return res

    def winning_numbers(self) -> int:
        res = 0
        for winning in self.winning:
            if winning in self.yours:
                res += 1

        return res


@dataclass
class CardStack:
    cards: list[Card]
    instances: list[int]

    @staticmethod
    def from_str(lines: str):
        cards = []
        for line in lines.split("\n"):
            card = Card.from_str(line)
            cards.append(card)
        return CardStack(cards, [1] * len(cards))

    def _process_card(self, number: int):
        card = self.cards[number]
        winning = card.winning_numbers()
        for x in range(winning):
            self.instances[number + 1 + x] += self.instances[number]

    def _process_stack(self):
        for i in range(len(self.cards)):
            self._process_card(i)

    def sum(self):
        return sum([c.score() for c in self.cards])

    def instance_sum(self):
        self._process_stack()
        return sum(self.instances)


def main():
    with open("../data/day4.txt") as f:
        lines = f.read()

    print(f"Day 4 part 1 is: {CardStack.from_str(lines).sum()}")
    print(f"Day 4 part 2 is: {CardStack.from_str(lines).instance_sum()}")


if __name__ == "__main__":
    main()
