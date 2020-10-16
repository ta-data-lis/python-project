# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 06:46:02 2020

@author: ivana
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 11:25:23 2020

@author: ivanaex
"""
from PIL import Image
import pygame
from pygame import mixer
#Winner Image
winner_image = Image.open(r"C:\Users\ivana\Documents\python-project\python-project\Freedom.png")

# define rooms and items

bush = {
    "name": "bush",
    "type": "thing",
}

oak_tree = {
    "name": "oak tree",
    "type": "thing",
}


rock = {
    "name": "rock",
    "type": "thing",
}

birch_tree = {
    "name": "birch tree",
    "type": "thing",
}

cottage = {
    "name": "cottage",
    "type": "thing",
}

squirell = {
    "name": "squirrel",
    "type": "thing",
}

blue_bridge = {
    "name": "blue bridge",
    "type": "bridge",
}

yellow_bridge = {
    "name": "yellow bridge",
    "type": "bridge",
}


red_bridge = {
    "name": "red bridge",
    "type": "bridge",
}


black_bridge = {
    "name": "black bridge",
    "type": "bridge"
}

daisy = {
    "name": "flower for blue bridge",
    "type": "flower",
    "target": blue_bridge,
}

gardenia = {
    "name": "flower for yellow bridge",
    "type": "flower",
    "target": yellow_bridge,
}

chrysanthemum = {
    "name": "flower for red bridge",
    "type": "flower",
    "target": red_bridge,
}


lily = {
    "name": "flower for black bridge",
    "type": "flower",
    "target": black_bridge,
}

forest = {
    "name": "forest",
    "type": "place",
}

meadow = {
    "name": "meadow",
    "type": "place",
}

pasture = {
    "name": "pasture",
    "type": "place",
}

field = {
    "name": "field",
    "type": "place",
}

outside = {
    "name": "outside"
}

all_rooms = [forest, meadow, pasture, field]

all_doors = [blue_bridge, yellow_bridge, red_bridge, black_bridge]

# define which items/rooms are related

object_relations = {
    "forest": [bush, oak_tree, blue_bridge],
    "oak tree": [daisy],
    "blue bridge": [forest, meadow],
    "meadow": [rock, blue_bridge, yellow_bridge, red_bridge],
    "rock": [gardenia],
    "yellow bridge": [meadow, pasture],
    "pasture": [birch_tree, cottage, yellow_bridge],
    "birch tree": [chrysanthemum],
    "cottage": [lily],
    "red bridge": [meadow, field],
    "field": [squirell, red_bridge, black_bridge],
    "outside": [black_bridge],
    "black bridge": [field, outside]
}

# define game state. Do not directly change this dict.
# Instead, when a new game starts, make a copy of this
# dict and use the copy to store gameplay state. This
# way you can replay the game multiple times.

INIT_GAME_STATE = {
    "current_room": forest,
    "flowers_collected": [],
    "target_room": outside
}

def linebreak():
    """
    Print a line break
    """
    print("\n\n")
    
def music():
    mixer.init()
    mixer.music.load('PTY_-_Hero_Quest_-_Piano.mp3')
    mixer.music.play()


def start_game():
    """
    Start the game
    """
    print(
        "Good morning! You just woke up in the middle of a beautiful forest!\nBut it sounds like there is a bear nearby...\nMaybe get a move on and get somewhere safe!.\nHINT: Seems like a good day for some flower picking!")
    music()
    play_room(game_state["current_room"])


def play_room(place):
    """
    Play a room. First check if the room being played is the target room.
    If it is, the game will end with success. Otherwise, let player either
    explore (list all items in this room) or examine an item found here.
    """
    game_state["current_room"] = place
    if (game_state["current_room"] == game_state["target_room"]):
        print("Good job! Crossing the bridge!")
    else:
        print("You are now in " + place["name"] + ".\nDon't forget the flowers!")
        intended_action = input("There are some things around. Try to check them by typing: check! ").strip()
        if intended_action == "check":
            explore_room(place)
            examine_item(input("What would you like to check? ").strip())
            #napisi novu funkciju koja ce da pita sta hoces da explore odmah
            #furniture_explore()
            #play_room(room)
        #elif intended_action == "examine":
            #examine_item(input("What would you like to examine? ").strip())
        else:
            print("Hmmmmmmmm. You confused me. And the bear seems to be closer. Let me help you out. Type: check. ")
            play_room(place)
        linebreak()

#def furniture_explore(name):
 #   items = [i["name"] for i in object_relations[room["name"]]]
  #  print("What do you want to . This is " + room["name"] + ". You find " + ", ".join(items) + ".")


def explore_room(place):
    """
    Explore a room. List all items belonging to this room.
    """
    items = [i["name"] for i in object_relations[place["name"]]]
    print("You walk around. This is " + place["name"] + ". You find " + ", ".join(items) + ".")


def get_next_room_of_door(bridge, current_room):
    """
    From object_relations, find the two rooms connected to the given door.
    Return the room that is not the current_room.
    """
    connected_rooms = object_relations[bridge["name"]]
    for place in connected_rooms:
        if (not current_room == place):
            return place


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
            output = "You search " + item_name + ". "
            if (item["type"] == "bridge"):
                have_key = False
                for flower in game_state["flowers_collected"]:
                    if (flower["target"] == item):
                        have_key = True
                if (have_key):
                    output += "You cross the bridge because you collected a beautiful flower."
                    next_room = get_next_room_of_door(item, current_room)
                else:
                    output += "Seems like you cannot cross the bridge right now. Did I mention how much I like flowers?\nMaybe you could find me one?"
            else:
                if (item["name"] in object_relations and len(object_relations[item["name"]]) > 0):
                    item_found = object_relations[item["name"]].pop()
                    game_state["flowers_collected"].append(item_found)
                    output += "You find " + item_found["name"] + "."
                else:
                    output += "I don't like it, check something else."
            print(output)
            break

    if (output is None):
        print("I think you are confused. That doesn't exist here.")

    if (next_room):
        dialogue_box()
        play_room(next_room)

    else:
        play_room(current_room)

import tkinter as tk
from tkinter import messagebox as mb

def dialogue_box():

    
    leave = tk.Tk()               # Create instance 
    leave.title("CROSS THE BRIDGE") 


    def answer():
        mb.showerror("Yes", "You are further from the bear!")


    tk.Button(text="\n\n\n                           Click to cross the bridge.                        \n\n\n", command=answer, bg='blue').pack(fill=tk.X)
    tk.mainloop()

game_state = INIT_GAME_STATE.copy()

start_game()


winner_image.show()
