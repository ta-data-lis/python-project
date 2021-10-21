#!/usr/bin/env python
# coding: utf-8

# In[1]:


#from pygame import mixer
from pygame import mixer


def linebreak():
    """
    Print a line break
    """
    print("\n\n")

def start_game():
    """
    Start the game
    """
    # Starting the mixer
    mixer.init()

    # Loading the song
    mixer.music.load("C:\\Users\\User\Desktop\\IronHack\\python-project\\your-code\\harry.mp3")

    # Setting the volume
    mixer.music.set_volume(0.7)

    # Start playing the song
    mixer.music.play()
    
    print("You wake up in Hogwards. You don't remember why you are here and what had happened before. You feel some unknown danger is approaching and you must get out of the house, NOW!")
    play_room(game_state["current_room"])

def play_room(room):
    """
    Play a room. First check if the room being played is the target room.
    If it is, the game will end with success. Otherwise, let player either 
    explore (list all items in this room) or examine an item found here.
    """    
    game_state["current_room"] = room
    if(game_state["current_room"] == game_state["target_room"]):
        #stop the music when ends the game
        mixer.music.pause()
        print("Congrats! You are free from the spells",)
    else:
        print("You are now in " + room["name"])
        intended_action = input("What would you like to do? Type 'explore' or 'examine'?").strip()
        if intended_action == "explore":
            explore_room(room)
            play_room(room)
        elif intended_action == "examine":
            examine_item(input("What would you like to examine?").strip())
        else:
            print("Not sure what you mean. Type 'explore' or 'examine'.")
            play_room(room)
        linebreak()

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
                    output += "You unlock it with a key you have."
                    next_room = get_next_room_of_door(item, current_room)
                else:
                    output += "It is locked but you don't have the key."
            else:
                if(item["name"] in object_relations and len(object_relations[item["name"]])>0):
                    item_found = object_relations[item["name"]].pop()
                    game_state["keys_collected"].append(item_found)
                    output += "You find " + item_found["name"] + "."
                else:
                    output += "There isn't anything interesting about it."
            print(output)
            break

    if(output is None):
        print("The item you requested is not found in the current room.")
    
    if(next_room and input("Do you want to go to the next room? Ener 'yes' or 'no'").strip() == 'yes'):
        play_room(next_room)
    else:
        play_room(current_room)
        


# In[2]:


nundu_door = {
    "name": "nundu door",
    "type": "door",
}


fenix_door = {
    "name": "fenix door",
    "type": "door",
}
wand = {
    "name": "wand",
    "type": "furniture",
}

dumbledore = {
    "name": "dumbledore",
    "type": "furniture",
}    
    


snake_door = {
    "name": "snake door",
    "type": "door",
}

key_snake= {
    "name": "key for snake door",
    "type": "key",
    "target": snake_door,
}

pensieve = {
    "name": "pensieve",
    "type": "furniture"
}
spell={
    "name":"\n \n Expectro patrono \n \n",
    "type": "key",
    "target":pensieve
    
}

mirror_enrised = {
    "name": "mirror enrised",
    "type": "furniture",
}

hogwarts = {
    "name": "hogwarts",
    "type": "room",
}

outside = {
  "name": "outside"
}

#DEFINE BEDROOM1

azkaban = {
    "name": "azkaban",
    "type": "room",
}

dwarves_door = {
    "name": "dwarves door",
    "type": "door",
}
elfes_door = {
    "name": "elfes door",
    "type": "door",
}

weasley_clock = {
    "name": "weasley clock",
    "type": "furniture",
}
key_dwarves={
    "name": "key for dwarves door",
    "type": "key",
    "target": dwarves_door
}



#DEFINE BEDROOM2

invisibility_cloak = {
    "name": "invisibility cloak",
    "type": "furniture"
}

key_elfes = {
    "name": "key for elfes door",
    "type": "key",
    "target": elfes_door,
}

key_fenix = {
    "name": "key for fenix door",
    "type": "key",
    "target": fenix_door
}
portkey = {
    "name": "portkey",
    "type": "furniture"
}

diagon_alley = {
    "name": "diagon alley",
    "type": "room",
}

key_nundu = {
    "name": "key for nundu door",
    "type": "key",
    "target": nundu_door,
}

# define LIVINGROOM


broonstick = {
    "name": "broonstick",
    "type": "furniture",
}


dumbledore_chamber = {
    "name": "dumbledore chamber",
    "type": "room",
}

outside = {
  "name": "outside"
}

all_rooms = [hogwarts, azkaban, diagon_alley, dumbledore_chamber,  outside]

all_doors = [snake_door, dwarves_door, elfes_door, nundu_door, fenix_door]

# define which items/rooms are related

object_relations = {
    "hogwarts": [dumbledore,wand, mirror_enrised, snake_door],
    "mirror enrised": [key_snake],
    "outside": [snake_door],
    "snake door": [hogwarts, azkaban],
    #"snake door":[outside],
    "weasley clock":[key_dwarves],
    "dwarves door":[azkaban, diagon_alley],
    "elfes door":[azkaban, dumbledore_chamber],
    "portkey":[key_elfes],
    "pensieve": [key_fenix, spell],
    "dinning table":[dumbledore_chamber],
    "fenix door":[dumbledore_chamber, outside],
    "azkaban":[weasley_clock,snake_door, dwarves_door, elfes_door],
    "diagon alley":[portkey, dwarves_door, nundu_door, invisibility_cloak],
    "dumbledore chamber":[broonstick, elfes_door, fenix_door,  pensieve],
    "invisibility cloak":[key_nundu],
    "nundu door":[diagon_alley, hogwarts],
    "dumbledore":[spell,]
}
   



# define game state. Do not directly change this dict. 
# Instead, when a new game starts, make a copy of this
# dict and use the copy to store gameplay state. This 
# way you can replay the game multiple times.

INIT_GAME_STATE = {
    "current_room": hogwarts,
    "keys_collected": [],
    "target_room": outside,

}


# In[ ]:


game_state = INIT_GAME_STATE.copy()

start_game()


# In[ ]:





# In[ ]:





# In[ ]:




