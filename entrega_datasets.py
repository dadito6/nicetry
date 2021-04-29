import PySimpleGUI as sg
from archivo1 import agencia
from archivo2 import camas


def menu():
    """
    Construye la ventana del menú del juego
    """
    layout = [
        [sg.Button('Datos de Agencia de Viajes', size=(50, 2), key="-agencia-")],
        [sg.Button('Camas Criticas (covid-19)', size=(50, 2), key="-camas-")],
        [sg.Button('Salir', size=(50, 2), key="-exit-")]
    ]

    board = sg.Window('Recoleccion de datos').Layout(layout)

    return board

def start():
    window = loop()
    window.close()


def loop():
    """
    Loop de la ventana de menú que capta los eventos al apretar las opciones
    """
    window = menu()
    while True:
        event, _values = window.read()
        if event in (sg.WINDOW_CLOSED, "Exit", "-exit-"):
            break
        if event == "-agencia-":
            window.hide()
            agencia()
            window.un_hide()
        if event == "-camas-":
            window.hide()
            camas()
            window.un_hide()    

    return window
    
start()