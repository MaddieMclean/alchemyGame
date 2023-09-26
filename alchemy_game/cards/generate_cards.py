import json
from itertools import product
from dataclasses import asdict

from alchemy_game.cards import Ingredient, Symptoms
from alchemy_game.utils import CardValues


def generate_ingredients():
    cards = [
        Ingredient(
            name="",
            biome="",
            symptoms=Symptoms(bleeding=b, temperature=t, sensitivity=s, congestion=c),
        )
        for b, t, s, c in product(CardValues, repeat=4)
    ]

    with open("Ingredients.json", "w") as f:
        json.dump([asdict(c) for c in cards], f, indent=4, default=lambda x: x.value)


if __name__ == "__main__":
    generate_ingredients()
