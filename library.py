class Library():
    rooms = []
    def __init__(self, number_of_rooms):
        self.number_of_rooms = number_of_rooms

    def add_room(self, room):
        if (len(self.rooms)  < self.number_of_rooms):
            self.rooms.append(room)
        else:
            raise Exception("You can't add another room to the library.")