from __future__ import annotations

from enum import Enum


class CardValues(Enum):
    negative = -1
    neutral = 0
    positive = 1

    def __add__(self, other) -> CardValues:
        if self.__class__ is other.__class__:
            return self._clamp(self.value + other.value)
        return NotImplemented

    def __eq__(self, other) -> bool:
        if self.__class__ is other.__class__:
            return self.value == other.value
        return NotImplemented

    @staticmethod
    def _clamp(n: int) -> CardValues:
        return CardValues(
            max(int(CardValues.negative), min(n, int(CardValues.positive)))
        )
