# PyTextFinder

## Purpose/How It Works
This Python script extracts text from a video file using OpenCV and Tesseract OCR. 
It processes one frame per second and saves detected text in a text file while also 
storing processed frames with bounding boxes around the detected text.

## Features
Extracts text from video frames using Tesseract OCR

Processes one frame per second for efficiency

Saves detected text in detected_text.txt

Outputs processed frames with bounding boxes in output_frames folder

## Required Materials

Python 3.x

OpenCV (cv2)

Tesseract OCR

pytesseract library

## Installation

1.Install dependencies:

    pip install opencv-python pytesseract

## Usage
Place your video file in the main project folder.

Run the script (if not using PyCharm):

    python main.py

The detected text will be saved in detected_text.txt.

Processed frames with bounding boxes will be stored in the output_frames folder.

## Author
Merrick Pilon