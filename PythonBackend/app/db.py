from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

client : AsyncIOMotorClient = None
db = None  
async def connect_to_mongo():
    global client, db  
    client = AsyncIOMotorClient(MONGO_URI)
    db = client["test"]  
    print("✅ Connected to MongoDB:", db.name)

async def close_mongo_connection():
    global client
    if client:
        client.close()

def get_database():
    #print(db)
    return db
