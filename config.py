from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    reverso_refresh_token: SecretStr = Field(validation_alias="REVERSO_REFRESH")

    duocards_access_token: SecretStr = Field(validation_alias="DUOCARDS_TOKEN")
    duocards_deck_id: SecretStr = Field(validation_alias="DUOCARDS_DECK_ID")

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


app_settings = AppSettings()
