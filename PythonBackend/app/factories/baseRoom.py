from abc import abstractmethod,ABC
from datetime import datetime


class Room(ABC):
    def __init__(self,room_id):
        self.room_id = room_id
        self.rent = 0
        self.beds = []
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.utilities = {"wifi":True,"tv":False,"geyser":False,"ac":False}
        self.room_type = None

    @abstractmethod
    def create(self):
        pass

