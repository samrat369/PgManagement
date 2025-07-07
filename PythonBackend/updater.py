import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb+srv://admin123:admin123@cluster0.oobqelf.mongodb.net/test?retryWrites=true&w=majority&appName=Cluster0"
DB_NAME = "test"

async def patch_rooms_with_utilities():
    client = AsyncIOMotorClient(MONGO_URI)
    db = client[DB_NAME]
    rooms = db.rooms

    async for room in rooms.find({}):
        update_fields = {}

        # Add utilities if missing
        #
        update_fields["utilities"] = {
                "wifi": True,
                "ac": False,
                "geyser": False,
                "tv" : False
            }

        # Add rent if missing
        # if "rent" not in room:
        #     if room["roomType"]=="single":
        #         update_fields["rent"] = 15000  # Default value
        #     else:update_fields["rent"] = 10000


        if update_fields:
            await rooms.update_one(
                {"_id": room["_id"]},
                {"$set": update_fields}
            )

    print("✅ Rooms updated with utilities and rent.")

asyncio.run(patch_rooms_with_utilities())
