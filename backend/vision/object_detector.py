from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def detect_objects(image_path):
    results = model(image_path)

    objects = []

    for result in results:
        for box in result.boxes:
            class_id = int(box.cls[0])
            objects.append(
                model.names[class_id]
            )

    return list(set(objects))