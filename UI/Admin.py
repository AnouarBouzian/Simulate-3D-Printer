import PySimpleGUI as sg
import lib.GlobalVariables as var
import lib.Functions as f
import lib.relay as relay



def genwin():
    var.layout =[	[sg.Text("Welcome to the Admin screen", font=("helvetica",25))],
                    [sg.Button('Printer on', font=("helvetica",25))],
                    [sg.Button('Printer off', font=("helvetica",25))],
                    [sg.Button('Logout', font=("helvetica",25))],
                    [sg.Button('Shutdown', font=("helvetica",25))]]

    var.window = sg.Window('Admin', var.layout, size=(1024,600))

def events():
    if var.event == 'Printer on':
        print("relay on")
        #relay.on()
    elif var.event == 'Printer off':
        print("relay off")
        #relay.off()
    elif var.event == 'Logout':
        var.passw = ''
        var.LoggedIn = False
        var.active = 0
        var.window.close()
        f.exgenwin()
    elif var.event == 'Shutdown':
        var.terminate = True
    elif var.event in var.close:
        var.terminate = True