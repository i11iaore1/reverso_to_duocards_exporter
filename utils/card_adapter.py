from typing import Protocol, Self

from schemas import Card


class AdaptableToCard(Protocol):
    def to_card(self) -> Card: ...


class AdaptableFromCard(Protocol):
    @classmethod
    def from_card(cls, card: Card) -> Self: ...


def adapt[T: AdaptableFromCard](
    from_object: AdaptableToCard,
    to_class: type[T],
) -> T:
    card = from_object.to_card()
    return to_class.from_card(card)
