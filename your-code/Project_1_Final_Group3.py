#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PIL import Image, ImageTk
import tkinter as tk
from time import sleep
import pygame as py

#call sounds
def tocar_mp3(caminho):
    
    py.init()
    py.mixer.init()
    py.mixer.music.load(caminho)
    py.mixer.music.play()
    #sleep(10)
    #py.mixer.music.stop()
    
# tocar_mp3("music.mp3")

#call images
bk = {"grand hall":"image1.png",
      "trophy room":"image2.png", 
      "attic":"image3.png", 
      "dungeon":"image4.png",
      "outside":"image5.png"}

def house (background):
    def fechar_janela():
        janela.after(3000, janela.destroy)

    imagem = Image.open(background)

    largura_desejada = 1200
    altura_desejada = 800
    imagem_redimensionada = imagem.resize((largura_desejada, altura_desejada))

    janela = tk.Tk()

    imagem_tk = ImageTk.PhotoImage(imagem_redimensionada)
    imagem_label = tk.Label(janela, image=imagem_tk)
    imagem_label.pack()

    fechar_janela()
    janela.mainloop()
    
    


# In[2]:


# define rooms and items
door_a = {"name": "door a", "type": "door"}
door_b = {"name": "door b", "type": "door"}
door_c = {"name": "door c", "type": "door"}
door_d = {"name": "door d", "type": "door"}

pile_of_bones = {"name": "pile of bones", "type": "furniture"}
key_a = {"name": "key for door a", "type": "key", "target": door_a}
piano = {"name": "piano", "type": "furniture"}
grand_hall = {"name": "grand hall", "type": "room"}

deer_head = {"name":"deer head", "type":"furniture"}
key_b = {"name": "key for door b", "type": "key", "target": door_b}
trophy_room = {"name": "trophy room", "type": "room"}

chainsaw = {"name": "chainsaw", "type": "furniture"}
dungeon = {"name": "dungeon", "type": "room"}

dead_body = {"name":"dead body", "type":"furniture"}
coffin = {"name":"coffin", "type":"furniture"}
key_c = {"name": "key for door c", "type": "key", "target": door_c}
key_d = {"name": "key for door d", "type": "key", "target": door_d}
attic = {"name": "attic", "type": "room"}

outside = {"name": "outside"}
all_rooms = [grand_hall, trophy_room, attic, dungeon, outside]
all_doors = [door_a, door_b, door_c, door_d]

# define which items/rooms are related

object_relations = {
    "grand hall": [pile_of_bones, piano, door_a],
    "piano": [key_a],
    "outside": [door_d],
    "door a": [grand_hall, trophy_room],
    "door b": [trophy_room, attic],
    "door c": [trophy_room, dungeon],
    "door d": [dungeon, outside],
    "trophy room":[deer_head, door_a, door_b, door_c],
    "deer head":[key_b],
    "attic":[dead_body, coffin, door_b],
    "dead body":[key_c],
    "coffin":[key_d],
    "dungeon":[chainsaw, door_c, door_d]
}

# define game state. Do not directly change this dict.
# Instead, when a new game starts, make a copy of this
# dict and use the copy to store gameplay state. This
# way you can replay the game multiple times.

INIT_GAME_STATE = {
    "current_room": grand_hall,
    "keys_collected": [],
    "target_room": outside
}


# In[3]:


def linebreak():
    """
    Print a line break
    """
    print("\n\n")

def start_game():
    
    """
    Start the game
    """
    print("Prepare to enter a realm of darkness, where every step could be your last. As you find yourself surrounded by a haunting pile of bones, the eerie atmosphere engulfs you, sending shivers down your spine. Your mission? Escape this malevolent house of horrors before it consumes your very soul. You must get out IMMEDIATELY!")
    play_room(game_state["current_room"])
    
def play_room(room):
    """
    Play a room. First check if the room being played is the target room.
    If it is, the game will end with success. Otherwise, let player either
    explore (list all items in this room) or examine an item found here.
    """
    game_state["current_room"] = room
    if(game_state["current_room"] == game_state["target_room"]):
        print("Congratulations! After a heart-pounding pursuit, you have successfully escaped the haunted house, leaving behind the bone-chilling terrors to be nothing more than a lingering memory. Well done!")
        house(bk["outside"]) #image end game
        tocar_mp3("end.mp3")#musica vitoria
        sleep(5)        
        py.mixer.music.stop() #stop music
    else:
        print("You are now in " + room["name"])
        house(bk[room["name"]]) #images change room
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
                    tocar_mp3("examine.mp3") #musica examinar
                    house("chave.png") #imagem chave
                    sleep(5) #tempo
                    tocar_mp3("music.mp3") #tocar musica
                else:
                    output += "There isn't anything interesting about it."                    
                    tocar_mp3("examine.mp3") #musica examinar
                    house("fantasma.jpg")
                    sleep(5)
                    tocar_mp3("music.mp3")                    
            print(output)
            break

    if(output is None):
        print("The item you requested is not found in the current room.")

    if(next_room and input("Do you want to go to the next room? Enter 'yes' or 'no'").strip() == 'yes'):
        tocar_mp3("door.mp3") #musica abrir porta
        house("porta.jpg")
        sleep(5)
        tocar_mp3("music.mp3")
        play_room(next_room)        
    else:
        play_room(current_room)


# In[4]:


game_state = INIT_GAME_STATE.copy()
tocar_mp3("music.mp3")
start_game()


# In[ ]:





# In[ ]:




