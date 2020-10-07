"""
A text adventure game using dictionaries
Made by: Adam Syauqi Medise
"""
from cmd import Cmd
import random

#rooms setup
rooms = {'starting':{'name': 'the starting room', 'north': 'room_1', 'text': "The room is dark and empty.", 'contents': ['water', 'flashlight', 'key']},
    'room_1':{'name': 'a dimly lit room', 'north': 'room_2', 'west': 'none', 'south': 'starting', 'text': "Still pretty dark even with the light bulb shining dimly.", 'lock': 'yes'},
    'room_2':{'name': 'an intersection', 'north': 'none', 'west': 'room_3', 'south': 'room_1', 'text': "There's nothing here."},
    'room_3':{'name': 'an empty room', 'west': 'room_4', 'east': 'room_2', 'text': 'I hear something in the distance.'},
    'room_4':{'name': 'an 4-way intersection', 'north': 'none', 'west': 'room_5', 'east': 'room_3', 'south': 'none', 'text': "There's hallway in every direction."},
    'room_5':{'name': 'a strange room', 'west': 'room_6', 'east': 'room_4', 'text': "There are strange markings here."},
    'room_6':{'name': 'an intersection', 'west': 'none', 'east': 'room_5', 'north': 'room_7', 'text': "I hear skeletons near me."},
    'room_7':{'name': 'a dark room', 'north': 'room_8', 'south': 'room_6', 'text': "I feel like something is following me."},
    'room_8':{'name': 'an intersection', 'north': 'room_9', 'west': 'none', 'east': 'none', 'text': "The rooms are getting darker as I go."},
    'room_9':{'name': 'a room filled with bones', 'north': 'room_10', 'west': 'none', 'east': 'none', 'text': "I don't like this room one bit."},
    'room_10':{'name': 'a dark corner', 'south': 'room_9', 'east': 'room_11', 'text': "Only go forward or go back."},
    'room_11':{'name': 'a hallway', 'north': 'none', 'east': 'room_12', 'text': "East or north? I don't know where should I go."},
    'room_12':{'name': 'a dark hallway', 'north': 'room_13', 'south': 'none', 'text': "I see a door leading me somewhere."},
    'room_13':{'name': 'a room filled with blood', 'north': 'room_14', 'south': 'room_12', 'text':"There's blood all over the floor! I feel sick!"},
    'room_14':{'name': 'a hallway with a text written with blood on the wall', 'west': 'none', 'east': 'room_15', 'south': 'room_13', 'text': "It says exit is on the west."},
    'room_15':{'name': 'a room with light shining through a door', 'north': 'end', 'west': 'room_14', 'text': "This is it, it's the exit."},
    'end':{'name': 'the exit', 'text': "I am finally free of this place!"}}
direction = ['north', 'south', 'east', 'west']
current_room = rooms['starting']

#player information
health = 10
player_items = {}

#weapons list:
weapons_list = ['sword', 'knife']

def dev_win():
    global current_room
    global rooms
    current_room = rooms['end']
    in_room()

def game_end():
    if current_room['name'] == 'the exit':
        print("Game End!")
        raise SystemExit
    else:
        pass

def current_inventory():
    global player_items
    l = []
    if player_items != {}:
        for k, v in player_items.items():
            if v > 0:
                l.append(str("{}: {}".format(k.capitalize(), v)))
            else:
                continue
        if l == []:
            print("I don't have anything.")
        else:
            print("Inventory:",' '.join(l))
    else:
        print("I don't have anything.")

def stat():
    print("Player Health: {}".format(health))

def in_room():
    global rooms
    global direction
    global current_room
    l = []
    print()
    print("You are in {}.".format(current_room['name']))
    print(current_room['text'])
    for i in current_room.keys():
        if i in direction:
            l.append(i.capitalize())
    if l == []:
        pass
    else:
        print()
        print('Available direction')
        print(' '.join(l))
    game_end()

def movement(command):
    global rooms
    global direction
    global current_room
    if command in direction:
        if command in current_room:
            try:
                lock_room = rooms[current_room[command]]
                if lock_room['lock'] == 'yes':
                    print("Room is locked.")
                else:
                    if current_room[command] == 'none':
                        print("Room is not made yet.")
                    else:
                        current_room = rooms[current_room[command]]
                        in_room()
            except KeyError:
                try:
                    current_room = rooms[current_room[command]]
                    in_room()
                except KeyError:
                    print("Room is not made yet.")
        else:
            print("You can't go that way.")
    else:
        print("I don't understand that command.")

def look():
    l = []
    try:
        if current_room['contents'] == []:
            print('I see nothing useful here')
        else:
            for item in current_room['contents']:
                l.append(item.capitalize())
            print('What I see in this room:')
            print(' '.join(l))
    except KeyError:
        print('I see nothing useful here')

def take(command):
    global player_items
    global rooms
    global direction
    global current_room
    try:
        try:
            current_room['contents'].remove(command)
            if command in player_items:
                player_items[command] += 1
                print("I've picked up {}".format(command))
            else:
                player_items[command] = 1
                print("I've picked up {}".format(command))
        except:
            print("That item isn't here")
    except:
        print("That item isn't here")

def drop(item):
    global player_items
    if item in player_items:
        if player_items[item] > 0:
            player_items[item] -= 1
            print("I've dropped {}".format(item))
            try:
                current_room['contents'].append(item)
            except KeyError:
                l = []
                l.append(item)
                current_room['contents'] = l
        else:
            print("I don't have that item.")
    else:
        print("I don't have that item.")

def unlock(location):
    global player_items
    global current_room
    global rooms
    global direction
    if 'key' not in player_items.keys():
        print("I don't have a key")
    else:
        if location in current_room:
            try:
                unlock_room = rooms[current_room[location]]
                if unlock_room['lock'] == 'no':
                    print("That room is already unlocked. A1")
                elif unlock_room['lock'] == 'yes':
                    if player_items['key'] > 0:
                        unlock_room['lock'] = 'no'
                        player_items['key'] -= 1
                        print("I've unlocked {} of my current room.".format(location))
                    else:
                        print("I don't have a key.")
            except KeyError:
                print("That room is already unlocked. A2")
        else:
            print("That location doesn't exist.")

#def check_enemy():
#    global current_room
#    global rooms
#    if 'enemy' in current_room:
#        fight()
#    else:
#        pass

#def fight():
#    if current_room['enemy'] == 'Jati':
#        TheEnemy = Jati
#    else:
#        pass
#    do = input(str('What do ou want to do?: ').lower())
#    if do == attack:
#        attack()
#    elif do == item:
#        use_item()
#    elif do == flee:
#        pass

#def attack():
#    for item in player_items:
#        if item in weapons_list:
#            print(item)
#    weapon_attack = input('What weapon do you want to use?: ')
#    if weapon_attack == sword:
#        TheEnemy.health -= 3
#    elif weapon_attack == knife:
#        TheEnemy.health -= 2


class Enemy:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
    
    def is_alive(self):
        return self.health > 0

class Jati(Enemy):
    def __init__(self):
        super().__init__(name="Jati", heath=5, damage=18)

class my_prompt(Cmd):
    def do_Move(self, args):
        movement(args.lower())

    def help_Move(self):
        print("Move to a desired location whenever possible. eg. Move North/north")

    def do_Stat(self, args):
        stat()

    def help_Stat(self):
        print("Shows the current player stats (right now only health is available.)")

    def do_Inventory(self, args):
        current_inventory()

    def help_Inventory(self):
        print("Shows the current player inventory.")

    def do_Quit(self, args):
        raise SystemExit

    def help_Quit(self, args):
        print("Quits the game.")

    def do_Look(self, args):
        look()

    def help_Look(self):
        print("Checks the room for usable items and possibly interactable items.")

    def do_Take(self, args):
        if args == '':
            print("You can't take nothing.")
        else:
            take(args.lower())

    def help_Take(self):
        print("Takes an item and puts it in the player inventory.")

    def do_Drop(self, args):
        if args == '':
            print("You can't drop nothing.")
        else:
            drop(args.lower())

    def help_Drop(self):
        print("Drops the desired item in the room.")

    def do_Unlock(self, args):
        if args == '':
            print("Please specify location")
        else:
            unlock(args.lower())

    def do_Win(self, args):
        dev_win()

prompt = my_prompt()
prompt.prompt = '> '
print('Text adventure game v0.3')
print()
print("-Update v0.2:")
print('Player now can move, look for items in the room, take items, check their stat (only health for now), drop items, and check their inventory')
print("-Update v0.3:")
print("Room now may come locked. Player can unlock it with a key.")
prompt.cmdloop(in_room())
