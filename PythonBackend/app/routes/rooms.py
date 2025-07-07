from fastapi import APIRouter, HTTPException
from datetime import datetime
from ..db import get_database
from ..models.roomRequest import RoomCreateRequest
from ..models.rooms import RoomOut

from ..factories.concreteRooms import SingleRoom, DoubleRoom, TripleRoom, QuadRoom
from ..factories.decorators import AcDecorator, GeyserDecorator, TvDecorator

router = APIRouter()

@router.post("/rooms/create", response_model=RoomOut)
async def create_room_via_factory(data: RoomCreateRequest):
    db = get_database()
    # Check if room already exists
    if await db.rooms.find_one({"roomId": data.roomId}):
        raise HTTPException(status_code=400, detail="Room ID already exists")

    # Map room type to base room factory
    factory_map = {
        "single": SingleRoom,
        "double": DoubleRoom,
        "triple": TripleRoom,
        "quad": QuadRoom
    }

    base_room = factory_map[data.roomType](data.roomId)

    # Apply decorators based on flags
    if data.useAC:
        base_room = AcDecorator(base_room)
    if data.useGeyser:
        base_room = GeyserDecorator(base_room)
    if data.useTV:
        base_room = TvDecorator(base_room)

    # Final room dict
    room_dict = base_room.create()
    
    await db.rooms.insert_one(room_dict)

    return room_dict
