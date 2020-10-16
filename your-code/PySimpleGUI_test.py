import PySimpleGUI as sg

text = "You wake up on a couch and find yourself in a strange house with no windows which you have never been to before. \n\n You don't remember why you are here and what had happened before. \n\n You feel some unknown danger is approaching and you must get out of the house, NOW!"

initial_layout = [[sg.Text(text)], [sg.Button("Let's scape!")]]
gameroom_layout = [[sg.Text("You are now in game room. \n\n What would you like to do?", key="gameroom")], [sg.Button("Couch")], [sg.Button("Piano")], [sg.Button("Door")]]

nothing_layout = [[sg.Text("There isn't anything interesting about it.")], [sg.Button("Ok")]]
key_layout = [[sg.Text("You find key for Door.")], [sg.Button("Ok")]]

# Create the window
start_window = sg.Window("Start",initial_layout,margins=(300,150))
gameroom_window = sg.Window("Game Room", gameroom_layout,margins=(500,300))

nothing_window = sg.Window("test", nothing_layout, margins=(300,150))
key_window = sg.Window("You have a key now!", key_layout, margins=(300,150))

key = 0

# Create an event loop
while True:
    event,values = start_window.read()
    if event == "Let's scape!":
        start_window.close()
    event, values = gameroom_window.read()
    if event == "Couch":
        event, values = nothing_window.read()
        if event == "Ok":
            nothing_window.close()
    elif event == "Piano":
        event, values = key_window.read()
        key = 1
        if event == "Ok":
            key_window.close()
    elif event == "Door":
        if key == 1: #door open
            event, values = nothing_window.read()
            if event == "Ok":
                nothing_window.close()
    event, values = gameroom_window.read()
        
    # End program if user closes window or
    # presses the OK button
    if event == sg.WIN_CLOSED:
        break

#start_window.close()