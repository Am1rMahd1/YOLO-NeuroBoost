from ultralytics import YOLO

model = YOLO('ultralytics/cfg/models/v8/yolov8.yaml')  # Replace with the path to your YAML file
print(model.model)  # Print the model structure to verify layers