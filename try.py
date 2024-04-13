import yolov8
import cv2

# Load the YOLOv8 model
model = yolov8.load("yolov8x")

# Open the input video
cap = cv2.VideoCapture('download.mp4')

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

# Process the video
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Perform detection
    results = model(frame)
    
    # Draw results on the frame
    results.render()  # This modifies the frame in-place

    # Write the frame
    out.write(frame)

    # Display the resulting frame
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything if job is finished
cap.release()
out.release()
