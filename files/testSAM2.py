############
## # UPDATE dataset_dir TO YOUR DATASET DIRECTORY(Both images and labels)
############

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw

def visualize_yolo_segmentation(dataset_dir, num_images=5, random_sample=True):
    """
    Visualize YOLO segmentation annotations on top of images
    
    Args:
        dataset_dir: Root directory with 'images' and 'labels' folders
        num_images: Number of images to visualize
        random_sample: If True, randomly samples images, otherwise takes first N
    """
    image_dir = os.path.join(dataset_dir, 'images')
    label_dir = os.path.join(dataset_dir, 'labels')
    
    # Get list of image files
    image_files = [f for f in os.listdir(image_dir) 
                   if f.lower().endswith(('.jpg', '.png', '.jpeg'))]
    
    if not image_files:
        print(f"No images found in {image_dir}")
        return
    
    # Select images to visualize
    if random_sample:
        indices = np.random.choice(len(image_files), min(num_images, len(image_files)), replace=False)
        selected_files = [image_files[i] for i in indices]
    else:
        selected_files = image_files[:min(num_images, len(image_files))]
    
    print(f"Visualizing {len(selected_files)} images...")
    
    # Create visualization directory
    viz_dir = os.path.join(dataset_dir, 'visualizations')
    os.makedirs(viz_dir, exist_ok=True)
    
    # Define colors for different classes
    colors = [
        (255, 0, 0),    # Red
        (0, 255, 0),    # Green
        (0, 0, 255),    # Blue
        (255, 255, 0),  # Yellow
        (255, 0, 255),  # Magenta
        (0, 255, 255),  # Cyan
        (255, 165, 0),  # Orange
        (128, 0, 128),  # Purple
        (0, 128, 0),    # Dark Green
        (128, 128, 0)   # Olive
    ]
    
    for image_file in selected_files:
        # Load image
        image_path = os.path.join(image_dir, image_file)
        img = cv2.imread(image_path)
        if img is None:
            print(f"Could not load image: {image_path}")
            continue
        
        # Convert BGR to RGB for better visualization
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_height, img_width = img_rgb.shape[:2]
        
        # Check for label file
        label_file = os.path.splitext(image_file)[0] + '.txt'
        label_path = os.path.join(label_dir, label_file)
        
        if not os.path.exists(label_path):
            print(f"No label file for {image_file}, creating image without annotations...")
            # Save image without annotations
            viz_path = os.path.join(viz_dir, f"no_labels_{image_file}")
            plt.figure(figsize=(12, 8))
            plt.imshow(img_rgb)
            plt.title(f"{image_file} - No Labels")
            plt.axis('off')
            plt.savefig(viz_path, bbox_inches='tight', dpi=150)
            plt.close()
            print(f"Saved: {viz_path}")
            continue
        
        # Read and parse YOLO segmentation annotations
        with open(label_path, 'r') as f:
            annotations = []
            for line_num, line in enumerate(f.readlines()):
                parts = line.strip().split()
                if len(parts) < 5:
                    continue
                
                try:
                    class_id = int(parts[0])
                    coords = list(map(float, parts[1:]))
                    
                    # Convert normalized coordinates to pixel coordinates
                    polygon = []
                    for i in range(0, len(coords), 2):
                        x = int(coords[i] * img_width)
                        y = int(coords[i+1] * img_height)
                        polygon.append((x, y))
                    
                    if len(polygon) >= 3:
                        annotations.append({
                            'class_id': class_id,
                            'polygon': polygon,
                            'bbox': self._get_bbox_from_polygon(polygon)
                        })
                except Exception as e:
                    print(f"Error parsing line {line_num} in {label_file}: {e}")
                    continue
        
        # Create visualization
        fig, axes = plt.subplots(1, 2, figsize=(20, 10))
        
        # Plot 1: Original image
        axes[0].imshow(img_rgb)
        axes[0].set_title(f"Original: {image_file}")
        axes[0].axis('off')
        
        # Plot 2: Image with annotations
        axes[1].imshow(img_rgb)
        
        if annotations:
            print(f"\n{image_file}: {len(annotations)} annotations")
            
            for i, ann in enumerate(annotations):
                class_id = ann['class_id']
                polygon = ann['polygon']
                bbox = ann['bbox']
                
                # Get color for this class
                color_idx = class_id % len(colors)
                color = colors[color_idx]
                
                # Convert color to tuple for matplotlib
                color_normalized = (color[0]/255, color[1]/255, color[2]/255)
                
                # Draw polygon
                polygon_array = np.array(polygon)
                axes[1].fill(polygon_array[:, 0], polygon_array[:, 1], 
                           color=color_normalized, alpha=0.3, label=f'Class {class_id}')
                
                # Draw polygon outline
                axes[1].plot(polygon_array[:, 0], polygon_array[:, 1], 
                           color=color_normalized, linewidth=2)
                
                # Draw bounding box
                x_min, y_min, x_max, y_max = bbox
                rect = plt.Rectangle((x_min, y_min), x_max - x_min, y_max - y_min,
                                   fill=False, edgecolor=color_normalized, 
                                   linewidth=1, linestyle='--')
                axes[1].add_patch(rect)
                
                # Add class label
                label_x = x_min + 5
                label_y = y_min - 5 if y_min > 20 else y_min + 15
                axes[1].text(label_x, label_y, f'Class {class_id}', 
                           color='white', fontsize=10, fontweight='bold',
                           bbox=dict(boxstyle="round,pad=0.3", 
                                    facecolor=color_normalized, 
                                    edgecolor='white', alpha=0.7))
                
                # Print polygon points for debugging
                print(f"  Annotation {i}: Class {class_id}, {len(polygon)} points")
                if len(polygon) <= 10:  # Print if not too many points
                    print(f"    Points: {polygon}")
        
        else:
            axes[1].text(img_width/2, img_height/2, "No valid annotations", 
                       ha='center', va='center', fontsize=14, color='red',
                       bbox=dict(boxstyle="round,pad=0.5", facecolor='white', alpha=0.8))
        
        axes[1].set_title(f"With Annotations: {image_file}\nTotal annotations: {len(annotations)}")
        axes[1].axis('off')
        
        # Add legend if there are annotations
        if annotations:
            handles, labels = axes[1].get_legend_handles_labels()
            if handles:  # Only add legend if we have handles
                by_label = dict(zip(labels, handles))  # Remove duplicates
                axes[1].legend(by_label.values(), by_label.keys(), 
                             loc='upper right', bbox_to_anchor=(1.05, 1))
        
        # Save visualization
        viz_filename = os.path.splitext(image_file)[0] + '_viz.png'
        viz_path = os.path.join(viz_dir, viz_filename)
        plt.tight_layout()
        plt.savefig(viz_path, bbox_inches='tight', dpi=150)
        plt.close()
        
        print(f"Saved visualization: {viz_path}")
        
        # Also create a detailed view with polygon points numbered
        if annotations:
            create_detailed_view(image_file, img_rgb, annotations, viz_dir)
    
    print(f"\nVisualizations saved in: {viz_dir}")
    
    # Display one sample in notebook if running interactively
    try:
        from IPython.display import Image as IPImage, display
        if selected_files:
            sample_viz = os.path.join(viz_dir, os.path.splitext(selected_files[0])[0] + '_viz.png')
            if os.path.exists(sample_viz):
                print("\nSample visualization:")
                display(IPImage(filename=sample_viz))
    except:
        pass

def _get_bbox_from_polygon(polygon):
    """Calculate bounding box from polygon points"""
    xs = [p[0] for p in polygon]
    ys = [p[1] for p in polygon]
    return min(xs), min(ys), max(xs), max(ys)

def create_detailed_view(image_file, img_rgb, annotations, output_dir):
    """Create a detailed visualization with numbered polygon points"""
    fig, ax = plt.subplots(1, 1, figsize=(15, 10))
    ax.imshow(img_rgb)
    
    for i, ann in enumerate(annotations):
        class_id = ann['class_id']
        polygon = ann['polygon']
        
        # Get color
        colors = [(255,0,0), (0,255,0), (0,0,255), (255,255,0), (255,0,255)]
        color_idx = class_id % len(colors)
        color = colors[color_idx]
        color_normalized = (color[0]/255, color[1]/255, color[2]/255)
        
        # Draw polygon with transparency
        polygon_array = np.array(polygon)
        ax.fill(polygon_array[:, 0], polygon_array[:, 1], 
                color=color_normalized, alpha=0.2)
        
        # Draw polygon outline
        ax.plot(polygon_array[:, 0], polygon_array[:, 1], 
                color=color_normalized, linewidth=2, marker='o')
        
        # Number each point
        for j, (x, y) in enumerate(polygon):
            ax.text(x, y, str(j), color='white', fontsize=8, fontweight='bold',
                   ha='center', va='center',
                   bbox=dict(boxstyle="circle,pad=0.3", 
                            facecolor=color_normalized, alpha=0.8))
    
    ax.set_title(f"Detailed View: {image_file}\nPolygon points are numbered")
    ax.axis('off')
    
    # Save detailed view
    detailed_filename = os.path.splitext(image_file)[0] + '_detailed.png'
    detailed_path = os.path.join(output_dir, detailed_filename)
    plt.savefig(detailed_path, bbox_inches='tight', dpi=150)
    plt.close()
    print(f"Saved detailed view: {detailed_path}")

def check_yolo_format_examples(dataset_dir, num_examples=3):
    """
    Check and print examples of YOLO annotation format
    """
    label_dir = os.path.join(dataset_dir, 'labels')
    
    if not os.path.exists(label_dir):
        print(f"Labels directory not found: {label_dir}")
        return
    
    label_files = [f for f in os.listdir(label_dir) if f.endswith('.txt')]
    
    if not label_files:
        print("No label files found")
        return
    
    print("\n=== Checking YOLO Format Examples ===")
    
    for i, label_file in enumerate(label_files[:num_examples]):
        label_path = os.path.join(label_dir, label_file)
        
        print(f"\n{label_file}:")
        print("-" * 50)
        
        with open(label_path, 'r') as f:
            lines = f.readlines()
            
        if not lines:
            print("  (Empty file)")
            continue
        
        # Show first 3 annotations
        for j, line in enumerate(lines[:3]):
            parts = line.strip().split()
            if len(parts) < 5:
                print(f"  Line {j}: INVALID - {line.strip()}")
                continue
            
            class_id = parts[0]
            coords = parts[1:]
            num_points = len(coords) // 2
            
            print(f"  Line {j}: Class {class_id}, {num_points} points")
            print(f"    Coords: {coords[:6]}..." if len(coords) > 6 else f"    Coords: {coords}")
        
        if len(lines) > 3:
            print(f"  ... and {len(lines) - 3} more lines")

# Run the visualization
if __name__ == "__main__":
    
    dataset_path = 'C:/dataset/path/folder/images_and_labels'   # UPDATE THIS PATH to your dataset directory(containing both images and labels)
    
    # First, check the format of your YOLO files
    check_yolo_format_examples(dataset_path, num_examples=3)
    
    # Then visualize
    visualize_yolo_segmentation(dataset_path, num_images=10, random_sample=True)
