from pydantic import BaseModel
from typing import Literal

class RoomCreateRequest(BaseModel):
    roomId: int
    roomType: Literal["single", "double", "triple", "quad"]
    useAC: bool = False
    useGeyser: bool = False
    useTV: bool = False
