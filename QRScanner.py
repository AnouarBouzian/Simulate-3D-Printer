import cv2

# camera instellen
cap = cv2.VideoCapture(0)

# QR-code detectie
detector = cv2.QRCodeDetector()

while True:
    # Camera begint met de lezen
    _, img = cap.read()
    # ontvang bounding box coordinaten en data
    data, bbox, _ = detector.detectAndDecode(img)

    # als er een selectiekader is, teken er dan een vierkant rond, en haal er data uit
    if (bbox is not None):
        for i in range(len(bbox)):
            cv2.line(img, tuple(bbox[i][0]), tuple(bbox[(i + 1) % len(bbox)][0]), color=(255,
                                                                                         0, 255), thickness=2)
        cv2.putText(img, data, (int(bbox[0][0][0]), int(bbox[0][0][1]) - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 255, 0), 2)
        if data:
            print("data found: ", data)
    # Geef op het beeld een afbeeldingsvoorbeeld
    cv2.imshow("code detector", img)
    if (cv2.waitKey(1) == ord("q")):
        break
# Camera en tabs sluiten zich af
cap.release()
cv2.destroyAllWindows()