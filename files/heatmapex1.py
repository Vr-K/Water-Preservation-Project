# Yes, you can generate heatmaps for still images using Ultralytics solutions. The core heatmap functionality is designed around video streams, but the same approach can be adapted to process single images—by treating your image as a single frame and passing it through the heatmap solution. The process involves initializing the heatmap object and calling it on your image data

# links [(1)](https://docs.ultralytics.com/guides/heatmaps)[(2)](https://docs.ultralytics.com/reference/solutions/heatmap)[(3)](https://github.com/orgs/ultralytics/discussions/9662).

# For example, with Ultralytics YOLO11, you can use the Heatmap solution like this:

import cv2
from ultralytics import solutions
im0 = cv2.imread("path/to/image.jpg")
heatmap = solutions.Heatmap(colormap=cv2.COLORMAP_PARULA, show=True, model="yolo11n.pt")
results = heatmap(im0)
cv2.imshow("Heatmap", results.plot_im)
cv2.waitKey(0)
cv2.destroyAllWindows()

# [(1)](https://docs.ultralytics.com/guides/heatmaps)

# This approach generates a heatmap for a single image. If you want to visualize specific classes, you can use the classes argument when initializing the Heatmap object[(1)](https://docs.ultralytics.com/guides/heatmaps).
