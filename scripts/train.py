from ultralytics import YOLO

def train():
    model = YOLO("yolov8n-seg.pt")

    model.train(
        data="data/Pothole_Segmentation_YOLOv8/data.yaml",
        epochs=10,
        imgsz=640,
        batch=4,        
        device="cpu"    
    )

if __name__ == "__main__":
    train()
