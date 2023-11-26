import cv2
import pytesseract
from gtts import gTTS
import os
import time

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray, lang='eng', config='--oem 3 --psm 6')

    # Eğer belirli metin algılanırsa "ENERJI" yazdır
    if "ENERJI" in text:
        print("enerji sözcüğü algılandı")
        tts = gTTS('enerji', lang='tr')  # Türkçe seslendirme için dil parametresi ekledik
        tts.save('enerji.mp3')
        os.system("enerji.mp3")

    elif "IKTIDAR" in text:
        print("iktidar sözcüğü algılandı")
        tts = gTTS('iktidar', lang='tr')  # Türkçe seslendirme için dil parametresi ekledik
        tts.save('iktidar.mp3')
        os.system("iktidar.mp3")

    elif "Piranha" in text:
        print("piranha sözcüğü algılandı")
        tts = gTTS('piranha', lang='tr')  # Türkçe seslendirme için dil parametresi ekledik
        tts.save('piranha.mp3')
        os.system("piranha.mp3")
        
        
    cv2.putText(frame, text, (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    cv2.imshow('Webcam Text Recognition', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
