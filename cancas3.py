import os
import cv2
import mediapipe as mp

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()


def identify_body_type(img_path):
    # Check if file exists
    if not os.path.exists(img_path):
        print(f"Error: Image file '{img_path}' does not exist.")
        return

    # Load image
    image = cv2.imread(img_path)
    if image is None:
        print(f"Error: Unable to load image at '{img_path}'. Check if the file is corrupted.")
        return

    # Convert to RGB for MediaPipe processing
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Process with MediaPipe
    results = pose.process(image_rgb)

    if results.pose_landmarks is None:
        print("No pose landmarks detected.")
        return

    # Extract pose landmarks
    landmarks = results.pose_landmarks.landmark

    # Get coordinates
    shoulder_y = int(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER].y * image.shape[0])
    hip_y = int(landmarks[mp_pose.PoseLandmark.LEFT_HIP].y * image.shape[0])
    left_hip_x = int(landmarks[mp_pose.PoseLandmark.LEFT_HIP].x * image.shape[1])
    right_hip_x = int(landmarks[mp_pose.PoseLandmark.RIGHT_HIP].x * image.shape[1])

    # Calculate torso height and hip width
    torso_height = hip_y - shoulder_y
    hip_width = right_hip_x - left_hip_x

    # Determine body type based on the ratio
    ratio = torso_height / hip_width
    print(f"Torso-to-hip ratio: {ratio:.2f}")

    if ratio < 1.0:
        body_type = "Thin"
    elif ratio > 1.2:
        body_type = "Fat"
    else:
        body_type = "Medium"

    # Display body type
    cv2.putText(image, f'Body Type: {body_type}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Body Type Identification', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Run the function
image_path = r'C:\project\VR_blind_shopping\test_data\v1.jpg'
identify_body_type(image_path)
