from starlette.config import Config
import logging

config = Config("app/core/.env")

FA_DATABASE_URL = config("FA_DATABASE_URL", cast=str, default="")
