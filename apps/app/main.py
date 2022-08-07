from fastapi import FastAPI
import app.ping.api as ping


def create_app():
    app = FastAPI()
    app.include_router(ping.router)
    return app

app = create_app()
