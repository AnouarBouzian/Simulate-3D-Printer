# Script for GUI for easier use
import PySimpleGUI as qrrec
import cv2
from imgrec import qr_reader
import variable as var

# functie om verschillende windows te bedienen
cap = var.qrp
active = 0


def wndwgen():
    if active == 0:
        var.layout = [[qrrec.Text("Please Scan QR-Code for Printer use", size=(20, 1), justification='center')],
                      [qrrec.Button("Scan")], [qrrec.Button("Cancel")]]
    elif active == 1:
        var.layout = [[qrrec.Text("Please Wait...", size=(20, 1), justification='center')],
                      [qrrec.Image(filename='', key='image')], [qrrec.Button("Back")]]
    var.window = qrrec.Window("QR-Reader", var.layout, margins=(400, 300))


wndwgen()

# Verschillende events te handelen door de window

while True:
    var.event, var.values = var.window.read()

    if var.event == "Cancel" or var.event == qrrec.WIN_CLOSED:
        break

    elif var.event == "Scan":
        active = 1
        qr_reader()
        var.window.close()
        wndwgen()


    elif var.event == "Back":
        active = 0
        var.window.close()
        wndwgen()

var.window.close()
