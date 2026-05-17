import asyncio

import httpx

from config import app_settings

from .schemas import DuocardsCard

BASE_DUOCARDS_URL = "https://api.duocards.com/graphql"

HEADERS = {
    "Authorization": f"Bearer {app_settings.duocards_access_token.get_secret_value()}",
    "Origin": "https://app.duocards.com",
    "Referer": "https://app.duocards.com/",
}

CREATE_QUERY = "mutation cardCreateMutation(\n  $deckId: ID!\n  $front: String!\n  $back: String!\n  $langBack: String\n  $hint: String) {\n  cardCreate(\n    deckId: $deckId\n    front: $front\n    back: $back\n    langBack: $langBack\n    hint: $hint\n  ) {\n    duplicatedCard {\n      id\n      front\n      back\n    }\n  }\n}\n"


async def _create_card(
    client: httpx.AsyncClient,
    card: DuocardsCard,
    deck_id: str = app_settings.duocards_deck_id.get_secret_value(),
) -> None:
    payload = {
        "query": CREATE_QUERY,
        "variables": {
            **card.model_dump(),
            "deckId": deck_id,
        },
    }

    response = await client.post(
        url=f"{BASE_DUOCARDS_URL}?cardCreateMutation",
        headers=HEADERS,
        json=payload,
    )

    return response.content


async def create_cards(cards: list[DuocardsCard]):
    async with httpx.AsyncClient() as client:
        async with asyncio.TaskGroup() as tg:
            tasks = [
                tg.create_task(_create_card(client=client, card=card)) for card in cards
            ]
    return [task.result() for task in tasks]
