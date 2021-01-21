import PySimpleGUI as sg
close = ["Exit", sg.WINDOW_CLOSED]
numbers = ['0','1','2','3','4','5','6','7','8','9']
correctPass = '1234'
passw = ''
active = 0
QR_String = None
LoggedIn = False
terminate = False
admin = False

#PySimpleGUI variables
layout = None
window = None
event = None
values = None

#QR Variables
ID = None
Device = None
Reservation = None
Date = None
Time = None
indays = None

#login Time
length = 0
end = None
remaining = None
countdown = False

#QR Scanner
scan = None
ret = None
frame = None
imgbytes = None
QR_Read = None

