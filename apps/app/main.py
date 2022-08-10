from fastapi import FastAPI
import app.ping.api as ping
from app.db.base import database
from app.endpoints import users, auth, jobs


app = FastAPI(title='Exchange')
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(users.router, prefix="/api/users", tags=["users"])
app.include_router(jobs.router, prefix="/api/jobs", tags=["jobs"])

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(ping.router)
