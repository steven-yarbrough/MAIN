import PySimpleGUI as sg

def create_blue_screen():
    sg.Window('BLUE Pill', [[sg.Text('Sky is the limit')]]).read(close=True)

def create_red_screen():
    sg.Window('RED Pill', [[sg.Text('Jesus aint down here bub')]]).read(close=True)

layout = [
    [sg.Text('RED or BLUE Pill', justification='center', font=('Helvetica', 20))],
    [sg.Button('Blue'), sg.Button('Red'), sg.Exit()]
]

window = sg.Window('Full Stack Assistance', layout)

while True:
    event, _ = window.read()
    
    if event == 'Blue':
        create_blue_screen()
    elif event == 'Red':
        create_red_screen()
    elif event == 'Exit' or event == sg.WINDOW_CLOSED:
        break

window.close()