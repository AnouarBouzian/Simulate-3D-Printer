from pyzbar.pyzbar import decode
import cv2
import numpy as np
import variable as var
import time

def qr_reader():
	var.qrp = cv2.VideoCapture(0)
	var.qrp.set(3,1024)
	var.qrp.set(4,600)
	duration = 10

	start_time = time.time()
	while(int(time.time() - start_time) < duration):

		success, var.img = var.qrp.read()
		for barcode in decode(var.img):
			print(barcode.data)
			myQrd = barcode.data.decode('utf-8')
			print(myQrd)
			pnts = np.array([barcode.polygon],np.int32)
			pnts = pnts.reshape((-1,1,2))
			cv2.polylines(var.img,[pnts],True,(0,0,0),2)
			pnts2 = barcode.rect
			cv2.putText(var.img,myQrd,(pnts2[0],pnts2[1]),cv2.FONT_HERSHEY_COMPLEX,0.9,(0,0,0),2)

		cv2.imshow('QR-Reader', var.img)
		cv2.waitKey(1)

	cv2.destroyWindow('QR-Reader')