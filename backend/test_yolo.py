from vision.object_detector import detect_objects

objects = detect_objects(
    "uploads/resume reference.jpg"
)

print(objects)