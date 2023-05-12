import cv2

# Abrir la cámara predeterminada
cap = cv2.VideoCapture(1)



while True:
    # Capturar frame por frameqqq
    ret, frame = cap.read()

    # Dibujar línea 1 (azul) desde (0,0) a (200,200)
    start1 = (639, 193)
    end1 = (352, 115)
    color1 = (0, 100, 255) # Azulq
    thickness1 = 2

    cv2.line(frame, start1, end1, color1, thickness1)

    # Dibujar línea 2 (verde) desde (0,240) a (320,240)
    start2 = (190, 130)
    end2 = (195, 310)
    color2 = (0, 100, 255) # Verde
    thickness2 = 2
    cv2.line(frame, start2, end2, color2, thickness2)

    # Dibujar línea 3 (roja) desde (300,0) a (300,480)
    start3 = (195, 310)
    
    end3 = (300, 480)
    color3 = (0, 100, 255) # Rojo
    thickness3 = 2
    cv2.line(frame, start3, end3, color3, thickness3)

    # Dibujar línea 4 
    start4 = (190, 130)
    end4 = (352, 115)
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
