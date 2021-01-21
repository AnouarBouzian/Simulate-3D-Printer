import lib.GlobalVariables as var
import UI.Home as home
import UI.login as login
import UI.Checkin as Checkin
from datetime import datetime, timedelta, date
import UI.Admin as Admin

def resetScan():
    var.scan = None
    var.ret = None
    var.frame = None
    var.imgbytes = None
    var.QR_Read = None

def toseconds(time):
    seconds = time.second + time.minute * 60 + time.hour * 3600
    return seconds


def get_end(start, slot):
    TReturn = start + timedelta(hours=int(slot.split(":")[0]), minutes=int(slot.split(":")[1]))
    return TReturn.time()


def totime(delta):
    Etime = datetime.strptime((str(delta).split(".")[0]), "%H:%M:%S").time()
    return Etime


def PassToSecret(n):
    Secret = ''
    for i in n:
        Secret += '*'
    return Secret


def exgenwin():
    if var.LoggedIn:
        Admin.genwin()
    elif var.active == 0:
        home.genwin()
    elif var.active == 1:
        login.genwin()
    elif var.active == 2:
        Checkin.genwin()
    elif var.active == 3:
        Checkin.genwin2()
    elif var.active == 4:
        Checkin.genwinInDays()
    elif var.active == 5:
        Checkin.genwinInHours()

def eventcheck():
    if var.LoggedIn:
        Admin.events()
    elif var.active == 0:
        home.events()
    elif var.active == 1:
        login.events()
    elif var.active == 2:
        Checkin.events()
    elif var.active == 3:
        #var.length = toseconds(datetime.strptime(var.Time, "%H:%M").time())
        #var.end = get_end(var.Date, var.Time)
        Checkin.events2()
    elif var.active == 4:
        Checkin.events3()
    elif var.active == 5:
        Checkin.events4()


def QR_Extraction(QR):
    QR_Split = QR.split(";")
    for x in QR_Split:
        if x.split(",")[0] == "ID":
            var.ID = x.split(",")[1]
        elif x.split(",")[0] == "Device":
            var.Device = x.split(",")[1]
        elif x.split(",")[0] == "Reservation":
            var.Reservation = x.split(",")[1]
        elif x.split(",")[0] == "Date":
            var.Date = datetime.strptime(x.split(",")[1], "%d-%m-%Y %H:%M")
        elif x.split(",")[0] == "Time":
            var.Time = x.split(",")[1]
