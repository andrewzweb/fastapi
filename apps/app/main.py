from fastapi import FastAPI

#from app.ping.api import ping_pong
import app.ping.api as ping
#app = FastAPI()

#app.include_router(ping_pong.router)

def create_app():
    app = FastAPI()
    app.include_router(ping.router)
    return app

app = create_app()
