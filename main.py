import asyncio

import typer

import duocards_service
import reverso_service
from duocards_service.client import DuocardsCard
from utils.card_adapter import adapt

app = typer.Typer()


@app.command()
def move(amount: int):
    if amount <= 0:
        return

    reverso_cards = reverso_service.get_favorites(amount=amount)
    duocards_cards = [
        adapt(reverso_card, DuocardsCard) for reverso_card in reverso_cards
    ]

    asyncio.run(duocards_service.create_cards(duocards_cards))

    reverso_service.delete_favorites(
        [reverso_card.id for reverso_card in reverso_cards]
    )


if __name__ == "__main__":
    app()
