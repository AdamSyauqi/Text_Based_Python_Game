import csv
from icecream import ic

class Rooms:

    def __init__(self, name, text, lock, items):
        self.name = name
        self.text = text
        self.lock = lock
        self.items = items
        self.north = None
        self.east = None
        self.south = None
        self.west = None


    def take_item(self, item):

        if item in self.items:
            return self.items.remove(item)

    def drop_item(self, item):

        self.items.append(item)

    def return_self(self):

        return self

class RoomLinked:

    def __init__(self):

        self.start = None
        self.current = None
        self.pointer = None
        self.end = None

class Player:

    def __init__(self, name, items):

        self.name = name
        self.items = items

    def take_item(self, item):

        self.items.append(item)

room = {}
room_start = ""
room_list = []

def print_room():

    ic(room)

def import_csv(files):

    reader = csv.reader(open(files, 'r'))
    room_counter = 0
    for row in reader:
        if room_counter == 0:
            global room_start
            room_start = row[0]
            room[row[0]] = {"text": row[1], "north": row[2], "east": row[3], "south": row[4],
                            "west": row[5], "lock": row[6], "items": row[7].split("|")}
            room_counter += 1
        else:
            room[row[0]] = {"text": row[1], "north": row[2], "east": row[3], "south": row[4],
                            "west": row[5], "lock": row[6], "items": row[7].split("|")}
            room_counter += 1



input_file = input("Please input csv file: ")
import_csv(input_file)
print_room()

room_counter = len(room)
RoomLinkedClass = RoomLinked()

room_made = 0

def create_rooms(key):
    current_room = room[key]

    if RoomLinkedClass.start == None:
        NewRoom = Rooms(key, current_room["text"], current_room["lock"], current_room["items"])
        RoomLinkedClass.start = NewRoom
        RoomLinkedClass.current = NewRoom
        RoomLinkedClass.end = "End"

        north = current_room["north"]
        if north is not "none":
            temp_room = room[north]
            NewRoom.north = Rooms(north, temp_room["text"], temp_room["lock"], temp_room["items"])

        east = current_room["east"]
        if east is not "none":
            temp_room = room[east]
            NewRoom.east = Rooms(east, temp_room["text"], temp_room["lock"], temp_room["items"])

        south = current_room["south"]
        if south is not "none":
            temp_room = room[south]
            NewRoom.south = Rooms(south, temp_room["text"], temp_room["lock"], temp_room["items"])

        west = current_room["west"]
        if west is not "none":
            temp_room = room[west]
            NewRoom.west = Rooms(west, temp_room["text"], temp_room["lock"], temp_room["items"])

        return

    NewRoom = Rooms(key, current_room["text"], current_room["lock"], current_room["items"])

    north = current_room["north"]
    if north is not "none" and north not in room_list:
        room_list.append(north)
        temp_room = room[north]


    east = current_room["east"]
    if east is not "none" and east not in room_list:
        room_list.append(east)
        temp_room = room[east]
        RoomLinkedClass.east = Rooms(east, temp_room["text"], temp_room["lock"], temp_room["item"])

    south = current_room["south"]
    if south is not "none" and south not in room_list:
        room_list.append(south)
        temp_room = room[south]
        RoomLinkedClass.south = Rooms(south, temp_room["text"], temp_room["lock"], temp_room["item"])

    west = current_room["west"]
    if west is not "none" and west not in room_list:
        room_list.append(west)
        temp_room = room[west]
        RoomLinkedClass.west = Rooms(west, temp_room["text"], temp_room["lock"], temp_room["item"])

for key in room:
    if room_made == 0:
        RoomLinkedClass.current = RoomLinkedClass.start
        create_rooms(key)
        room_made += 1
