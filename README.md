# Pothole-Segmentation-using-YOLOv8
A computer vision project for detecting and segmenting road potholes in images and videos using YOLOv8 segmentation. Trained on a custom pothole dataset and supports video-based inference.

# Pothole Segmentation using YOLOv8

This project implements **pothole detection and segmentation** using the **YOLOv8 segmentation model**.
The model is trained on a pothole image segmentation dataset and can perform **frame-by-frame segmentation on videos**, highlighting pothole regions on roads.

The project is suitable for academic demonstrations, computer vision learning, and smart transportation applications.

---

## 📌 Features

* YOLOv8-based **image segmentation**
* Supports **video input**
* Outputs segmented video with potholes highlighted
* CPU-compatible inference
* Clean and modular project structure

---

## 🗂 Project Structure

```
pothole-segmentation/
│
├── data/
│   └── Pothole_Segmentation_YOLOv8/
│       ├── train/
│       │   ├── images/
│       │   └── labels/
│       ├── valid/
│       │   ├── images/
│       │   └── labels/
│       └── data.yaml
│
├── inputs/
│   └── input_video.mp4
│
├── outputs/
│   └── segmented_output.mp4
│
├── scripts/
│   ├── train.py
│   ├── infer_image.py
│   └── infer_video.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🧠 Model Used

* **YOLOv8 Segmentation (`yolov8n-seg`)**
* Trained on a custom pothole segmentation dataset
* Output includes segmentation masks over detected potholes

---

## ⚙️ Setup Instructions

### 1️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

* **Windows**

```bash
venv\Scripts\activate
```

* **Linux / macOS**

```bash
source venv/bin/activate
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🏋️ Training the Model

```bash
python scripts/train.py
```

> ⚠️ Training on CPU can be slow. GPU-based training (e.g., Google Colab) is recommended.

The trained model will be saved at:

```
runs/segment/train/weights/best.pt
```

---

## 🎥 Video Inference

1. Place your input video in:

```
inputs/input_video.mp4
```

2. Run segmentation:

```bash
python scripts/infer_video.py
```

3. Output video will be saved to:

```
outputs/segmented_output.mp4
```

---

## 🧪 Notes

* VS Code may not preview `.mp4` files correctly.
  Use **VLC Media Player** or **Windows Media Player** to view results.
* Short videos are recommended for CPU inference.

---

## 📚 Dataset

The dataset used for training contains annotated pothole images with segmentation labels in YOLOv8 format.

---

## 🚀 Future Enhancements

* Real-time webcam pothole detection
* Web-based UI using Streamlit or Flask
* Mask-only output for damage analysis
* Performance optimization for edge devices

---

## 👨‍💻 Author

**D D S S Mahith**

---

## 📄 License

This project is intended for **educational and research purposes**.
