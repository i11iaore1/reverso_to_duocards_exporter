import asyncio

import duocards_service
import reverso_service
from duocards_service.client import DuocardsCard
from utils.card_adapter import adapt


async def main():
    reverso_cards = reverso_service.get_favorites()
    duocards_cards = [
        adapt(reverso_card, DuocardsCard) for reverso_card in reverso_cards
    ]

    result = await duocards_service.create_cards(duocards_cards)

    return result


if __name__ == "__main__":
    print(asyncio.run(main()))
