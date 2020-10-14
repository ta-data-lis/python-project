import PySimpleGUI as sg

class ScreenGame:
	def __init__(self):
		#Layout
		layout = [ #define styles first in a paper
			[sg.Text("Type the player name: "),sg.Input()], #cria uma label
		#[sg.Input()] cria uma textbox
			[sg.Text("Here we are going to type the rules of the game")],
			[sg.Button("Choice1")],
			[sg.Button("Choice2")],
			[sg.Button("Choice3")]
		]
		#Window
		text_window = sg.Window("Scape Room Game").layout(layout)
		#Data extraction
		self.Button, self.values = text_window.Read()

	def Iniciar(self):
		print(self.values)

screen = ScreenGame()
screen.Iniciar()