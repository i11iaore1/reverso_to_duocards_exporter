from abc import ABC

from pydantic import BaseModel

from schemas import Card


class _ReversoCardBase(BaseModel, ABC):
    """Contains only necessary fields.
    Can be converted to Card."""

    srcText: str
    trgText: str
    trgLang: str

    def to_card(self) -> Card:
        return Card(
            original=self.srcText,
            translation=self.trgText,
            language=self.trgLang,
        )


class ReversoCardFull(_ReversoCardBase):
    """Contains additional fields.
    Can not be created from Card."""

    id: int


class ReversoCard(_ReversoCardBase):
    """Can be created from Card."""

    @classmethod
    def from_card(cls, card: Card) -> "ReversoCard":
        return cls(
            srcText=card.original,
            trgText=card.translation,
            trgLang=card.language,
        )
