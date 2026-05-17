from typing import NamedTuple


class Card(NamedTuple):
    original: str
    translation: str
    language: str = "uk"
