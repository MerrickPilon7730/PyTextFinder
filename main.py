import cv2
import pytesseract
import os

# Name of video in main project directory
video_path = "video2.mkv"
cap = cv2.VideoCapture(video_path)

# Change if it is installed in a different directory
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Get video FPS to process one frame per second
fps = int(cap.get(cv2.CAP_PROP_FPS))
frame_interval = fps

output_text_file = "detected_text.txt"
output_frames_folder = "output_frames"
os.makedirs(output_frames_folder, exist_ok=True)

# Overrides the output file each time it's run
with open(output_text_file, "w", encoding="utf-8") as f:
    f.write("Detected Text from Video:\n\n")

frame_count = 0
saved_frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1

    # Process every nth frame
    if frame_count % frame_interval != 0:
        continue

    saved_frame_count += 1
    print(f"Rendering Frame {saved_frame_count}")

    # Convert frame to grayscale so OCR can read it better
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to enhance text detection
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

    # Allows the OCR to identify text regions better
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    detected_text = ""

    # Draw bounding boxes around the text and extract it
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if w > 50 and h > 20:
            roi = gray[y:y+h, x:x+w]
            text = pytesseract.image_to_string(roi, config="--psm 6").strip()

            if text:  # Ignore empty results
                detected_text += f"Frame {saved_frame_count}: {text}\n"
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Output any detected text
    if detected_text:
        with open(output_text_file, "a", encoding="utf-8") as f:
            f.write(detected_text)

        # Save the frame with the bounding boxes
        frame_filename = os.path.join(output_frames_folder, f"frame_{saved_frame_count}.jpg")
        cv2.imwrite(frame_filename, frame)

cap.release()
cv2.destroyAllWindows()

print(f"Detected text has been saved to {output_text_file}")
print(f"Processed frames are saved in the '{output_frames_folder}' folder")
