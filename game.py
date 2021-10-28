
# define rooms and items
import time
import pygame
from playsound import playsound
from random import randrange

couch = {
    "name": "couch",
    "type": "furniture",
}
ghost = {
    "name": "ghost",
    "type": "furniture",
        }
door_a = {
    "name": "door a",
    "type": "door",
}
door_b = {
    "name": "door b",
    "type": "door",
}
door_c = {
    "name": "door c",
    "type": "door",
}
door_d = {
    "name": "door d",
    "type": "door",
}
key_a = {
    "name": "key for door a",
    "type": "key",
    "target": door_a,
}
key_b = {
    "name": "key for door b",
    "type": "key",
    "target": door_b,
}
key_c = {
    "name": "key for door c",
    "type": "key",
    "target": door_c,
}
key_d = {
    "name": "key for door d",
    "type": "key",
    "target": door_d,
}
zombie = {
    "name": "zombie",
    "type": "furniture",
}
werewolf = {
    "name": "werewolf",
    "type": "furniture",
}
dracula = {
    "name": "dracula",
    "type": "furniture",
}
frankenstein = {
    "name": "frankenstein",
    "type": "furniture",
}
game_room = {
    "name": "game room",
    "type": "room",
}
bedroom_1 = {
        "name": "bedroom 1",
        "type": "room",
        }
bedroom_2 = {
        "name": "bedroom 2",
        "type": "room",
        }
living_room = {
        "name": "living room",
        "type": "room",
        }
outside = {
  "name": "outside"
}
all_rooms = [game_room, bedroom_1, bedroom_2, living_room, outside]
all_doors = [door_a, door_b, door_c, door_d]

def tic_tac():
    playsound('sounds/tic-tac.mp3')
def fail_sound():
    playsound('sounds/fail.wav')
def congrats_sound():
    playsound('sounds/congrats.wav')
def happy_halloween():
    playsound('sounds/happyhalloween.mp3')


def zombie_enigma():
    timeout = time.time() + 20   # 20 seconds from now
    result = False
    while True:
        x = input('You have 20 seconds! guess a number below 10:')
        if time.time() > timeout:
            print('too slow')
            break
        elif int(x) == 6:
            print('good job!')
            result = True
            break
        else:
            continue
    return result

def ghost_enigma():
    mistake_count = 0
    chances = 3
    while mistake_count  != 3 :
        ghost = input("Which room do the ghosts hate to go to? be careful you will only have 3 chances! ")
        if ghost.strip().lower() == 'living room' :
                print("Congrats! it's an easy one.")
                return True
        else :
                mistake_count += 1
                chances = chances - mistake_count
                print("No, that's not the answer")
                if mistake_count == 3:
                    print("Too many mistakes. GAME OVER.")
                    start_game()


def dracula_enigma():
    answer = input('You want to kill Dracula to retrieve the key.\nYou see a window with the curtains closed. What do you do?').lower()
    key_words = ['light','sunlight', 'sun', 'open']
    result = False
    for word in key_words:
        if word in answer.split():
            result =  True
        else:
            continue
    if result:
        print('Well done! The sunlight coming through the window kills Dracula!')
    else:
        print('You failed! Dracula sucks your blood. GAME OVER')
        start_game()
    return result

def werewolf_enigma():
    mistake_count = 0
    chances = 3
    while mistake_count  != 3 :
        werewolf = input("The werewolf is asking you to solve a simple math problem in exchange for a key. \nYou have 3 chances. What is 10 x 10 + 1? ")
        if int(werewolf) == 101 :
                print("Congrats! it's an easy one.")
                return True
        else :
                mistake_count += 1
                chances = chances - mistake_count
                print("No, that's not the answer")
                if mistake_count == 3:
                    print("Too many mistakes. GAME OVER.")
                    start_game()

# define which items/rooms are related

object_relations = {
    "game room": [couch, zombie, door_a],
    "bedroom 1": [ghost, door_a,door_b, door_c],
    "bedroom 2": [werewolf, dracula, door_b],
    "living room": [frankenstein, door_c, door_d],
    "zombie": [key_a, zombie_enigma],
    "dracula": [key_d, dracula_enigma],
    "werewolf": [key_c, werewolf_enigma],
    "outside": [door_a],
    "door a": [game_room, bedroom_1],
    "door b": [bedroom_1, bedroom_2],
    "door c": [bedroom_1, living_room],
    "door d": [living_room, outside],
    "ghost" : [key_b, ghost_enigma]
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
    print("You wake up on a couch and find yourself in a strange haunted house with no windows which you have never been to before. You don't remember why you are here and what had happened before. You feel some unknown danger is approaching and you must get out of the house, NOW!")
    show_image("hauntedhouse")
    play_room(game_state["current_room"])

def play_room(room):
    """
    Play a room. First check if the room being played is the target room.
    If it is, the game will end with success. Otherwise, let player either
    explore (list all items in this room) or examine an item found here.
    """
    game_state["current_room"] = room
    if(game_state["current_room"] == game_state["target_room"]):
        show_image('exit')
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
            output = "You encounter " + item_name + ". "
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
                    fail_sound()
            else:
                show_image(str(item["name"]))
                if(item["name"] in object_relations and len(object_relations[item["name"]][0])>0):
                    if object_relations[item["name"]][1]():
                        item_found = object_relations[item["name"]].pop(0)
                        game_state["keys_collected"].append(item_found)
                        output += "You find " + item_found["name"] + "."
                    else:
                        output += "You failed"
                else:
                    output += "There isn't anything interesting about it."
            print(output)
            break
    if(output is None):
        print("The item you requested is not found in the current room.")
    if(next_room and input("Do you want to go to the next room? Enter 'yes' or 'no'").strip() == 'yes'):
        congrats_sound()
        play_room(next_room)
    else:
        play_room(current_room)

def show_image(name):
  
    # activate the pygame library .
    # initiate pygame and give permission
    # to use pygame's functionality.
    pygame.init()
  
    # define the RGB value
    # for white colour
    black = (0,0,0)
    running = True
  
    # assigning values to X and Y variable
    X = 600
    Y = 600
  
    # create the display surface object
    #of specific dimension..e(X, Y).
    display_surface = pygame.display.set_mode((X, Y ))
  
    # create a surface object, image is drawn on it.
    image = pygame.image.load('pics/' + name +'.jpg')
  
    # infinite loop
    while running :
  
        # completely fill the surface object
        # with white colour
        display_surface.fill(black)
  
        # copying the image surface object
        # to the display surface object at
        # (0, 0) coordinate.
        display_surface.blit(image, (0, 0))


        # Draws the surface object to the screen.  
        pygame.display.update() 
        playsound('pics_sound/' +name + '.mp3')
        running = False
        pygame.quit()
        break




game_state = INIT_GAME_STATE.copy()

start_game()