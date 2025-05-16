import cv2
from datetime import datetime
import os
import shutil
from tkinter import Tk, filedialog  # 🔁 GUI for file selection

class WebcamCapture:
    def __init__(self, output_dir="captures"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    @staticmethod
    def get_timestamp():
        return datetime.now().strftime("%Y%m%d_%H%M%S")

    def capture_image(self):
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("❌ Cannot open webcam")
            return None

        print("📷 Press SPACE to capture the image. Press ESC to cancel.")
        filename = None

        while True:
            ret, frame = cap.read()
            if not ret:
                print("❌ Failed to read from webcam.")
                break

            cv2.imshow("📸 Press SPACE to capture", frame)
            key = cv2.waitKey(1)

            if key == 27:  # ESC
                print("❌ Cancelled.")
                break
            elif key == 32:  # SPACE
                filename = os.path.join(self.output_dir, f"image_{self.get_timestamp()}.jpg")
                cv2.imwrite(filename, frame)
                abs_path = os.path.abspath(filename)
                print(f"✅ Image saved: {abs_path}")
                break

        cap.release()
        cv2.destroyAllWindows()
        return os.path.abspath(filename) if filename else None

    def record_video(self):
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("❌ Error: Cannot open webcam")
            return None

        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        filename = os.path.join(self.output_dir, f"video_{self.get_timestamp()}.avi")
        out = cv2.VideoWriter(filename, fourcc, 20.0, (640, 480))

        print("🎥 Recording started. Press 'q' to stop.")

        while True:
            ret, frame = cap.read()
            if not ret:
                print("❌ Failed to read frame")
                break

            out.write(frame)
            cv2.imshow('Video Recording - Press q to stop', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("🛑 Recording stopped.")
                break

        cap.release()
        out.release()
        cv2.destroyAllWindows()
        abs_path = os.path.abspath(filename)
        print(f"✅ Video saved as {abs_path}")
        return abs_path

    def upload_image(self):
        print("📂 Select an image file to upload...")
        root = Tk()
        root.withdraw()
        filetypes = [("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif")]
        source_path = filedialog.askopenfilename(title="Select Image File", filetypes=filetypes)
        root.destroy()

        if not source_path:
            print("❌ No file selected.")
            return None

        ext = os.path.splitext(source_path)[-1]
        dest_path = os.path.join(self.output_dir, f"uploaded_image_{self.get_timestamp()}{ext}")
        shutil.copy(source_path, dest_path)
        abs_path = os.path.abspath(dest_path)
        print(f"✅ Image uploaded to: {abs_path}")
        return abs_path

    def upload_video(self):
        print("📂 Select a video file to upload...")
        root = Tk()
        root.withdraw()
        filetypes = [("Video Files", "*.mp4 *.avi *.mov *.mkv")]
        source_path = filedialog.askopenfilename(title="Select Video File", filetypes=filetypes)
        root.destroy()

        if not source_path:
            print("❌ No file selected.")
            return None

        ext = os.path.splitext(source_path)[-1]
        dest_path = os.path.join(self.output_dir, f"uploaded_video_{self.get_timestamp()}{ext}")
        shutil.copy(source_path, dest_path)
        abs_path = os.path.abspath(dest_path)
        print(f"✅ Video uploaded to: {abs_path}")
        return abs_path

def main():
    webcam = WebcamCapture()

    print("\n📷 Webcam Capture Tool")
    print("1. Capture Image")
    print("2. Record Video")
    print("3. Upload Image")
    print("4. Upload Video")
    choice = input("Enter your choice (1-4): ")

    path = None
    if choice == '1':
        path = webcam.capture_image()
    elif choice == '2':
        path = webcam.record_video()
    elif choice == '3':
        path = webcam.upload_image()
    elif choice == '4':
        path = webcam.upload_video()
    else:
        print("❌ Invalid choice.")

    if path:
        print(f"📁 File path returned: {path}")
    return path

if __name__ == "__main__":
    main()

