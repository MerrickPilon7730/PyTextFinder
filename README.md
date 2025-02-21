# PyTextFinder

## Purpose/How It Works
This Python script extracts text from a video file using OpenCV and Tesseract OCR. 
It processes one frame per second and saves detected text in a text file while also 
storing processed frames with bounding boxes around the detected text (can be 
commented out, mainly for debugging purposes).

## Features
Extracts text from video frames using Tesseract OCR

Processes one frame per second for efficiency

Saves detected text in detected_text.txt

Outputs processed frames with bounding boxes in output_frames folder

## Required Materials

Python 3.x

OpenCV (cv2)

pytesseract library

## Installation

1.Install dependencies:

    pip install opencv-python pytesseract

## Usage
Place your video file in the main project folder.

Run the script:

    python main.py

The detected text will be saved in detected_text.txt.

Processed frames with bounding boxes will be stored in the output_frames folder.

## License

I added a GNU GPL(General Public License) because I wanted to ensure that it remains
as an open source program under the same license. It allows others to freely use, modify,
and distribute the code with minimal restrictions, focusing on collaboration.

## Author
Merrick Pilon