
import cv2
import os
import time
import uuid

IMAGES_PATH = os.path.join('data','captured_images') #Declaramos la ruta donde guardaremos las imagenes capturadas
number_images = 10 #Declaramos la cantidad de iamgenes a capturar

cap = cv2.VideoCapture(1) # El numero indica la camara a usar, 1 suele ser una web cam externa mientra 0 es la incorporada

time.sleep(3.5)

for imgnum in range(number_images):
    print('Collecting image {}'.format(imgnum))
    ret, frame = cap.read()
    imgname = os.path.join(IMAGES_PATH,f'{str(uuid.uuid1())}.jpg')
    cv2.imwrite(imgname, frame)
    cv2.imshow('frame', frame)
    #time.sleep(0.3)

    if cv2.waitKey(1) & 0xFF == ord('q'): #Se indica que con q se cierra la ventana
        break
cap.release()
cv2.destroyAllWindows()