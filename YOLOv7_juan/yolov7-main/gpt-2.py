import cv2
import numpy as np
from pathlib import Path

import cv2
import torch
import torch.backends.cudnn as cudnn
from models.experimental import attempt_load
from utils.datasets import LoadStreams, LoadImages
from utils.general import non_max_suppression, scale_coords
from utils.plots import plot_one_box

# Definir los puntos de inicio y fin de la línea
p1 = (0, 300)
p2 = (800, 300)

# Set device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Set config file and weight file paths
config_path = "cfg\training\yolov7-hatsu-2.yaml"
weight_path = 'yolo-hatsu-2.pt'


model = attempt_load(weight_path, map_location=device)
model.eval()

# Configurar el modelo
model.conf = 0.5  # Umbral de confianza para la detección
model.iou = 0.5  # Umbral de IoU para la supresión no máxima

# Obtener las etiquetas de las clases
names=['hatsu azul', 'rosa', 'verde']


# Configurar la cámara web
cap = cv2.VideoCapture(0)

# Inicializar el contador de objetos
counter = {name: 0 for name in names}

while True:
    # Leer un frame de la cámara
    ret, img = cap.read()

    # Pasar el frame a través del modelo
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (640, 640))
    img = torch.from_numpy(img).permute(2, 0, 1).float().div(255.0).unsqueeze(0)
    detections = model(img)[0]
    detections = non_max_suppression(detections, model.conf, model.iou)

    # Dibujar la línea en el frame
    img_line = img.copy().squeeze().transpose(1, 2, 0)
    cv2.line(img_line, p1, p2, (255, 0, 0), 2)

    # Contar los objetos detectados que cruzan la línea
    for detection in detections:
        if detection is not None:
            detection = scale_coords(img.shape[2:], detection[:, :4], img_line.shape).round()
            for x1, y1, x2, y2, conf, cls_conf, cls in detection:
                label = names[int(cls)]
                if label in counter:
                    box = [x1, y1, x2, y2]
                    if intersects(box, p1, p2):
                        counter[label] += 1
                        plot_one_box(box, img_line, label=label + ' ' + str(counter[label]), color=(0, 255, 0), line_thickness=2)

    # Mostrar el frame con la línea y el contador
    cv2.imshow('Line Counter', img_line)
    if cv2.waitKey(1) == ord('q'):
        break

# Liberar la cámara y cerrar la ventana
cap.release()
cv2.destroyAllWindows()
