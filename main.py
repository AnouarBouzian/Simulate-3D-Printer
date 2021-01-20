import lib.GlobalVariables as var
import lib.Functions as f
from datetime import datetime, date
f.exgenwin()
while True:
    if var.terminate:
        break
    else:
        var.event, var.values = var.window.read(timeout=0)
        f.eventcheck()