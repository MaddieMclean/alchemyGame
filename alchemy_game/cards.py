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
        # todo improve this
        cured = []
        for symptom, treatment in zip(self.symptoms, potion.symptoms):
            if symptom + treatment == CardValues.neutral:
                cured.append(CardValues.neutral)
            else:
                cured.append(symptom)

        self.symptoms = Symptoms(*cured)

    def cured(self) -> bool:
        return all(n == CardValues.neutral for n in self.symptoms)


def create_potion(card_1: Ingredient, card_2: Ingredient) -> Potion:
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
