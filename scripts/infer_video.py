import cv2
from ultralytics import YOLO

# Paths
MODEL_PATH = "runs/segment/train/weights/best.pt"
VIDEO_PATH = "inputs/input_video.mp4"
OUTPUT_PATH = "outputs/segmented_output.mp4"

def segment_video():
    model = YOLO(MODEL_PATH)

    cap = cv2.VideoCapture(VIDEO_PATH)

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(OUTPUT_PATH, fourcc, fps, (width, height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame, conf=0.4)

        annotated_frame = results[0].plot()
        out.write(annotated_frame)

    cap.release()
    out.release()
    print("✅ Video segmentation complete!")

if __name__ == "__main__":
    segment_video()
