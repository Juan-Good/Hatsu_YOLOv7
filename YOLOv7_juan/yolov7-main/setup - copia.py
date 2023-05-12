import cv2

# Abrir la cámara predeterminada
cap = cv2.VideoCapture(1)


punto1 = (639, 180)
punto2 = (480, 100)
punto3 = (320, 105)
punto4 = (320, 253)
punto5 = (390, 639)
while True:
    # Capturar frame por frameqqq
    ret, frame = cap.read()

    # Dibujar línea 1 (azul) desde (0,0) a (200,200)
    start1 = punto1
    end1 = punto2
    color1 = (0, 100, 255) # Azulq
    thickness1 = 2

    cv2.line(frame, start1, end1, color1, thickness1)

    # Dibujar línea 2 (verde) desde (0,240) a (320,240)
    start2 = punto2
    end2 = punto3
    color2 = (0, 100, 255) # Verde
    thickness2 = 2
    cv2.line(frame, start2, end2, color2, thickness2)

    # Dibujar línea 3 (roja) desde (300,0) a (300,480)
    start3 = punto3
    end3 = punto4
    color3 = (0, 100, 255) # Rojo
    thickness3 = 2
    cv2.line(frame, start3, end3, color3, thickness3)

    # Dibujar línea 4 
    start4 = punto4
    end4 = punto5
    color4 = (0, 100, 255) # Naranja
    thickness4 = 2
    cv2.line(frame, start4, end4, color4, thickness4)

    # Mostrar el frame resultante
    cv2.imshow('Setup', frame)

    # Esperar por una tecla para salir
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar la ventana
cap.release()
cv2.destroyAllWindows()
