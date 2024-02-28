from ultralytics import YOLO
import cv2

model = YOLO('../yolo_weights/yolov8l.pt')
results = model("images/2.png", show=True)
cv2.waitKey(0)