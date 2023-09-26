from dataclasses import dataclass
from typing import NamedTuple

from alchemy_game.utils import CardValues


class Symptoms(NamedTuple):
    bleeding: CardValues
    temperature: CardValues
    sensitivity: CardValues
    congestion: CardValues


@dataclass
class Card:
    name: str


@dataclass
class Artefact(Card):
    biome: str
    text: str
    tapped: bool


@dataclass
class Ingredient(Card):
    biome: str
    symptoms: Symptoms


@dataclass
class Potion(Ingredient):
    pass


@dataclass
class Patient(Ingredient):
    def cure(self, potion: Potion):
        # updates if potion neutralises the symptom, else keeps current symptom
        # CardValues.neutral.value is false, which is why the loop works
        self.symptoms = Symptoms(
            *[
                s if (s + p).value else CardValues.neutral
                for s, p in zip(self.symptoms, potion.symptoms)
            ]
        )

    def cured(self) -> bool:
        return all(n == CardValues.neutral for n in self.symptoms)


def create_potion(card_1: Ingredient, card_2: Ingredient) -> Potion:
    # todo Should this be in Ingredient?
    return Potion(
        name="",
        biome="",
        symptoms=Symptoms(
            bleeding=card_1.symptoms.bleeding + card_2.symptoms.bleeding,
            temperature=card_1.symptoms.temperature + card_2.symptoms.temperature,
            sensitivity=card_1.symptoms.sensitivity + card_2.symptoms.sensitivity,
            congestion=card_1.symptoms.congestion + card_2.symptoms.congestion,
        ),
    )
