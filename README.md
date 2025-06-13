# 📦 Warehouse Box Counter - YOLOv11 Based CV App

A real-time application that **automatically detects and counts boxes** in warehouse images or videos using YOLOv11 and a clean Python GUI.

✅ Supports:  
- 📸 Webcam live feed  
- 🖼️ Image upload  
- 🎞️ Video file detection  

➡️ All from a **single, user-friendly interface**.

---

## 🖥️ Demo Flow

🎛️ Choose input: Image / Video / Webcam  
🧠 YOLOv11 runs detection  
📦 Boxes are marked with bounding boxes  
🔢 Total count is displayed on screen

---

## 🚀 Getting Started

Follow these steps to get the app up and running on your machine.

### 1. Clone the Repository

```bash
git clone https://github.com/MANASA-NUKALA/warehouse-box-counter-cv.git
cd warehouse-box-counter-cv
```

### 2. Create & Activate a Virtual Environment

#### On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

#### On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
cd gui
python app_gui.py
```

✅ You’ll see a simple interface where you can choose image, video, or webcam for detection.

---

## 📁 Project Structure

```
warehouse-box-counter-cv/
├── box/                    # Placeholder or legacy (if any)
├── box_counter/            # Core logic for counting boxes
├── detect_contours.py      # Optional method using contours for box detection
├── gui/                    # GUI interface (Main entry: app_gui.py)
│   └── app_gui.py
├── main.py                 # Initial script used for testing
├── preprocessing/          # Optional image preprocessing steps
├── requirements.txt        # Python dependencies
├── webcam_capture/         # Webcam image capture logic
├── yolo_module/            # YOLOv11 model inference logic
├── yolov8/                 
├── yolov_11/               # Legacy or test data/models for YOLOv11
├── .gitignore              # Ignored files for Git
└── README.md               # Project info
```

---

## ⚙️ Tech Stack Used

- Python 3.8+
- YOLOv11 via Ultralytics
- OpenCV
- Tkinter
- NumPy

---

## 👥 Team Contributors

- [@MANASA-NUKALA](https://github.com/MANASA-NUKALA)
- [@vidyaganjasri](https://github.com/vidyaganjasri)
- [@MissHaRin19](https://github.com/MissHaRin19)
- [@AdulaAnusha22](https://github.com/AdulaAnusha22)
- [@KPRANEETHA-1](https://github.com/KPRANEETHA-1)
- [@Sudheshna193](https://github.com/Sudheshna193)

---


