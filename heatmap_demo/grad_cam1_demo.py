import torch
import torch.nn.functional as F
from torchvision import transforms
from torchvision.models import resnet50, ResNet50_Weights
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# ---------- 1. Load and prepare the image ----------

img_path = "input.jpg"  # Make sure this file exists in the same folder

# Open image
img = Image.open(img_path).convert("RGB")

# Save a copy as numpy array for display
img_np = np.array(img)

# Preprocessing for ResNet (ImageNet normalization and resize)
preprocess = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],  # ImageNet mean
        std=[0.229, 0.224, 0.225]    # ImageNet std
    ),
])

input_tensor = preprocess(img).unsqueeze(0)  # shape: [1, 3, 224, 224]

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
input_tensor = input_tensor.to(device)

# ---------- 2. Load pretrained ResNet50 model ----------

weights = ResNet50_Weights.DEFAULT
model = resnet50(weights=weights)
model = model.to(device)
model.eval()

# Get class labels (ImageNet categories)
categories = weights.meta["categories"]

# ---------- 3. Hook into the last conv layer ----------

# For ResNet50, we'll use the last block of layer4
target_layer = model.layer4[-1].conv3

activations = None
grads = None

def forward_hook(module, input, output):
    global activations
    activations = output

def backward_hook(module, grad_input, grad_output):
    global grads
    grads = grad_output[0]

# Register hooks
forward_handle = target_layer.register_forward_hook(forward_hook)
backward_handle = target_layer.register_backward_hook(backward_hook)

# ---------- 4. Forward pass through the model ----------

output = model(input_tensor)  # shape: [1, 1000]
pred_index = output.argmax(dim=1).item()
pred_score = output[0, pred_index].item()
pred_label = categories[pred_index]

print(f"Predicted class index: {pred_index}")
print(f"Predicted label: {pred_label}")
print(f"Predicted score (logits): {pred_score:.4f}")

# ---------- 5. Backward pass to get gradients ----------

model.zero_grad()
class_score = output[0, pred_index]
class_score.backward()

# Now we have:
# activations -> feature maps at target layer
# grads -> gradients of class score w.r.t. those feature maps

# ---------- 6. Compute Grad-CAM heatmap ----------

# activations: [1, C, H, W]
# grads: [C, H, W] after we take the first batch element

# Take the first (and only) batch
activations = activations[0]           # [C, H, W]
grads = grads                          # [C, H, W]

# Global average pool the gradients over H and W -> weights for each channel
weights_cam = grads.mean(dim=(1, 2))   # [C]

# Compute the weighted sum of activations
cam = torch.zeros(activations.shape[1:], dtype=torch.float32).to(device)  # [H, W]

for i, w in enumerate(weights_cam):
    cam += w * activations[i, :, :]

# Apply ReLU to keep only positive values
cam = F.relu(cam)

# Normalize cam to [0, 1]
cam -= cam.min()
if cam.max() != 0:
    cam /= cam.max()

# Move to CPU numpy array
cam = cam.detach().cpu().numpy()  # [H, W]

# ---------- 7. Resize CAM to match original image size ----------

cam_image = Image.fromarray(np.uint8(cam * 255))  # scale to [0,255] for resizing
cam_resized = cam_image.resize((img_np.shape[1], img_np.shape[0]))
cam_resized = np.array(cam_resized) / 255.0  # back to [0,1]

# ---------- 8. Show original image + heatmap overlay ----------

plt.figure(figsize=(12, 5))

# Original image
plt.subplot(1, 2, 1)
plt.imshow(img_np)
plt.axis("off")
plt.title("Original Image")

# Heatmap overlay
plt.subplot(1, 2, 2)
plt.imshow(img_np)
plt.imshow(cam_resized, cmap="jet", alpha=0.4)  # alpha controls transparency
plt.axis("off")
plt.title(f"Grad-CAM Heatmap\nPredicted: {pred_label}")

plt.tight_layout()
plt.show()

# ---------- 9. Remove hooks ----------

forward_handle.remove()
backward_handle.remove()

