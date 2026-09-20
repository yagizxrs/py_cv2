import face_recognition
import face_recognition
import cv2 
import os
import numpy as np

#kamerayi baslat
camera = cv2.VideoCapture(0)

face_cards = []
face_name = []
face_check = []

face_yol = "kisiler"
for i in os.listdir(face_yol):
    all_face = os.path.join(face_yol, i)
    if os.path.isdir(all_face):
        name_status_pack = i.split("_")
        if len(name_status_pack) == 2:
            name = name_status_pack[0].capitalize() #ilk harf büyült
            status = name_status_pack[1].lower() #küçük harfe çevir
            for foto_name in os.listdir(all_face):
                foto_all_yol = os.path.join(all_face, foto_name)
                try:
                    ref_foto = face_recognition.load_image_file(foto_all_yol)
                    face_code = face_recognition.face_encodings(ref_foto)

                    if len(face_code) > 0:
                        face_cards.append(face_code[0])
                        face_name.append(name)
                        face_check.append(status)
                
                except:
                    pass

# Döngüden önce bu hafıza değişkenlerini ve yeni sayacımızı ekliyoruz
frame_counter = 0
last_face_location = []
last_face_name = []
last_face_check = []
while True:
    bas, fl = camera.read()
    if bas:
        low_fl = cv2.resize(fl, (0,0), fx=0.25, fy=0.25)
        low_color_fl = cv2.cvtColor(low_fl, cv2.COLOR_BGR2RGB)
        
        frame_counter += 1
        # 5 karede 1 yüz tanıma
        if frame_counter % 5 == 0:
            face_location = face_recognition.face_locations(low_color_fl)
            face_code = face_recognition.face_encodings(low_color_fl, face_location)
            last_face_location = []
            last_face_name = []
            last_face_check = []
            for (up, right, down, left), f_code in zip(face_location, face_code):
                name = "not found"
                status = "not found"
                if len(face_cards) > 0:
                    distance = face_recognition.face_distance(face_cards, f_code)
                    match = face_recognition.compare_faces(face_cards, f_code)
                    top_match = np.argmin(distance)
                    if match[top_match]:
                        name = face_name[top_match]
                        status = face_check[top_match]
                
                last_face_location.append((up, right, down, left))
                last_face_name.append(name)
                last_face_check.append(status)
      
        for (up, right, down, left), name, status in zip(last_face_location, last_face_name, last_face_check):
            up, right, down, left = up*4, right*4, down*4, left*4
            if status == "suclu":
                color = (0, 0, 255) # Kırmızı
                text = f"{name} SUCLU"
            elif status == "normal":
                color = (0, 255, 0) # Yeşil
                text = f"{name}"
            else:
                color = (255, 0, 0) # Mavi
                text = "Bilinmiyor"
            #  (4 birim) kutu çiziyoruz
            cv2.rectangle(fl, (left, up), (right, down), color, 4)
            
            # Metni kutunun "içine" (sol alta) yerleştiriyoruz. Yazı rengi kutuyla aynı.
            cv2.putText(fl, text, (left + 10, down - 10), cv2.FONT_HERSHEY_DUPLEX, 0.8, color, 2)
        cv2.imshow("Yuz tanima", fl)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
camera.release()
cv2.destroyAllWindows()