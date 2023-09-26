from typing import NamedTuple

from alchemy_game.utils import CardValues


class Card(NamedTuple):
    name: str


class Artefact(Card):
    biome: str
    text: str


class Ingredient(Card):
    biome: str
    bleeding: CardValues
    temperature: CardValues
    sensitivity: CardValues
    congestion: CardValues


class Potion(Ingredient):
    pass


def create_potion(card_1: Ingredient, card_2: Ingredient) -> Potion:
    return Potion(
        name="",
        biome="",
        bleeding=card_1.bleeding + card_2.bleeding,
        temperature=card_1.temperature + card_2.temperature,
        sensitivity=card_1.sensitivity + card_2.sensitivity,
        congestion=card_1.congestion + card_2.congestion
    )
