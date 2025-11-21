# YOLOv8 doesnt have built in heatmap solution, YOLOv11 does

# YOLOv8 doesn't include the built-in Heatmap solution (that's provided for YOLO11). To generate a heatmap from a single image using YOLOv8, run detections with a YOLOv8 model, extract object centers (or bbox areas), and accumulate them into a 2D intensity map using NumPy/OpenCV. Minimal example below.

#- Install: `pip install ultralytics opencv-python numpy`
#- Run detections and build heatmap:


import cv2
import numpy as np
from ultralytics import YOLO  # YOLOv8 API

# load model (e.g., yolov8n.pt)
model = YOLO("yolov8n.pt")
img = cv2.imread("image.jpg")
h, w = img.shape[:2]

# run detection
results = model(img, conf=0.25)[0]  # first (and only) batch result

# create heatmap accumulator
heat = np.zeros((h, w), dtype=np.float32)

# for each bbox, add a gaussian blob at its center (or fill bbox)
for box in results.boxes.xyxy.numpy():
    x0, y0, x1, y1 = map(int, box)
    cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
    # parameters
    sigma = max(5, int(min(x1 - x0, y1 - y0) / 2))
    # make Gaussian kernel region
    size = sigma * 6
    gx = cv2.getGaussianKernel(size, sigma)
    gk = (gx @ gx.T).astype(np.float32)
    # position kernel on heatmap with bounds check
    ys = cy - size//2
    xs = cx - size//2
    y1i = min(h, ys + size)
    x1i = min(w, xs + size)
    y0i = max(0, ys)
    x0i = max(0, xs)
    gy0 = y0i - ys
    gx0 = x0i - xs
    gy1 = gy0 + (y1i - y0i)
    gx1 = gx0 + (x1i - x0i)
    heat[y0i:y1i, x0i:x1i] += gk[gy0:gy1, gx0:gx1]

# normalize and apply colormap
heat_norm = cv2.normalize(heat, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
colored = cv2.applyColorMap(heat_norm, cv2.COLORMAP_JET)
overlay = cv2.addWeighted(img, 0.6, colored, 0.4, 0)

cv2.imwrite("heatmap_overlay.jpg", overlay)


# If you want tracking + accumulation over frames (video), use the same accumulation across frames. For the YOLO11 built-in Heatmap solution docs and API, see the Heatmap guide and reference: [Heatmaps guide](https://docs.ultralytics.com/guides/heatmaps/) and [Heatmap reference](https://docs.ultralytics.com/reference/solutions/heatmap/).
