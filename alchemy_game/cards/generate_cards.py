import json
from itertools import product

from alchemy_game.cards import Ingredient
from alchemy_game.utils import CardValues


def generate_ingredients():
    cards = [
        Ingredient(
            name="", biome="", bleeding=b, temperature=t, sensitivity=s, congestion=c
        )
        for b, t, s, c in product(CardValues, repeat=4)
    ]

    with open("Ingredients.json", "w") as f:
        json.dump([c._asdict() for c in cards], f, indent=4)


if __name__ == "__main__":
    generate_ingredients()
