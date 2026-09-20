import cv2
#kamera (0 = harici kamera, 1 dahili kamera)
cap = cv2.VideoCapture(0)

widht = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#kayıt
writer = cv2.VideoWriter("video_record.mp4", cv2.VideoWriter_fourcc(*"DIVX"), 20,(widht, height))

while True:
    ret, frame = cap.read()
    cv2.imshow("video", frame)
    
    #burada kayıt işlemi yapar
    writer.write(frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"): break

cap.release(),writer.release(),cv2.destroyAllWindows()
