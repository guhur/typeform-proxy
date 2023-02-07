from pydantic import BaseSettings


class Settings(BaseSettings):
    api_key: str

    allowed_origins: list[str] = ["http://localhost"]

    test_form_id: str = ""

    class Config:
        env_file = ".env"


settings = Settings()
