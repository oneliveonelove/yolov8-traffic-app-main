<div align="center">
  <h2>Research and Analysis Software for Vehicle Trajectory Recognition and Target Detection Based on YOLOv8</h2>
  <p>
    <a href="https://github.com/ultralytics/assets/releases/tag/v8.2.0" target="_blank">
      <img width="100%" src="https://raw.githubusercontent.com/ultralytics/assets/main/yolov8/banner-yolov8.png" alt="YOLO Vision banner"></a>
  </p>
</div>

YOLOv8 can be used directly in a Python environment. A simple example is shown below.：

```python
from ultralytics import YOLO

# Load the model
model = YOLO("yolov8n.yaml")  # Building a new model from scratch
model = YOLO("yolov8n.pt")  # Load the pre-trained model (recommended for training)

# Using the model
model.train(data="coco128.yaml", epochs=3) # Training the model
metrics = model.val()  # Evaluate model performance on the validation set
results = model("https://ultralytics.com/images/bus.jpg")  # Predicting from an image
success = model.export(format="onnx") # Export the model as ONNX format
```

Check YOLOv8 [Python 文档](https://docs.ultralytics.com/usage/python) See below for more examples.

## <div align="center"> ⭐ New UI </div>
![Uploading 522978009-801caa13-24c2-443f-ba4b-3304d3543896.jpg…]()



- In the `ui` folder, there are `ui` files ending with `_new`, which are version 2.0 of the UI.

- Version 1.0 of the UI is designed for computer screens with a resolution of 2880×1800. If the resolution is insufficient, the UI interface may be too large and overflow the screen.

- Version 2.0 of the UI is designed for computer screens with a resolution of 1920×1080. The overall window is smaller than before, and the color scheme and other styles have been modified to make it more aesthetically pleasing and comfortable.

- Currently, `main.py` uses version 2.0 of the UI. The theme color changing function has not been modified, so it may look a little strange. You can customize the colors yourself or remove this function (it doesn't have much practical significance except for aesthetics), or write your own color scheme according to your preferences, or switch to version 1.0 of the UI. Multiple theme color schemes look quite good.
## <div align="center"> ⭐ 项目功能 </div>

### Traffic Object Detection and Instance Segmentation

This project, based on the YOLOv8 framework, enables traffic object detection. For images, it detects objects and annotates them with anchor boxes. For videos, it performs object detection analysis on each frame, also annotating with anchor boxes. The resulting object detection video tracks objects in real-time and displays them with colored boxes.

In addition to using conventional models for object detection, users can also use a dedicated instance segmentation model. After training and prediction, different objects can be identified. Unlike simple object detection, instance segmentation provides more detailed annotation of object contours and annotates the entire object with a specific color, producing more refined and better visualization results compared to ordinary object detection.

### Traffic Trajectory Recognition

This project can detect objects in imported traffic videos. Through object ID annotation and frame-by-frame video analysis, it captures the real-time position of each object and plots the position points in the video. Finally, it integrates these data to generate a video with the plotted object trajectories, achieving traffic vehicle trajectory recognition.

### Vehicle Line Crossing Count

In addition to vehicle tracking and trajectory drawing, this software can also count vehicle line crossings. Boundary lines can be drawn at key points in the video. When a vehicle crosses this line, the software captures the vehicle's coordinates frame by frame, assigns an ID, and increments the vehicle count to achieve line crossing counting.

### Generating Traffic Datasets

During object trajectory recognition, while capturing position coordinates and drawing trajectories, the software records the position information of different vehicles, along with their IDs, categories, and other information. After video detection is complete, the data is summarized and processed to generate a relatively ideal traffic dataset.

### Traffic Data Analysis

Importing the generated traffic dataset allows for detailed analysis of key data, including the detection counts of different object categories and vehicle position information. The data is presented visually using heatmaps, bar charts, and other methods, making it easy to clearly see the distribution of various data points.

## <div align="center"> ⭐ Project Deployment </div> Open the project in PyCharm, configure a venv virtual environment, and then install the dependencies using the following command:

```bash
pip install -r requirements.txt

```

## <div align="center"> ⭐ Detailed Usage Instructions </div>



Step 1 : Run tool install 
pip install -r requirements.txt 
or
python -m install -r requirements.txt                                                                           
Bước 2 : 
For track, count, and video, place the video in the video folder within the project, for example, the path C:\Users\Huy\Desktop\yolov8-traffic-app-main\video. The result will be in video_output. ![1](https://github.com/user-attachments/assets/801caa13-24c2-443f-ba4b-3304d3543896)
Bước 3:
Run file main.py
![2](https://github.com/user-attachments/assets/0891efe4-4e37-4647-b3c6-415202e37e3c)
<img width="1479" height="788" alt="Screenshot 2025-12-05 204806" src="https://github.com/user-attachments/assets/a5e8ac36-e776-4d34-85b0-3911a4d58232" />
