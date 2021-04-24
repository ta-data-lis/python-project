#Game

#Imports
import random

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

bedroom_1 = {
    "name": "bedroom 1",
    "type": "room",
}

queen_bed = {
    "name": "queen bed",
    "type": "furniture",
}

closet = {
    "name": "closet",
    "type": "furniture",
}

monster = {
    "name": "monster",
    "type": "furniture",
}

door_b = {
    "name": "door b",
    "type": "door",
}

key_b = {
    "name": "key for door b",
    "type": "key",
    "target": door_b,
}

door_c = {
    "name": "door c",
    "type": "door",
}

bedroom_2 = {
    "name": "bedroom 2",
    "type": "room",
}

double_bed = {
    "name": "double bed",
    "type": "furniture",
}

dresser = {
    "name": "dresser",
    "type": "furniture",
}

kitchen = {
    "name": "kitchen",
    "type": "room",
}

cup_board = {
    "name": "cup board",
    "type": "furniture",
}

fridge = {
    "name": "fridge",
    "type": "furniture",
}

cooker = {
    "name": "cooker",
    "type": "furniture",
}

door_d = {
    "name": "door d",
    "type": "door",
}

key_d = {
    "name": "key for door d",
    "type": "key",
    "target": door_d,
}

living_room = {
    "name": "living room",
    "type": "room",
}

dining_table = {
    "name": "dining table",
    "type": "furniture",
}

door_c = {
    "name": "door c",
    "type": "door",
}

key_c = {
    "name": "key for door c",
    "type": "key",
    "target": door_c,
}

door_e = {
    "name": "door e",
    "type": "door",
}

key_e = {
    "name": "key for door d",
    "type": "key",
    "target": door_e,
}

outside = {
  "name": "outside"
}

all_rooms = [game_room, outside,bedroom_1,bedroom_2,kitchen,living_room]

all_doors = [door_a,door_b,door_c,door_d,door_d]

# define which items/rooms are related

object_relations = {
    "game room": [couch, piano, door_a],
    "bedroom 1": [queen_bed, closet, door_a, door_b, door_c],
    "bedroom 2": [double_bed, dresser, door_b],
    "kitchen": [cup_board, fridge, cooker, door_c, door_d],
    "living room":[dining_table, door_d, door_e],
    "closet": [monster],
    "piano": [key_a],
    "queen bed": [key_b],
    "double bed": [key_c],
    "dresser": [key_d],
    "cup board": [key_e],
    "outside": [door_e],
    "door a": [game_room, bedroom_1],
    "door b": [bedroom_1, bedroom_2],
    "door c": [bedroom_1, kitchen],
    "door d": [kitchen, living_room],
    "door e": [living_room, outside],
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

#Tic Tac Toe

#define board
board = [i for i in range(0,9)]
winner=[]

# Function to print the board
def print_board():
    print(' ', board[0], ' | ', board[1], ' | ', board[2], ' ')
    print('-----------')
    print(' ', board[3], ' | ', board[4], ' | ', board[5], ' ')
    print('-----------')
    print(' ', board[6], ' | ', board[7], ' | ', board[8], ' ')

# Function to check if win condition is satisfied.
def win_check():
    if ((board[0] == "X" and board[4] == "X" and board[8] == "X") or (board[0] == "X" and board[3] == "X" and board[6] == "X") or (board[1] == "X" and board[4] == "X" and board[7] == "X") or (board[2] == "X" and board[5] == "X" and board[8] == "X") or (board[2] == "X" and board[4] == "X" and board[6] == "X") or (board[0] == "X" and board[1] == "X" and board[2] == "X") or (board[3] == "X" and board[4] == "X" and board[5] == "X") or (board[6] == "X" and board[7] == "X" and board[8] == "X")):
        print_board()
        winner.append("player")
    elif ((board[0] == "O" and board[4] == "O" and board[8] == "O") or (board[0] == "O" and board[3] == "O" and board[6] == "O") or (board[1] == "O" and board[4] == "O" and board[7] == "O") or (board[2] == "O" and board[5] == "O" and board[8] == "O") or (board[2] == "O" and board[4] == "O" and board[6] == "O") or (board[0] == "O" and board[1] == "O" and board[2] == "O") or (board[3] == "O" and board[4] == "O" and board[5] == "O") or (board[6] == "O" and board[7] == "O" and board[8] == "O")):
        print_board()
        winner.append("game")
    elif len([i for i in board if i != "X" and i != "O"]) == 0:
        print_board()
        winner.append("tie")
    else:
        current_player()


# define move
def current_player():
    print_board()
    a = board.count("X")
    b = board.count("O")
    if (int(a) > int(b)):
            possible_moves = [i for i in board if i != "X" and i != "O"]
            move = random.choice(possible_moves)
            monster_move = int(move)
            board[monster_move]="O"
            win_check()
    elif (int(a) == int(b) or int(a) == 0 ):
            player_choices = [i for i in board if i != "X" and i != "O" ]
            player_move = int(input("Make your move [0-8]: "))
            if player_move not in player_choices:
                print("Position not possible!")
            else:
                board[player_move]="X"
                win_check()
    else:
        print("error here")

def linebreak():
    """
    Print a line break
    """
    print("\n\n")

def start_game():
    """
    Start the game
    """
    print("You wake up on a couch and find yourself in a strange house with no windows which you have never been to before. You don't remember why you are here and what had happened before. You feel some unknown danger is approaching and you must get out of the house, NOW!")
    play_room(game_state["current_room"])

    
def new_start_game():
#    """
#    Start the game
#    """
    print("There's a monster at the closet, and now you will go back to the Game Room! Don`t be sad, you didn't lose your keys.")
    INIT_GAME_STATE = {"current_room": game_room,"keys_collected": [],"target_room": outside}
    game_state = INIT_GAME_STATE.copy()
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
        intended_action = input("What would you like to do? Type 'explore' or 'examine'?").lower().strip()
        if intended_action == "explore":
            explore_room(room)
            play_room(room)
        elif intended_action == "examine":
            examine_item(input("What would you like to examine?").lower().strip())
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
            elif(item["name"] == "closet"):
                #new_start_game()
                #output = "\nThere's a monster at the closet, and now you will go back to the Game Room! Don`t be sad, you didn't lose your keys"
                return print("\nThere's a monster at the closet! You lose and now you will go back to the Game Room!")
            elif(item["name"] == "dining table"):
                print("The Monster invites you for one last challenge!")
                while len(winner) == 0:
                    current_player()
                if len(winner) != 0:
                    if winner[0] == "player":
                        print("Congratulations! You defeat the Monster")
                    elif winner [0] == "game":
                        print("Nooo! The Monster win! Run!")
                    elif winner[0] == "tie":
                        print("It's a Tie!")
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
    
    if(next_room and input("Do you want to go to the next room? Enter 'yes' or 'no'").strip() == 'yes'):
        play_room(next_room)
    else:
        play_room(current_room)

        
while True:
    INIT_GAME_STATE = {"current_room": game_room,"keys_collected": [],"target_room": outside}
    game_state = INIT_GAME_STATE.copy() 
    start_game()
    object_relations = {
    "game room": [couch, piano, door_a],
    "bedroom 1": [queen_bed, closet, door_a, door_b, door_c],
    "bedroom 2": [double_bed, dresser, door_b],
    "kitchen": [cup_board, fridge, cooker, door_c, door_d],
    "living room":[dining_table, door_d, door_e],
    "closet": [monster],
    "piano": [key_a],
    "queen bed": [key_b],
    "double bed": [key_c],
    "dresser": [key_d],
    "cup board": [key_e],
    "outside": [door_e],
    "door a": [game_room, bedroom_1],
    "door b": [bedroom_1, bedroom_2],
    "door c": [bedroom_1, kitchen],
    "door d": [kitchen, living_room],
    "door e": [living_room, outside],
}
    #INIT_GAME_STATE = {"current_room": game_room,"keys_collected": [],"target_room": outside}
    #game_state = INIT_GAME_STATE.copy()
    #start_game()
    restart = input("New Game: Yes or No?").lower().strip()
    if restart == "no":
        break
    elif restart == "yes":
        continue
