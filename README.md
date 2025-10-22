
# Warehouse Box Counter

The **Warehouse Box Counter** is a computer vision project built with Python that automates the process of detecting and counting boxes in warehouse environments. Using the powerful YOLOv11 object detection algorithm, this tool can process static images, webcam feeds, or video streams to identify boxes, draw bounding boxes around them, and display the total count in real-time. 

The application is designed to be efficient, easy to use, and helpful in industrial settings where manual inventory tracking is time-consuming and error-prone. A simple GUI built with Tkinter makes the tool accessible even to non-technical users.

---

## Features

- Accurate object detection using YOLOv11
- Real-time webcam or image input support
- Bounding box visualization for detected objects
- Real-time count display of detected boxes
- User-friendly GUI interface using Tkinter
- Modular and scalable codebase for easy customization

---

## Tech Stack

| Technology | Purpose                        |
|------------|--------------------------------|
| Python     | Programming language           |
| YOLOv8     | Object detection                |
| Tkinter    | Graphical User Interface (GUI) |
| OpenCV     | Image and video processing     |

---
````
## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/MANASA-NUKALA/warehouse-box-counter-cv.git
cd warehouse-box-counter-cv
````

### 2. Create a Virtual Environment

#### For Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

#### For macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
cd gui
python app_gui.py
```

---

## Project Structure

```
warehouse-box-counter-cv/
├── box/                  # Model weights
├── box_counter/          # Box counting logic
├── gui/                  # GUI implementation (Tkinter)
├── preprocessing/        # Preprocessing scripts
├── webcam_capture/       # Webcam input scripts
├── yolo_module/          # YOLO detection logic
├── Testing2.0/           # Test images and GUI updates
├── detect_contours.py    # Contour-based detection
├── main.py               # Core detection script (CLI)
├── testing.py            # GUI testing script
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```
---

## 🎥 Demo Output

The following demo shows the real-time object detection and box counting using the application:

👉 [**Click here to watch the full demo video (MP4)**](https://github.com/MANASA-NUKALA/warehouse-box-counter-cv/raw/main/demo.mp4)


---

---

## Contributors

* [MANASA-NUKALA](https://github.com/MANASA-NUKALA)
* [vidyaganjasri](https://github.com/vidyaganjasri)
* [MissHaRin19](https://github.com/MissHaRin19)
* [AdulaAnusha22](https://github.com/AdulaAnusha22)
* [KPRANEETHA-1](https://github.com/KPRANEETHA-1)
* [Sudheshna193](https://github.com/Sudheshna193)

---
```
