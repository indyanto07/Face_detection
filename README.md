# Face_detection
# Real-Time Face Detection Using OpenCV

This project is a **real-time face detection application** built with **Python** and **OpenCV**. The program accesses a webcam, detects faces in each frame, draws bounding boxes around detected faces, and displays the total number of people on the screen.

## Features

* Real-time face detection using a webcam
* Bounding box visualization for detected faces
* Face count display on the video feed
* Mirrored camera view for a more natural display
* Exit the application by pressing the **q** key

## Technologies Used

* Python 3
* OpenCV (cv2)
* Haar Cascade Classifier (XML)

## Requirements

Make sure Python is installed on your system.

### Install OpenCV

pip install opencv-python

## Required Files

* `face_ref.xml` → Haar Cascade file for face detection
* Python script (e.g., `main.py`)

> Ensure that `face_ref.xml` is located in the same directory as the Python script.

## How to Run the Program

1. Connect a webcam to your computer
2. Run the program using the command:

python main.py

3. A camera window titled **Human** will appear
4. Press **q** to exit the program

## How It Works

1. The webcam captures video frames
2. Each frame is converted to grayscale for optimization
3. Haar Cascade detects faces in the frame
4. Bounding boxes are drawn around detected f
