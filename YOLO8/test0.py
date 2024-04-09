from ultralytics import YOLO
from PIL import Image
import cv2

model = YOLO("yolov8n.pt")

# from PIL
im1 = Image.open("people.jpg")
results = model.predict(source=im1, save=True)  # save plotted images
