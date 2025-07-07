from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime

#  Bed Schema
class Bed(BaseModel):
    bedNumber: int
    status: str = Field(default="vacant")  # vacant or occupied
    tenant: Optional[str] = None

#  Utilities Schema
class Utilities(BaseModel):
    wifi: bool = True
    ac: bool = False
    geyser: bool = False
    tv : bool = False

#  Room Schema (Input for Create)
class RoomIn(BaseModel):
    roomId: int
    roomType: str  # single | double | triple | quad
    beds: List[Bed]
    utilities: Utilities = Field(default_factory=Utilities)
    rent: int

#  Room Schema (Output from DB)
class RoomOut(RoomIn):
    createdAt: Optional[datetime]
    updatedAt: Optional[datetime]
