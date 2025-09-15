import cv2

# Open a connection to the webcam (0 is usually the default webcam)
cap = cv2.VideoCapture(0)

# Check if webcam is opened successfully
if not cap.isOpened():
    print("Cannot open webcam")
    exit()

# Continuously capture frames from the webcam
while True:
    # Read frame-by-frame
    ret, frame = cap.read()

    # If frame reading was unsuccessful, break the loop
    if not ret:
        print("Can't receive frame (stream end?). Exiting...")
        break

    # Display the frame in a window named 'Webcam Feed'
    cv2.imshow('Webcam Feed', frame)

    # Wait for the 'q' key to be pressed to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
