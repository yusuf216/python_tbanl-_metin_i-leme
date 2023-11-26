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
    if "kelime1" in text:
        print("kelime1 sözcüğü algılandı")
        tts = gTTS('kelime1', lang='tr')  # Türkçe seslendirme için dil parametresi ekledik
        tts.save('kelime1.mp3')
        os.system("kelime1.mp3")

    elif "kelime2" in text:
        print("kelime2 sözcüğü algılandı")
        tts = gTTS('kelime2', lang='tr')  # Türkçe seslendirme için dil parametresi ekledik
        tts.save('kelime2.mp3')
        os.system("kelime2.mp3")

    elif "kelime3" in text:
        print("kelime3 sözcüğü algılandı")
        tts = gTTS('kelime3', lang='tr')  # Türkçe seslendirme için dil parametresi ekledik
        tts.save('kelime3.mp3')
        os.system("kelime3.mp3")
        
        
    cv2.putText(frame, text, (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    cv2.imshow('Webcam Text Recognition', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
