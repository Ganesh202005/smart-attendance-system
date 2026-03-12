import cv2
import numpy as np
import os
import csv
from datetime import datetime

# -----------------------------
# CONFIGURATION
# -----------------------------
dataset_path = "photos"

# -----------------------------
# FACE DETECTOR
# -----------------------------
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# -----------------------------
# FACE RECOGNIZER
# -----------------------------
recognizer = cv2.face.LBPHFaceRecognizer_create()

faces = []
labels = []
label_names = {}
current_label = 0

# -----------------------------
# LOAD TRAINING DATA
# -----------------------------
for person_name in os.listdir(dataset_path):
    person_path = os.path.join(dataset_path, person_name)

    if not os.path.isdir(person_path):
        continue

    label_names[current_label] = person_name

    for image_name in os.listdir(person_path):
        img_path = os.path.join(person_path, image_name)

        # Skip non-image files
        if not image_name.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
            continue

        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

        if img is None:
            continue

        faces.append(img)
        labels.append(current_label)

    current_label += 1
# -----------------------------
# CHECK IF TRAINING DATA EXISTS
# -----------------------------
if len(faces) == 0:
    print("No training images found. Check your photos folder structure.")
    exit()

recognizer.train(faces, np.array(labels))

print("Training completed successfully.")

# -----------------------------
# ATTENDANCE FILE SETUP
# -----------------------------
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

file = open(current_date + ".csv", "w", newline="")
writer = csv.writer(file)
writer.writerow(["Name", "Time"])

marked_students = set()

# -----------------------------
# START CAMERA
# -----------------------------
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detected_faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in detected_faces:
        face_roi = gray[y:y+h, x:x+w]

        label, confidence = recognizer.predict(face_roi)
        name = label_names[label]

        if confidence < 120:
            if name not in marked_students:
                time_now = datetime.now().strftime("%H:%M:%S")
                writer.writerow([name, time_now])
                file.flush()
                marked_students.add(name)
        else:
            name = "Unknown"

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, name, (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9,
                    (0, 255, 0), 2)

    # These must be inside while loop but outside for loop
    cv2.imshow("Attendance System", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
file.close()