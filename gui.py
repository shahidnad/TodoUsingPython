from modules import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")
window = sg.Window("My To-Do App", layout=[[label], [input_box,add_button]]) #creates instance of window
window.read() #uses methods of that instance
window.close()