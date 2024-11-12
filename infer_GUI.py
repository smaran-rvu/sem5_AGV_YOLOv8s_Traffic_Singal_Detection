import tkinter as tk
from tkinter import filedialog, Label, messagebox
from PIL import Image, ImageTk
import torch
import cv2
import numpy as np
from ultralytics import YOLO

# Load the YOLOv8 model
model_path = "yolov8s_traffic_lights.pt"
model = YOLO(model_path)

# Function to perform inference
def detect_traffic_lights(image_path):
    # Load the image
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Run inference
    results = model.predict(source=image_rgb, save=False, show=False, verbose=False)

    # Check if any objects were detected
    if len(results[0].boxes) == 0:
        messagebox.showinfo("Detection Result", "No traffic signal detected.")
        return image_rgb

    # Iterate over the detected objects
    for box in results[0].boxes:
        # Get the bounding box coordinates, confidence, and class label
        x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
        confidence = box.conf[0].item()
        class_id = int(box.cls[0].item())
        label = model.names[class_id]

        # Define color based on the traffic signal color
        if label == "red":
            color = (255, 0, 0)
        elif label == "green":
            color = (0, 255, 0)
        elif label == "yellow":
            color = (0, 255, 255)
        else:
            color = (128, 128, 128)  # For "off" or unknown labels

        # Draw the bounding box and label on the image
        cv2.rectangle(image_rgb, (x1, y1), (x2, y2), color, 2)
        cv2.putText(
            image_rgb,
            f"{label} ({confidence:.2f})",
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            color,
            2,
        )

    return image_rgb

# Function to handle image upload and display
def upload_and_detect():
    # Open file dialog to select an image
    file_path = filedialog.askopenfilename(
        initialdir="/",
        title="Select an Image File",
    )   

    if not file_path:
        return

    # Perform traffic light detection
    detected_image = detect_traffic_lights(file_path)

    # Convert the image to display format
    detected_image_pil = Image.fromarray(detected_image)
    detected_image_tk = ImageTk.PhotoImage(detected_image_pil)

    # Update the label with the detected image
    image_label.config(image=detected_image_tk)
    image_label.image = detected_image_tk

# Create the main application window
root = tk.Tk()
root.title("Traffic Light Detector")
root.geometry("800x600")

# Create a button to upload and detect image
upload_button = tk.Button(root, text="Upload Image", command=upload_and_detect)
upload_button.pack(pady=20)

# Label to display the image
image_label = Label(root)
image_label.pack()

# Run the application
root.mainloop()
