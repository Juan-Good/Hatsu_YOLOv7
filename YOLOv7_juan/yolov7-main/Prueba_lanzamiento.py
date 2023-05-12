import subprocess

#Codigo para correr el script de tección desde otro script


# python detect_roboflow_set.py --weights yolo-hatsu7.pt --conf 0.7 --img-size 640 --source 0 --view-img --no-trace --nosave

subprocess.run(['python', 'detect_roboflow_set.py', '--weights', 'yolo-hatsu7.pt', '--conf', '0.7', '--img-size', '640', '--source', '0', '--view-img', '--no-trace', '--nosave'])
