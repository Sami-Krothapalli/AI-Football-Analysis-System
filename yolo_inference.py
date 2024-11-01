#Motes: 7:25

from ultralytics import YOLO

# Load YOLOv5s model 

model = YOLO('yolovv8x')

model.predict('input_videos/08fd33_4.mp4') # Inference on video