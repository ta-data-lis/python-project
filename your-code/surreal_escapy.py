#!/usr/bin/env python
# coding: utf-8

# In[20]:


# import modules

import time
import random

# define rooms and items

nails = {
    "name": "bed of nails",
    "type": "furniture",
}

desk = {
    "name": "escritoire desk",
    "type": "furniture",
}

veil = {
    "name": "veil of darkness",
    "type": "door",
}

candle = {
    "name": "candle-light",
    "type": "key",
    "target": veil,
}

insomnia_room = {
    "name": "the room of insomnia",
    "type": "room",
}

chest = {
    "name": "steel chest",
    "type": "furniture",
}

hole = {
    "name": "black hole",
    "type": "door",
}

mouth = {
    "name": "open mouth",
    "type": "door",
}

diamond = {
    "name": "diamond",
    "type": "key",
    "target": hole,
}

diamond_room = {
    "name": "diamond room",
    "type": "room",
}

rqbed = {
    "name": "Red Queen bed",
    "type": "furniture",
}

wkdresser = {
    "name": "White Knight dresser",
    "type": "furniture",
}

s_pill = {
    "name": "small pill",
    "type": "key",
    "target": mouth,
}

alice_room = {
    "name": "the room of Alice",
    "type": "room",
}

bag = {
    "name": "bag of problems",
    "type": "furniture",
}

arch = {
    "name": "arch of life",
    "type": "door",
}

l_pill = {
    "name": "large pill",
    "type": "key",
    "target": arch,
}

reasoning_room = {
    "name": "the room of reasoning",
    "type": "room",
}

outside = {
  "name": "outside"
}

all_rooms = [insomnia_room, diamond_room, alice_room, reasoning_room, outside]

all_doors = [veil, hole, mouth, arch]

# define which items/rooms are related

object_relations = {
    "the room of insomnia": [nails, desk, veil],
    "bed of nails": [],
    "escritoire desk": [],
    "outside": [arch],
    "veil of darkness": [insomnia_room, diamond_room],
    "diamond room": [chest, veil, hole, mouth],
    "steel chest": [diamond],
    "black hole": [diamond_room, alice_room],
    "the room of Alice": [rqbed, wkdresser, hole],
    "Red Queen bed": [],
    "White Knight dresser": [],
    "open mouth": [diamond_room, reasoning_room],
    "the room of reasoning": [bag, arch],
    "arch of life": [reasoning_room, outside],
}

# randomly assign thr first key to either of the furniture of the room
# randomly assign the third to either of the furniture of the room
# assign the fourth key to the empty furniture of the room

candle_location = random.choice(["bed of nails", "escritoire desk"])
object_relations[candle_location].append(candle)

s_pill_location = random.choice(["Red Queen bed", "White Knight dresser"])
object_relations[s_pill_location].append(s_pill)

if s_pill_location == "Red Queen bed":
    l_pill_location = "White Knight dresser"
else:
    l_pill_location = "White Knight dresser"
object_relations[l_pill_location].append(l_pill)

# define game state. Do not directly change this dict. 
# Instead, when a new game starts, make a copy of this
# dict and use the copy to store gameplay state. This 
# way you can replay the game multiple times.

INIT_GAME_STATE = {
    "current_room": insomnia_room,
    "keys_collected": [],
    "target_room": outside
}


# In[21]:


def linebreak():
    """
    Print a line break
    """
    print("\n\n")

def start_game():
    """
    Start the game
    Set a timer for start and end in order to give a message to the player of the time they wandered
    """
    print("You needed to sleep but you couldn't take any sleep. Waking up on a bed of nails, you understand why. You decide to get up and struggle with the dark forces that lurk in the clear moonlight (there's no electricity and you can barely see, but somehow your senses feel...enhanced!). Deep inside you, you sense some unknown dangerous mental movement approaching and you feel an urge to run as far as possible NOW!")
    
    start_time = time.time()
    play_room(game_state["current_room"])
    end_time = time.time()

    print(player_name,"you took",end_time-start_time,"to get out!!!")
    
    play_room(game_state["current_room"])

def play_room(room):
    """
    Play a room. First check if the room being played is the target room.
    If it is, the game will end with success. Otherwise, let player either 
    explore (list all items in this room) or examine an item found here.
    """
    game_state["current_room"] = room
    if(game_state["current_room"] == game_state["target_room"]):
        print("Congrats! You escaped the room (but you cannot escape yourself)!")
    else:
        print("You are now in " + room["name"])
        intended_action = input("What would you like to do? Type 'explore', 'check' or 'examine': ").strip()
        if intended_action == "explore":
            explore_room(room)
            play_room(room)
        elif intended_action == "check":
            explore_self(game_state)
            play_room(room)
        elif intended_action == "examine":
            examine_item(input("What would you like to examine?").strip())
        else:
            print("Not sure what you mean. Perhaps drink a glass of water and then re-type 'explore', 'check' or 'examine'.")
            play_room(room)
        linebreak()

def explore_self(game_state):
    """
    Check which keys the player has collected so far.
    """
    keys_collected = game_state["keys_collected"]
    if not keys_collected:
        print("You haven't collected anything yet. Empty pockets. You wonder why.")
    else:
        print("You have collected the following bunch of weird stuff:")
        for key_obj in keys_collected:
            print(key_obj["name"])
    return keys_collected        
        
def explore_room(room):
    """
    Explore a room. List all items belonging to this room.
    """
    items = [i["name"] for i in object_relations[room["name"]]]
    print("You explore the room. This is " + room["name"] + ". You find " + ", ".join(items))

def get_next_room_of_door(door, current_room):
    """
    From object_relations, find the two rooms connected to the given door.
    Return the room that is not the current_room.
    """
    connected_rooms = object_relations[door["name"]]
    for room in connected_rooms:
        if(not current_room == room):
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
        if(item["name"] == item_name):
            output = "You examine " + item_name + ". "
            if(item["type"] == "door"):
                have_key = False
                for key in game_state["keys_collected"]:
                    if(key["target"] == item):
                        have_key = True
                if(have_key):
                    output += "You go through it using one of the bizarre objects you carry."
                    next_room = get_next_room_of_door(item, current_room)
                else:
                     output += "You can't go though no matter how hard you try. It would help if you had something to use as a key..."
            else:
                if(item["name"] in object_relations and len(object_relations[item["name"]])>0):
                    item_found = object_relations[item["name"]].pop()
                    game_state["keys_collected"].append(item_found)
                    output += "You find " + item_found["name"] + "."
                else:
                    output += "Despite your continuous starring, there is nothing interesting about it. Move along!"
            print(output)
            break

    if(output is None):
        print("The item you requested is not found in the current room.")
    
    if(next_room and input("Do you want to go to the next room? Enter 'yes' or 'no'").strip() == 'yes'):
        play_room(next_room)
    else:
        play_room(current_room)


# In[22]:


game_state = INIT_GAME_STATE.copy()
player_name = input("Please insert your name: ")
start_game()


# In[ ]:




