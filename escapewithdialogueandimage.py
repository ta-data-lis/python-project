# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 11:25:23 2020

@author: ivana
"""
from PIL import Image
#Winner Image
winner_image = Image.open(r"C:\Users\ivana\Documents\python-project\python-project\Freedom.png")

# define rooms and items

couch = {
    "name": "couch",
    "type": "furniture",
}

door_a = {
    "name": "door a",
    "type": "door",
}

key_a = {
    "name": "key for door a",
    "type": "key",
    "target": door_a,
}

piano = {
    "name": "piano",
    "type": "furniture",
}

game_room = {
    "name": "game room",
    "type": "room",
}

outside = {
    "name": "outside"
}

all_rooms = [game_room, outside]

all_doors = [door_a]

# define which items/rooms are related

object_relations = {
    "game room": [couch, piano, door_a],
    "piano": [key_a],
    "outside": [door_a],
    "door a": [game_room, outside]
}

# define game state. Do not directly change this dict.
# Instead, when a new game starts, make a copy of this
# dict and use the copy to store gameplay state. This
# way you can replay the game multiple times.

INIT_GAME_STATE = {
    "current_room": game_room,
    "keys_collected": [],
    "target_room": outside
}

def linebreak():
    """
    Print a line break
    """
    print("\n\n")


def start_game():
    """
    Start the game
    """
    print(
        "You wake up on a couch and find yourself in a strange house with no windows which you have never been to before.\nYou don't remember why you are here and what had happened before.\nYou feel some unknown danger is approaching and you must get out of the house, NOW!")
    play_room(game_state["current_room"])


def play_room(room):
    """
    Play a room. First check if the room being played is the target room.
    If it is, the game will end with success. Otherwise, let player either
    explore (list all items in this room) or examine an item found here.
    """
    game_state["current_room"] = room
    if (game_state["current_room"] == game_state["target_room"]):
        print("Congrats! You escaped the room!")
    else:
        print("You are now in " + room["name"] + ".")
        intended_action = input("What would you like to do? Type 'explore' or 'examine'? ").strip()
        if intended_action == "explore":
            explore_room(room)
            examine_item(input("Which item would you like to examine? ").strip())
            #napisi novu funkciju koja ce da pita sta hoces da explore odmah
            #furniture_explore()
            #play_room(room)
        elif intended_action == "examine":
            examine_item(input("What would you like to examine? ").strip())
        else:
            print("Not sure what you mean. Type 'explore' or 'examine'.")
            play_room(room)
        linebreak()

#def furniture_explore(name):
 #   items = [i["name"] for i in object_relations[room["name"]]]
  #  print("What do you want to . This is " + room["name"] + ". You find " + ", ".join(items) + ".")


def explore_room(room):
    """
    Explore a room. List all items belonging to this room.
    """
    items = [i["name"] for i in object_relations[room["name"]]]
    print("You explore the room. This is " + room["name"] + ". You find " + ", ".join(items) + ".")


def get_next_room_of_door(door, current_room):
    """
    From object_relations, find the two rooms connected to the given door.
    Return the room that is not the current_room.
    """
    connected_rooms = object_relations[door["name"]]
    for room in connected_rooms:
        if (not current_room == room):
            return room


def examine_item(item_name):
    """
    Examine an item which can be a door or furniture.
    First make sure the intended item belongs to the current room.
    Then check if the item is a door. Tell player if key hasn't been
    collected yet. Otherwise ask player if they want to go to the next
    room. If the item is not a door, then check if it contains keys.
    Collect the key if found and update the game state. At the end,
    play either the current or the next room depending on the game state
    to keep playing.
    """
    current_room = game_state["current_room"]
    next_room = ""
    output = None

    for item in object_relations[current_room["name"]]:
        if (item["name"] == item_name):
            output = "You examine " + item_name + ". "
            if (item["type"] == "door"):
                have_key = False
                for key in game_state["keys_collected"]:
                    if (key["target"] == item):
                        have_key = True
                if (have_key):
                    output += "You unlock it with a key you have."
                    next_room = get_next_room_of_door(item, current_room)
                else:
                    output += "It is locked but you don't have the key."
            else:
                if (item["name"] in object_relations and len(object_relations[item["name"]]) > 0):
                    item_found = object_relations[item["name"]].pop()
                    game_state["keys_collected"].append(item_found)
                    output += "You find " + item_found["name"] + "."
                else:
                    output += "There isn't anything interesting about it."
            print(output)
            break

    if (output is None):
        print("The item you requested is not found in the current room.")

    if (next_room):
        dialogue_box()
        play_room(next_room)

    else:
        play_room(current_room)

import tkinter as tk
from tkinter import messagebox as mb

def dialogue_box():

    
    leave = tk.Tk()               # Create instance 
    leave.title("WANNA LEAVE?") 


    def answer():
        mb.showerror("Yes", "You are getting outside!")


    tk.Button(text="\n\n\n                           Click to go to the next room.                        \n\n\n", command=answer, bg='cyan').pack(fill=tk.X)
    tk.mainloop()

game_state = INIT_GAME_STATE.copy()

start_game()

queen_bed = {
    "name": "queen bed",
    "type": "furniture",
}

door_b = {
    "name": "door b",
    "type": "door",
}

door_c = {
    "name": "door c",
    "type": "door",
}


key_b = {
    "name": "key for door b",
    "type": "key",
    "target": door_b,
}

bedroom_1 = {
    "name": "bedroom 1",
    "type": "room",
}

outside = {
  "name": "outside"
}

all_rooms = [bedroom_1, outside]

all_doors = [door_b, door_c]

# define which items/rooms are related

object_relations = {
    "bedroom 1": [queen_bed, door_b, door_c],
    "queen bed": [key_b],
    "outside": [door_b],
    "door b": [bedroom_1, outside]
}

# define game state. Do not directly change this dict.
# Instead, when a new game starts, make a copy of this
# dict and use the copy to store gameplay state. This
# way you can replay the game multiple times.

game_state = INIT_GAME_STATE.copy()

play_room(bedroom_1)

#BEDROOM 2

# define rooms and items

double_bed = {
    "name": "double bed",
    "type": "furniture",
}

dresser = {
    "name": "dresser",
    "type": "furniture",
}

door_b = {
    "name": "door b",
    "type": "door",
}


key_c = {
    "name": "key for door c",
    "type": "key",
    "target": door_c,
}

door_d = {
    "name": "door d",
    "type": "door"
}

key_d = {
    "name": "key for door d",
    "type": "key",
    "target": door_d,
}


bedroom_2 = {
    "name": "bedroom 2",
    "type": "room",
}

outside = {
  "name": "outside"
}

all_rooms = [bedroom_2, outside]

all_doors = [door_b]

# define which items/rooms are related

object_relations = {
    "bedroom 2": [double_bed, dresser, door_b],
    "double bed": [key_c],
    "dresser": [key_d],
    "outside": [door_b],
    "door b": [bedroom_2, outside]
}

# define game state. Do not directly change this dict.
# Instead, when a new game starts, make a copy of this
# dict and use the copy to store gameplay state. This
# way you can replay the game multiple times.



game_state = INIT_GAME_STATE.copy()

play_room(bedroom_2)

#LIVING ROOM!!!!!!


# define rooms and items

dining_table = {
    "name": "dining table",
    "type": "furniture",
}

door_c = {
    "name": "door c",
    "type": "door",
}

door_d = {
    "name": "door d",
    "type": "door",
}

living_room = {
    "name": "living room",
    "type": "room",
}

outside = {
  "name": "outside"
}

all_rooms = [living_room, outside]

all_doors = [door_c, door_d]

# define which items/rooms are related

object_relations = {
    "living room": [dining_table, door_c, door_d],
    "outside": [door_d],
    "door d": [living_room, outside]
}

# define game state. Do not directly change this dict.
# Instead, when a new game starts, make a copy of this
# dict and use the copy to store gameplay state. This
# way you can replay the game multiple times.



game_state = INIT_GAME_STATE.copy()

play_room(living_room)

winner_image.show()
