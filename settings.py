from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    baseUrl: str = Field(default="https://dsp2-technical-test.iliad78.net")


client_settings = Settings()
