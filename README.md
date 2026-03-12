# 📸 Real-Time Face Recognition Attendance System

A Python-based desktop application for automated attendance marking using **face recognition**, suitable for classrooms, offices, or event management systems.

The project combines **computer vision techniques with practical automation** to simplify attendance tracking using real-time webcam input.

---

# 🚀 Features

- Trains the model using images stored in a **photos folder** (separate folder per person)
- Real-time **face detection using Haar Cascades**
- **LBPH Face Recognizer** for reliable identification (confidence <120)
- Marks **attendance only once per person per session**
- Automatically logs attendance to **daily CSV files** (`YYYY-MM-DD.csv`)
- Records **Name and Time** for each recognized individual
- Displays **bounding boxes and labels** on detected faces
- Press **'q' key to exit** the application
- Handles missing images or empty datasets gracefully

---

# 📂 File Structure

| File | Description |
|-----|-------------|
| `program.py` | Main application handling training, face recognition, and attendance logging |

---

# 🛠 Tech Stack

**Computer Vision**
- OpenCV (cv2)

**Face Detection**
- Haar Cascade (`haarcascade_frontalface_default.xml`)

**Recognition Algorithm**
- LBPHFaceRecognizer

**Data Handling**
- NumPy  
- CSV  
- datetime  
- os

---

# ⚙️ Quick Setup

### 1️⃣ Install Dependencies

```bash
pip install opencv-python numpy
```

### 2️⃣ Create Photos Folder

Create a `photos` directory with subfolders for each person.

Example:

```
photos/
├── Student1/
│   ├── img1.jpg
│   └── img2.png
└── Student2/
    └── img1.jpg
```

Each person should have **10–20 clear face images**.

---

### 3️⃣ Run the Program

```bash
python program.py
```

The webcam will open and start detecting faces.  
Attendance will automatically be logged into a **CSV file for the current date**.

Press **`q`** to exit.

---

# ⚙️ How It Works

**Training**
- Loads grayscale face images from the `photos` directory
- Assigns labels based on folder names

**Detection**
- Uses webcam feed to detect faces in real time

**Recognition**
- Predicts identity using **LBPH Face Recognizer**
- Accepts recognition if confidence <120

**Logging**
- Writes attendance entries into a CSV file
- Prevents duplicate entries during a session

---

# 📄 Sample CSV Output

```
Name,Time marked
John,14:30:25
Jane,14:31:10
```

---

# 🔧 Customization

- Adjust the **confidence threshold** to improve accuracy
- Add additional **Haar cascades** for improved detection
- Extend the system with **database storage (SQLite)** or **cloud-based logging**

---

# ⚠️ Limitations & Future Improvements

Current limitations:

- Works with a **single webcam**
- Performance may vary under **poor lighting conditions**

Possible improvements:

- GUI using **Tkinter**
- Multi-camera support
- Automated attendance reports
- Integration with **Google Sheets or databases**

---

# 🤝 Contributing

Contributions are welcome.

Ideas for improvement:
- Age and gender detection
- Emotion recognition
- Attendance analytics

Fork the repository and submit a **Pull Request**.

---

# 📜 License

This project is licensed under the **MIT License**.
