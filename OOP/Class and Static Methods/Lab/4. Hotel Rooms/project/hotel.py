from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []

    @property
    def guests(self):
        return sum([room.guests for room in self.rooms])

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people: int):
        for room in self.rooms:
            if room.number == room_number:
                room.take_room(people)

    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                room.free_room()

    def status(self):
        free_rooms = [room.number for room in self.rooms if room.guests == 0]
        taken_rooms = [room.number for room in self.rooms if room.guests != 0]
        return f"Hotel {self.name} has {self.guests} total guests\n" + 'Free rooms: ' + ', '.join(map(str, free_rooms)) + '\n' + 'Taken rooms: ' + ', '.join(map(str, taken_rooms))