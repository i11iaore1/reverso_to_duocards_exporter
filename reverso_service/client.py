from curl_cffi import requests
from pydantic import BaseModel

from reverso_service.schemas import ReversoCard

from .auth import with_reverso_auth

BASE_REVERSO_URL = "https://context.reverso.net"
REVERSO_FAV_URL = f"{BASE_REVERSO_URL}/bst-web-user/user/favourites"


class GetFavResponse(BaseModel):
    results: list[ReversoCard]


@with_reverso_auth
def get_favorites(reverso_auth: str, amount: int = 50) -> list[ReversoCard]:
    params = {
        "order": 10,
        "start": 0,
        "length": amount,
    }

    response = requests.get(
        url=REVERSO_FAV_URL,
        params=params,
        headers={"Authorization": reverso_auth},
        impersonate="chrome",
    )
    result = response.content.decode("utf-8")

    return GetFavResponse.model_validate_json(result).results


@with_reverso_auth
def delete_favorites(reverso_auth: str, ids: list[int]) -> None:
    params = {"ids": ids}

    response = requests.delete(
        url=REVERSO_FAV_URL,
        params=params,
        headers={"Authorization": reverso_auth},
        impersonate="chrome",
    )

    return response.content.decode("utf-8")
