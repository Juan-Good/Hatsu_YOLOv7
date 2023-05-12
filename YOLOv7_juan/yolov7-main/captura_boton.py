import cv2
import os
import time
import uuid

# Ruta donde se guardarán las fotos
images_path = os.path.join('data','captured_images')



# Función para capturar varias fotos y guardarlas en el directorio especificado
def capture_images():
    # Creamos la ventana donde se mostrará la imagen
    cv2.namedWindow("Captura de imagen", cv2.WINDOW_NORMAL)
    
    # Inicializamos la cámara
    cap = cv2.VideoCapture(1)
    
    # Contador para nombrar las imágenes capturadas
    count = 0
    number_images = 30 #Declaramos la cantidad de iamgenes a capturar
    
    while True:
        # Capturamos una imagen de la cámara
        ret, frame = cap.read()

        new_size = (640, 480)
        frame = cv2.resize(frame, new_size)
        
        # Mostramos la imagen capturada en la ventana
        cv2.imshow("Captura de imagen", frame)
        
        # Esperamos a que se presione una tecla
        key = cv2.waitKey(1)
        
        # Si se presiona la tecla "s", guardamos la imagen actual en el directorio especificado
        if key == ord("s"):
            count += 1
            filename = os.path.join(images_path,f'{str(uuid.uuid1())}.jpg')
            cv2.imwrite(filename, frame)
            print("Imagen guardada como", filename)
        
        # Si se presiona la tecla "q", salimos del bucle
        elif key == ord("q") or count>=number_images:
            break
    
    # Liberamos los recursos de la cámara y cerramos la ventana
    cap.release()
    cv2.destroyAllWindows()

# Llamamos a la función para capturar las fotos
capture_images()
