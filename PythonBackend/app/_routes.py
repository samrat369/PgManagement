from fastapi import APIRouter
from app.db import get_database  # ✅ gets global db

router = APIRouter()

@router.get("/health/db")
async def check_db():
    db = get_database()
    if db is None:
        return {"status": "disconnected"}

    try:
        await db.command("ping")
        return {"status": "connected"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
