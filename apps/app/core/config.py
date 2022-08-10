from starlette.config import Config
import logging

config = Config("app/core/.env")

FA_DATABASE_URL = config("FA_DATABASE_URL", cast=str, default="")
ACCESS_TOKEN_EXPIRE_MINUTES = 60
ALGORITM = "HS256"
FA_SECRET_KEY = config(
    "FA_SECRET_KEY", cast=str,
    default="f8fec52a6dd5d6812415940d72d1862b9379560133e23ccdda1e7419f77ca344")
