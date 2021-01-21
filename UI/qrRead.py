from pyzbar.pyzbar import decode
import cv2
import PySimpleGUI as sg
import lib.GlobalVariables as var


def genwin():
    var.layout = [[sg.Text("Scanning QR", font=("helvetica",25))],
                  [sg.Image(filename='', key='image')],
                  [sg.Button('Home', font=("helvetica",25))]]
    var.window = sg.Window("QR-Reader", var.layout, size=(1024, 600))


def initCapture():
    var.scan = cv2.VideoCapture(0)


def recording():
    var.ret, var.frame = var.scan.read()
    var.imgbytes = cv2.imencode('.png', var.frame)[1].tobytes()
    var.window['image'].update(data=var.imgbytes)
    try:
        var.QR_Read = decode(var.frame)[0].data.decode('utf-8')
        #print(var.QR_Read)
    except:
        pass
        #print("error")


#genwin()
#initCapture()
#while True:
#    var.window.read(timeout=0)
#    recording()