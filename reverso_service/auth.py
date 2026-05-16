from datetime import datetime, timezone
from functools import wraps
from typing import Callable, Concatenate

from curl_cffi import requests
from pydantic import BaseModel, Field

from config import app_settings


class ReversoAuth(BaseModel):
    access: str = Field(validation_alias="accessToken")
    access_exp: datetime = Field(validation_alias="accessTokenExpirationDate")


_reverso_auth: ReversoAuth | None = None


def refresh_token() -> ReversoAuth:
    headers = {
        "Accept": "application/json",
        "Origin": "https://www.reverso.net",
        "Referer": "https://www.reverso.net/",
        "X-Reverso-Origin": "translation.web",
    }

    response = requests.post(
        url="https://account.reverso.net/api/v1/account/accessToken",
        impersonate="chrome",
        json={"refreshToken": app_settings.reverso_refresh_token.get_secret_value()},
        headers=headers,
    )
    result = response.content.decode("utf-8")

    return ReversoAuth.model_validate_json(result)


def with_reverso_auth[**P, R](func: Callable[Concatenate[str, P], R]) -> Callable[P, R]:
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        global _reverso_auth
        if _reverso_auth is None or _reverso_auth.access_exp.astimezone(
            timezone.utc
        ) < datetime.now(timezone.utc):
            _reverso_auth = refresh_token()
        return func(_reverso_auth.access, *args, **kwargs)

    return wrapper
