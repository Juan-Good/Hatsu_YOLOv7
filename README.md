
# Detector de objetos personalizado para retail con YOLOV7 y Bytrackt

**Universidad Nacional de Colombia**

**Realizado por:** Juan Andres Bueno

**Dirigido por:** Jorge Sofrony


Se entrena un modelo personalizado para la detección de un set de productos seleccionados, se usa YOLOV7, posteriormente se adapta un codigo para el uso de Supervision (Paquete de roboflow para el conteo de productos)

![Resultados de detector](https://github.com/Juan-Good/Hatsu_YOLOv7/blob/main/images/hatsu7.gif)

## Descripción

Se busca realizar un modelo de detección personalizada para entornos retail, para ello se capturan y generan distintos datasets para el entrenamiento de un modelo de detección de objetos. Se desea que el sistema sea capaz de identificar los objetos en un espacio definido y llevar el registro de los objetos entrando y saliendo de este espacio para asi automatizar el proceso de compra y mejorar la experiencia global del usuario, para tal fin se emplea Supervisión para el conteo de entradas y salidas definiendo una linea en la imagen  como frontera, asi mismo se usa ByteTrackt como rastreador.

## Características

- Detector de objetos personalizado utilizando YOLOV7.
- Uso de Bytetrack para el rastreo de productos.
- Uso de LineCounter con modificaciones propias para el conteo de productos.
- Codigos para la construcción de datasets propios.

## Requisitos del Sistema

En esta sección, puedes listar los requisitos necesarios para ejecutar el proyecto. Esto puede incluir software, bibliotecas o hardware específicos. Por ejemplo:

- Python 3.9
- Anaconda Navigator
- YOLOV7
- Bytetrack
- Supervision
- Visual StudioCode

Sobre Software recomendado
- Procesador: 12th Gen Intel(R) Core(TM) i7-12700H   2.70 GHz.
- Ram: 16.0 GB.
- Tarjeta Gráfica NVIDIA GeForce RTX 3070 Ti GPU
- Memoria disponible 100 GB
- Webcam: 1920 x 1080 Pixeles FULL HD

## Instalación

Proporciona instrucciones claras sobre cómo instalar y configurar el proyecto en un entorno local. Incluye todos los pasos necesarios, como la instalación de dependencias y la configuración de variables de entorno. Por ejemplo:

1. Creación de un entorno virtual `conda create -n nombre_del_entorno python=3.9`  
2. Clona el repositorio: `git clone https://github.com/tu_usuario/tu_repositorio.git`
3. Instala las dependencias: `pip install -r requirements.txt`
4. Instala las dependencias para gpu: `pip install -r requirements_gpu.txt`

Para mayor detalle recomendamos visitar: https://drive.google.com/file/d/1CjT5fJelgwLNDtzH-cRaJhxHQvrFYyUY/view?usp=sharing

## Uso

En el archivo comandos.txt encontrara los diferentes comandos para entrenamiento y uso, tienen el siguiente estilo

```
#Entrenamiento
python train.py --workers 1 --device 0 --batch-size 8 --epochs 100 --img 640 640 --data data/hatsu_test3.yaml --hyp data/hyp.scratch.custom.yaml --cfg cfg/training/yolov7-hatsu3.yaml --name yolov7-hatsu3 --weights yolov7.pt
#Uso
python <archivo a correr> --weights <archivo de pesos> --conf <confianza del modelo> --img-size 640 --source 0 --view-img --no-trace
```



## Contacto

jbuenoh@unal.edu.co

## Créditos
Para mayor información se invita a revisar:

- Guia de entrenamiento de un detector personalizado: https://www.youtube.com/watch?v=-QWxJ0j9EY8
- Repositorio de yolo v7: https://github.com/WongKinYiu/yolov7
- Implementación de linecounter https://www.youtube.com/watch?v=OS5qI9YBkfk


