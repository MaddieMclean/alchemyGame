from typing import List, NamedTuple
from dataclasses import dataclass

from alchemy_game.cards import Card, Artefact, Patient


@dataclass
class Player:
    deck: List[Card]
    hand: List[Card]
    artefacts: List[Artefact]  # artefacts currently in play


class InPlay(NamedTuple):
    players: List[Player]
    patients: List[Patient]


class Board:
    in_play: InPlay
    forest: List[Card]  # todo create all biome draw piles
    patients_deck: List[Patient]


class Game:
    def new_game(self):
        return

    def loop(self) -> bool:
        return False


def main():
    game = Game()
    game.new_game()


if __name__ == "__main__":
    main()
