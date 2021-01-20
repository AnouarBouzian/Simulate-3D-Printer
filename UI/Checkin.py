import PySimpleGUI as sg
import lib.GlobalVariables as var
import lib.Functions as f
from datetime import datetime, date

def genwin():
    var.layout = [  [sg.Text("temp enter QR string")],
                    [sg.Input(size=(50,1), key='qr')],
                    [sg.Button('Checkin'),sg.Button('Home')]]

    var.window = sg.Window('Checkin', var.layout, size=(1024,600))

def genwin2():
    var.layout = [  [sg.Text('information read from the QR code')],
                    [sg.Text("begin: " + str(var.Date.time()) + ", end: " + str(f.get_end(var.Date, var.Time)))],
                    [sg.Text("Time Remaining: "),sg.Text("",size=(20,1), key="Time")],
                    [sg.ProgressBar(var.length, orientation='h', size=(70, 20), key='status')],
                    [sg.Button('Back'),sg.Button('Home')]]

    var.window = sg.Window('Checkedin', var.layout, size=(1024,600))



def genwinInDays():
    var.layout = [[sg.Text('You are a few days early')],
                  [sg.Text('Your reservation is in ' + str(var.indays) + ' days')],
                    [sg.Button('Back'),sg.Button('Home')]]
    var.window = sg.Window('to early', var.layout, size=(1024,600))

def genwinInHours():
    var.layout = [[sg.Text('You are a bit early')],
                  [sg.Text('Your reservation is ' + str(var.Date.time()))],
                    [sg.Button('Back'),sg.Button('Home')]]
    var.window = sg.Window('to early', var.layout, size=(1024,600))


def events():
    if var.event in var.close:
        var.terminate = True
    elif var.event == 'Home':
        var.active = 0
        var.window.close()
        f.exgenwin()
    elif var.event == 'Checkin':
        var.QR_String = var.values['qr']
        f.QR_Extraction(var.QR_String)
        if var.Date.date() > datetime.now().date():
            var.indays = (var.Date.date() - datetime.now().date()).days
            var.active = 4
            var.window.close()
            f.exgenwin()
        elif var.Date > datetime.now():
            var.active = 5
            var.window.close()
            f.exgenwin()
#        elif datetime.combine(var.Date.date(),f.get_end(var.Date, var.Time)) < datetime.now() < var.Date:
        else:
            var.length = f.toseconds(datetime.strptime(var.Time, "%H:%M").time())
            var.end = f.get_end(var.Date, var.Time)
            var.countdown = True
            var.active = 3
            var.window.close()
            f.exgenwin()
#        else:
#            var.active = 0
#            var.window.close()
#            f.exgenwin()


def events2():
    if var.countdown:
        if datetime.now().time() < var.end:
            var.remaining = f.totime(datetime.combine(date.today(), var.end) - datetime.now())
            var.window.FindElement("Time").update(value=str(var.remaining))
            var.window['status'].update_bar(var.length - f.toseconds(var.remaining))
    if var.event in var.close:
        var.terminate = True
    elif var.event == 'Home':
        var.active = 0
        var.window.close()
        f.exgenwin()
    elif var.event == 'Back':
        var.active = 2
        var.window.close()
        f.exgenwin()



def events3():
    if var.event in var.close:
        var.terminate = True
    elif var.event == 'Home':
        var.active = 0
        var.window.close()
        f.exgenwin()
    elif var.event == 'Back':
        var.active = 2
        var.window.close()
        f.exgenwin()


def events4():
    if var.event in var.close:
        var.terminate = True
    elif var.event == 'Home':
        var.active = 0
        var.window.close()
        f.exgenwin()
    elif var.event == 'Back':
        var.active = 2
        var.window.close()
        f.exgenwin()


genwin()

#while True:
#    var.event, var.values = var.window.read(timeout=0)
#    if var.countdown:
#        if datetime.now().time() < var.end:
#            var.remaining = f.totime(datetime.combine(date.today(), var.end) - datetime.now())
#            var.window.FindElement("Time").update(value=str(var.remaining))
#            var.window['status'].update_bar(var.length - f.toseconds(var.remaining))
#    if var.event in var.close:
#        break
#    elif var.event == 'Checkin':
#        var.QR_String = var.values['qr']
#        f.QR_Extraction(var.QR_String)
#        if var.Date.date() > datetime.now().date():
#            var.indays = (var.Date.date() - datetime.now().date()).days
#            genwinInDays()
#        elif var.Date > datetime.now():
#            genwinInHours()
#        else:
#            var.length = f.toseconds(datetime.strptime(var.Time, "%H:%M").time())
#            var.end = f.get_end(var.Date, var.Time)
#            genwin2()
#            var.countdown = True



