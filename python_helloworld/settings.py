import os
from pydantic import BaseSettings, IPvAnyAddress


ENV_FILE = os.getenv("ENV_FILE", ".env")


class APISettings(BaseSettings):
    host: IPvAnyAddress = "0.0.0.0"
    port: int = 5000

    class Config:
        env_file = ENV_FILE
        env_prefix = "API_"


api_settings = APISettings()
