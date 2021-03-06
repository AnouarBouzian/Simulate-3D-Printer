import PySimpleGUI as sg
import lib.GlobalVariables as var
import lib.Functions as f



def genwin():
    var.layout =[	[sg.Text('', key='passShow', size=(7,1))],
                    [sg.Button('1'),sg.Button('2'),sg.Button('3')],
                    [sg.Button('4'),sg.Button('5'),sg.Button('6')],
                    [sg.Button('7'),sg.Button('8'),sg.Button('9')],
                    [sg.Button('Correct'),sg.Button('0'),sg.Button('Home')]]

    var.window = sg.Window('Admin Login', var.layout, size=(1024,600))

def events():
    if var.event in var.close:
        var.terminate = True
    elif var.event == 'Home':
        var.active == 0
    elif len(var.passw) == 4:
        if var.passw == var.correctPass:
            var.LoggedIn = True
            var.window.close()
        else:
            var.passw = ''
    elif var.event in var.numbers:
        var.passw += var.event
        var.window.FindElement('passShow').update(value=f.PassToSecret(var.passw))
    elif var.event == 'Correct':
        var.passw = ''
        var.window.FindElement('passShow').update(value=f.PassToSecret(var.passw))
