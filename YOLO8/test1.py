from ultralytics import YOLO
from PIL import Image
import cv2

model_1 = YOLO("yolov8n.pt")
model_2 = YOLO("yolov8s.pt")
model_3 = YOLO("yolov8m.pt")

# from PIL
im1 = Image.open("people.jpg")
result_1 = model_1.predict(source=im1, save=True)  # save plotted images
result_2 = model_2.predict(source=im1, save=True)
result_3 = model_3.predict(source=im1, save=True)
