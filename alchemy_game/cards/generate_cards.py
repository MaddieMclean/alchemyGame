import json
from typing import NamedTuple
from itertools import product

from enum import IntEnum


class CardValues(IntEnum):
    negative = -1
    neutral = 0
    positive = 1


class Card(NamedTuple):
    name: str
    biome: str
    bleeding: CardValues
    temperature: CardValues
    sensitivity: CardValues
    congestion: CardValues


def generate_cards():
    cards = [Card(name="", biome="", bleeding=b, temperature=t, sensitivity=s, congestion=c)
             for b, t, s, c in product(CardValues, repeat=4)]

    with open("Cards.json", "w") as f:
        json.dump([c._asdict() for c in cards], f, indent=4)


if __name__ == '__main__':
    generate_cards()
