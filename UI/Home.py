import lib.GlobalVariables as var
import PySimpleGUI as sg
import lib.Functions as f

def genwin():
    var.layout = [[sg.Button("Checkin", font=("helvetica",25))], [sg.Button("override", font=("helvetica",25))]]
    var.window = sg.Window('Home', var.layout, size=(1024, 600))

def events():
    if var.event in var.close:
        var.terminate = True
    elif var.event == "Checkin":
        var.active = 2
        var.window.close()
        f.exgenwin()
    elif var.event == "override":
        var.active = 1
        var.window.close()
        f.exgenwin()

