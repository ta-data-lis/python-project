# define items in the_shire (game_room)

bilbo_house = {
    "name": "Bilbo's house",
    "type": "furniture",
}

safe_way_a = {
    "name": "road a",  #check if error due to different naming
    "type": "door",
}

map_a = {
    "name": "map a",
    "type": "key",
    "target": safe_way_a,   
}

sam_house = {
    "name": "Sam's house",
    "type": "furniture",
}

the_shire = {
    "name": "The Shire",
    "type": "room",
}


# define items in gondor (bedroom_1)

safe_way_b = {
    "name": "road b",
    "type": "door",
}

rivendell = {
    "name": "Rivendell",
    "type": "furniture",
}

map_b = {
    "name": "map b",
    "type": "key",
    "target": safe_way_b,
}


safe_way_c = {
    "name": "road c",
    "type": "door",
}

gondor = {
    "name": "Gondor",
    "type": "room",
}

# this is not an area - definition of safe_way d before defining map d

safe_way_d = {
    "name": "road d",
    "type": "door",
}

# define items in Rohan (bedroom_2)

map_c = {
    "name": "map c",
    "type": "key",
    "target": safe_way_c,
}

map_d = {
    "name": "map d",
    "type": "key",
    "target": safe_way_d,
}

moria = {
    "name": "Moria",
    "type": "furniture",
}

helm = {
    "name": "Helm's Deep",
    "type": "furniture",
}

safe_way_b = {
    "name": "road b",
    "type": "door",
}

rohan = {
    "name": "Rohan",
    "type": "room",
}


# define items in Mordor (living_room)

eye_tower = {
    "name": "Eye Tower",
    "type": "furniture",
}

safe_way_c = {
    "name": "road c",
    "type": "door",
}

safe_way_d = {
    "name": "road d",
    "type": "door",
}

mordor = {
    "name": "Mordor",
    "type": "room",
}


# define outside

outside = {
  "name": "Mount Doom"
}


# define all rooms and doors


all_rooms = [the_shire, gondor, rohan, mordor, outside]  # check if it must be changed to all_areas

all_doors = [safe_way_a, safe_way_b, safe_way_c, safe_way_d]



# define which items/rooms are related

object_relations = {
    "The Shire": [bilbo_house, sam_house, safe_way_a],
    "Gondor": [rivendell, safe_way_a, safe_way_b, safe_way_c],
    "Rohan": [moria, helm, safe_way_b],
    "Mordor": [eye_tower, safe_way_c, safe_way_d],
    "Mount Doom": [safe_way_d],
    "Sam's house": [map_a],
    "Rivendell": [map_b],
    "Moria": [map_c],
    "Helm's Deep": [map_d],
    "road a": [the_shire, gondor],
    "road b": [gondor, rohan],
    "road c": [gondor, mordor],
    "road d": [mordor, outside]
}

# define game state. Do not directly change this dict. 
# Instead, when a new game starts, make a copy of this
# dict and use the copy to store gameplay state. This 
# way you can replay the game multiple times.

INIT_GAME_STATE = {
    "current_room": the_shire,
    "keys_collected": [],
    "target_room": outside
}


def linebreak():
    """
    Print a line break
    """
    print("\n\n")

def start_game(): # change the script
    """
    Start the game
    """
    print("You wake up on a couch and find yourself in a strange house with no windows which you have never been to before. You don't remember why you are here and what had happened before. You feel some unknown danger is approaching and you must get out of the house, NOW!")
    play_room(game_state["current_room"])   

def play_room(room):
    """
    Play a room. First check if the room being played is the target room.
    If it is, the game will end with success. Otherwise, let player either 
    explore (list all items in this room) or examine an item found here.
    """
    game_state["current_room"] = room
    if(game_state["current_room"] == game_state["target_room"]):
        print("Congrats! You destroyed the Ring!")  # change text?
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
    print("You explore the area. This is " + room["name"] + ". You find " + ", ".join(items))

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
                    output += "You enter an area with a map you have."
                    next_room = get_next_room_of_door(item, current_room)
                else:
                    output += "You don't have the map to find the safe way."
            else:
                if(item["name"] in object_relations and len(object_relations[item["name"]])>0):
                    item_found = object_relations[item["name"]].pop()
                    game_state["keys_collected"].append(item_found)
                    output += "You find " + item_found["name"] + "."
                else:
                    output += "There isn't anything interesting in this place."
            print(output)
            break

    if(output is None):
        print("The place you requested is not found in the current area.")
    
    if(next_room and input("Do you want to go to the next area? Enter 'yes' or 'no'").strip() == 'yes'):
        play_room(next_room)
    else:
        play_room(current_room)



game_state = INIT_GAME_STATE.copy()
start_game()

