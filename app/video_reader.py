import cv2

VIDEO_PATH = "videos/test_video.mp4"

cap = cv2.VideoCapture(VIDEO_PATH)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

print("Video opened successfully.")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Video ended.")
        break

    cv2.imshow("CrowdSense AI - Video", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("Video stopped by user.")
        break

cap.release()
cv2.destroyAllWindows()