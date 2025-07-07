from .baseRoom import Room

class SingleRoom(Room):
    def create(self):
        self.rent = 15000
        self.beds = [{"bedNumber":int(f"{self.room_id}{i}")} for i in range(1)]
        self.room_type = "single"
        return {
            "roomId": self.room_id,
            "roomType": self.room_type,
            "beds": self.beds,
            "utilities": self.utilities,
            "rent": self.rent,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at
        }

class DoubleRoom(Room):
    def create(self):
        self.rent = 10000
        self.beds = [{"bedNumber":int(f"{self.room_id}{i}")} for i in range(2)]
        self.room_type = "double"
        return {
            "roomId": self.room_id,
            "roomType": self.room_type,
            "beds": self.beds,
            "utilities": self.utilities,
            "rent": self.rent,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at
        }
    
class TripleRoom(Room):
    def create(self):
        self.rent = 8000
        self.beds = [{"bedNumber":int(f"{self.room_id}{i}")} for i in range(3)]
        self.room_type = "triple"
        return {
            "roomId": self.room_id,
            "roomType": self.room_type,
            "beds": self.beds,
            "utilities": self.utilities,
            "rent": self.rent,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at
        }
    
class QuadRoom(Room):
    def create(self):
        self.rent = 6000
        self.beds = [{"bedNumber":int(f"{self.room_id}{i}")} for i in range(4)]
        self.room_type = "quad"
        return {
            "roomId": self.room_id,
            "roomType": self.room_type,
            "beds": self.beds,
            "utilities": self.utilities,
            "rent": self.rent,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at
        }