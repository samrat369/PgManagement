from .baseRoom import Room
from datetime import datetime

class RoomDecorator(Room):
    def __init__(self, room: Room):
        self._room = room  # Wraps a Room instance

    def create(self):
        return self._room.create()


class AcDecorator(RoomDecorator):
    def create(self):
        room = self._room.create()
        room["rent"] += 1000
        room["utilities"]["ac"] = True
        room["updatedAt"] = datetime.now()
        return room


class GeyserDecorator(RoomDecorator):
    def create(self):
        room = self._room.create()
        room["rent"] += 500
        room["utilities"]["geyser"] = True
        room["updatedAt"] = datetime.now()
        return room


class TvDecorator(RoomDecorator):
    def create(self):
        room = self._room.create()
        room["rent"] += 500
        room["utilities"]["tv"] = True
        room["updatedAt"] = datetime.now()
        return room
