import cv2
from pyzbar import pyzbar

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Decode QR codes
    decoded = pyzbar.decode(frame)
    for qr in decoded:
        data = qr.data.decode("utf-8")
        print("QR Code:", data)
        
        # Draw bounding box
        (x, y, w, h) = qr.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, data, (x, y - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("QR Scanner", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()