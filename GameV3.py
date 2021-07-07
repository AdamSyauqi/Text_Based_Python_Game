import csv
from icecream import ic

world = {}
world_start = ""
directions = ["north", "east", "south", "west"]

class Room:

    def __init__(self, text, north, east, south, west, lock, items, keys):
        self.text = text
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.lock = lock
        self.items = items
        self.keys = keys

    def return_room_directions(self):
        """ Returns directions of connected rooms """
        list_of_directions = ["north", "east", "south", "west"]
        if self.north == "none":
            list_of_directions.remove("north")

        if self.east == "none":
            list_of_directions.remove("east")

        if self.south == "none":
            list_of_directions.remove("south")

        if self.west == "none":
            list_of_directions.remove("west")

        return 'Available Directions\n' + ' '.join(list_of_directions)

class Player:

    def __init__(self, items, location):
        self.health = 100
        self.items = items
        self.location = location

    def move(self, direction):
        """ Takes direction arguments and see if it's a valid direction, if the room exists, and if it's locked or not"""
        if direction == "north":
            if self.location.north != "none":
                if world[self.location.north].lock != "true":
                    self.location = world[self.location.north]
                else:
                    return "Room is locked, perhaps there's something I could do to open it..."
            else:
                return "There's no room over there..."

        elif direction == "east":
            if self.location.east != "none":
                if world[self.location.east].lock != "true":
                    self.location = world[self.location.east]
                else:
                    return "Room is locked, perhaps there's something I could do to open it..."
            else:
                return "There's no room over there..."

        elif direction == "south":
            if self.location.south != "none":
                if world[self.location.south].lock != "true":
                    self.location = world[self.location.south]
                else:
                    return "Room is locked, perhaps there's something I could do to open it..."
            else:
                return "There's no room over there..."

        elif direction == "west":
            if self.location.west != "none":
                if world[self.location.west].lock != "true":
                    self.location = world[self.location.west]
                else:
                    return "Room is locked, perhaps there's something I could do to open it..."
            else:
                return "There's no room over there..."

        else:
            return "Direction not recognized"

    def item_list(self):
        """ Returns player's Inventory """
        result = ""
        for key, value in self.items.items():
            if value > 0:
                result += str("{}: {}\n".format(key.capitalize(), value))
        if result == "":
            return "You don't have any items\n"
        else:
            return "Your inventory:\n" + result

    def take_item(self, item):
        """ Takes an item from the room """
        if item in self.location.items:
            if item in self.items.keys():
                self.items[item] += 1
                self.location.items.remove(item)
                return "I've picked up {}".format(item)
            else:
                self.items[item] = 1
                self.location.items.remove(item)
                return "I've picked up {}".format(item)
        else:
            return "There nothing like that here..."

    def room_items(self):
        """ Returns the items that are inside of the current room """
        if len(self.location.items) > 0:
            return "What I see here:\n" + ' '.join(self.location.items) + "\n"


    #def use_item(self, item):
    #    if item in self.items:


def insert_rooms(file):
    """ Create rooms from csv file """
    reader = csv.reader(open(file, 'r'))
    room_counter = 0
    for row in reader:
        if room_counter == 0:
            global world_start
            world_start = row[0]
            world[row[0]] = Room(row[1], row[2], row[3], row[4], row[5], row[6], row[7].split("|"), row[8].split("|"))
            room_counter += 1

        else:
            world[row[0]] = Room(row[1], row[2], row[3], row[4], row[5], row[6], row[7].split("|"), row[8].split("|"))
            room_counter += 1

input_file = input("Please input csv file: ")
insert_rooms(input_file)

player = Player({}, world[world_start])

end = False

while not end:
    print(player.location.text)
    print(player.location.return_room_directions())
    command = input("What do you want to do?\n> ")

    list_of_commands = command.split(" ")

    if list_of_commands[0].lower() == "move":
        direction = list_of_commands[1].lower()
        print(player.move(direction))

    elif list_of_commands[0].lower() == "end":
        end = True
        print("Game ended")

    elif list_of_commands[0].lower() == "items":
        print(player.item_list())

    elif list_of_commands[0].lower() == "take":
        print(player.take_item(list_of_commands[1]))

    elif list_of_commands[0].lower() == "look":
        print(player.room_items())

    else:
        print("Command not recognized")


ic(player.location)
ic(player.items)
ic(world["room0"].keys)
ic(world["room1"].keys)
