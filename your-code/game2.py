from threading import Thread
from multiprocessing import Process
import sys
import time

import random
import os


# define rooms and items
#gameroom

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

safe = {
    "name": "safe",
    "type": "furniture",
}

game_room = {
    "name": "game room",
    "type": "room",
}

outside = {
  "name": "outside"
}

#bedroom1
bedroom1 = {
    "name": "bedroom 1",
    "type": "room", 
}

queenbed = {
    "name": "queen bed",
    "type": "furniture", 
}

door_b = {
    "name": "door b",
    "type": "door", 
}

key_b = {
    "name": "key b",
    "type": "key",
    "target": door_b, 

}
#bedroom2
bedroom2 = {
    "name": "bedroom 2",
    "type": "room", 
}

doublebed = {
    "name": "double bed",
    "type": "furniture", 
}

dresser = {
    "name": "dresser",
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


key_c = {
    "name": "key c",
    "type": "key",
    "target": door_c, 
}

key_d = {
    "name": "key d",
    "type": "key",
    "target": door_d, 
}

# living room

living_room = {
    "name": "living room",
    "type": "room", 
}

dinning_table = {
    "name": "dinning table",
    "type": "furniture", 
}



all_rooms = [game_room, bedroom1, bedroom2, living_room, outside]

all_doors = [door_a, door_b, door_c, door_d]

# define which items/rooms are related

object_relations = {
    "game room": [couch, safe, door_a],
    "safe": [key_a],
    "door a": [game_room, bedroom1],

    "bedroom 1":[queenbed, door_b, door_c],
    "queen bed":[key_b],
    "door b": [bedroom1, bedroom2],

    "bedroom 2":[doublebed, dresser, door_b],
    "double bed":[key_c],
    "dresser":[key_d],
    
    "living room":[dinning_table, door_d],
    "door c":[bedroom1, living_room],
    "door d":[living_room, outside],

    "outside": [door_d],

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

def game_return(): 
    INIT_GAME_STATE["keys_collected"]= []
    INIT_GAME_STATE["current_room"]= game_room

    object_relations["safe"] = [key_a]
    object_relations["queen bed"] = [key_b]
    object_relations["double bed"] = [key_c]
    object_relations["dresser"] = [key_d]

    global game_state
    game_state = INIT_GAME_STATE.copy()
    
    start_game()

def dresser_game():
    print("there is a thief inside the dresser that holds the key! fight him using the folow objects:" )
    print("Enter choice \n 0. hammer \n 1. axe \n 2. knife \n")
    power_dict = {"hammer": 2, "axe":3, "knife":1}
    computer_pontuation=0
    man_pontuation=0
    
    for i in range (0,3):
        choice = int(input("Choice: "))
        computer_choice = random.randint(0, 2)
        dict_k = list(power_dict.keys())
        if choice == computer_choice:
            computer_pontuation = computer_pontuation + power_dict[dict_k[computer_choice]]
            man_pontuation = man_pontuation + power_dict[dict_k[choice]]
        elif choice < computer_choice:
            computer_pontuation = computer_pontuation + power_dict[dict_k[computer_choice]]
        else:
            man_pontuation = man_pontuation + power_dict[dict_k[choice]]
                    
    if computer_pontuation < man_pontuation:
        return print("you killed the theif, you can colect the key")
    else:
        game_return()  

# define the countdown func.
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        time.sleep(1)
        if timer == '03:00':
            print('\n3 mins left')
        if timer == '02:00':
            print('\n2 mins left')
        if timer == '01:00':
            print('\n1 min left')
        if timer == '00:30':
            print('\n30 sec left')
        if timer == '00:10':
            print('\n10 sec left')
        t -= 1
    print("\nYou couldn't get out of the Kame House and your planet is destroyed :( \nGAME OVER!!!!")

# define the safe game
def safe_game():
    num = random.randint(1, 3)
    print('Guess the correct number to open the safe: \nPut in a number between 1 and 3. You have ONLY 2 attempts to get it right.')
    attempt = 2
    msg = 'You Lost! \nGAME OVER!!!'
    while attempt > 0:
        user_input = int(input('Enter Number: '))
        if user_input == num:
            msg = 'CONGRATULATIONS! You Won!'
            break
        else:
            print(f'Try again! {attempt} attempt left.')
            attempt -= 1
            continue
    print(msg)

def linebreak():
    """
    Print a line break
    """
    print("\n\n")

def start_game():
    """
    Start the game
    """
    print("Son Goku, you wake up on a couch and find yourself in Kame House with all windows blocked. You don't remember why you are here and what had happened before. You feel some unknown danger is approaching and you must get out of the house in order to safe the planet, NOW!")
    play_room(game_state["current_room"])

def play_room(room):
    """
    Play a room. First check if the room being played is the target room.
    If it is, the game will end with success. Otherwise, let player either 
    explore (list all items in this room) or examine an item found here.
    """
    game_state["current_room"] = room
    if(game_state["current_room"] == game_state["target_room"]):
        print("Congrats! You escaped the room!")
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
            if item["name"] == 'safe':
                safe_game()
            output = "You examine " + item_name + ". "
            if item == dresser:
                dresser_game()
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

game_state = INIT_GAME_STATE.copy()



if __name__ == '__main__':
    t1 = Thread(target=countdown, args=(180,)) #Setting for timer in seconds
    t2 = Thread(target=start_game)
    t1.start() #Calls first function
    t2.start() #Calls second function to run at same time

    t1.join()
    if t1.is_alive() == False:
        os._exit(0) #