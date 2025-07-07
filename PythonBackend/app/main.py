from fastapi import FastAPI
from .routes import rooms
from app.db import connect_to_mongo, close_mongo_connection,get_database
from ._routes import router

app = FastAPI()

@app.on_event("startup")
async def startup():
    await connect_to_mongo()
    print(get_database())


@app.on_event("shutdown")
async def shutdown():
    await close_mongo_connection()

app.include_router(rooms.router, prefix="/api")
app.include_router(router)