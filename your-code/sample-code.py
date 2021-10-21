



#from pygame import mixer
from pygame import mixer

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
    "outside": [fenix_door],
    "snake door": [hogwarts, azkaban],
    #"snake door":[dumbledore_chamber],
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

    print(""" ************Welcome to Hogwards Escape Room*************
    
    Welcome to our new Hogwarts Escape Room! Before we begin our journey, we would like to say a few words...
    
    Choose wisely your paths and remember your spells... 
    """)

    play_room(game_state["current_room"])

def play_room(room):
    """
    Play a room. First check if the room being played is the target room.
    If it is, the game will end with success. Otherwise, let player either 
    explore (list all items in this room) or examine an item found here."""

    game_state["current_room"] = room
    if(game_state["current_room"] == game_state["target_room"]):
        mixer.music.pause()
        print("Congrats! You escaped the room!")
    else:
#         if room["name"] == game_state["current_room"]:    
#         print("\n You are still in: " + room["name"])
#         else:
        print("\n Let's proceed! You are now in: " + room["name"])
        #intended_action = input("What would you like to do? Type 'explore' or 'examine'?").strip()
        choice = input("""Choose one of these options:
    
                      A: Explore what's in the room
                      B: Examine what you want to
                      

                      Please enter your choice: """)
        if choice.upper() == "A":
            explore_room(room)
            play_room(room)
        elif choice.upper() == "B":
            examine_item(input(" \n What would you like to examine? \n").strip())
        else:
            print("\n That is a muggle error! You must only type either A or B.")

            play_room(room)
        linebreak()

def explore_room(room):
    """
    Explore a room. List all items belonging to this room.
    """
    items = [i["name"] for i in object_relations[room["name"]]]
    print("\n You explore the room. This is " + room["name"] + ". You find these objects: \n- " + "\n- ".join(items))


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

            output = "\n You examine " + item_name + ". "

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
            see_again= input(("""Do you wish to examine more things?
    
                       Y: To examine more things
                       N: Stop examine
                      

                       Please enter your choice: """))
            if see_again.upper() == 'Y':
                examine_item(input(" \n What would you like to examine? \n").strip()) 
            elif see_again.upper() == 'N':
                continue
            else:
                see_again
            break

    if(output is None):
        print("You must have eaten some Bertie Botts Beansb and are seeing things twisted. That item isn't in the current room.")
    
    if(next_room and input("Do you wish to go to another Hogwards room? Write 'yes' to enter  or write anything else to go to main menu.").strip().lower() == 'yes'):

        play_room(next_room)
    else:
        play_room(current_room)
        
game_state = INIT_GAME_STATE.copy()

start_game()

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:
