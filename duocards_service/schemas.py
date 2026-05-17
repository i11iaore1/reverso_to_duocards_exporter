from abc import ABC

from pydantic import BaseModel

from schemas import Card


class _DuocardsCardBase(BaseModel, ABC):
    """Contains only necessary fields.
    Can be converted to Card."""

    front: str
    back: str
    langBack: str

    def to_card(self) -> Card:
        return Card(
            original=self.front,
            translation=self.back,
            language=self.langBack,
        )


class DuocardsCardFull(_DuocardsCardBase):
    """Contains additional fields.
    Can not be created from Card."""

    id: str
    hint: str


class DuocardsCard(_DuocardsCardBase):
    """Can be created from Card."""

    @classmethod
    def from_card(cls, card: Card) -> "DuocardsCard":
        return cls(
            front=card.original,
            back=card.translation,
            langBack=card.language,
        )
