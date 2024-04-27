import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import metrics
import os

# Function to evaluate image compression
def evaluate_image_compression(original, compressed):
    # Ensure the image is grayscale for comparison
    if len(original.shape) == 3:
        original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    if len(compressed.shape) == 3:
        compressed = cv2.cvtColor(compressed, cv2.COLOR_BGR2GRAY)
    
    # Calculate PSNR and SSIM
    psnr = metrics.peak_signal_noise_ratio(original, compressed)
    ssim = metrics.structural_similarity(original, compressed)
    return psnr, ssim

# Make sure results directories exist
if not os.path.exists('results'):
    os.makedirs('results')

# Load the original image and ensure it's RGB for JPEG/JPEG2000 compatibility
original_image = cv2.imread('lossless/Beautiful-landscape.png')
if original_image.shape[2] == 4:  # Convert RGBA to RGB
    original_image = cv2.cvtColor(original_image, cv2.COLOR_BGRA2BGR)

# Save as baseline JPEG
baseline_path = 'results/baseline.jpg'
cv2.imwrite(baseline_path, original_image, [int(cv2.IMWRITE_JPEG_QUALITY), 75])
compressed_baseline = cv2.imread(baseline_path)

# Save as JPEG2000
jpeg2000_path = 'results/jpeg2000.jp2'
cv2.imwrite(jpeg2000_path, original_image, [int(cv2.IMWRITE_JPEG2000_COMPRESSION_X1000), 75])
compressed_jpeg2000 = cv2.imread(jpeg2000_path)

# Evaluate Baseline JPEG
psnr_baseline, ssim_baseline = evaluate_image_compression(original_image, compressed_baseline)
print(f"Baseline JPEG PSNR: {psnr_baseline}, SSIM: {ssim_baseline}")

# Evaluate JPEG2000
psnr_jpeg2000, ssim_jpeg2000 = evaluate_image_compression(original_image, compressed_jpeg2000)
print(f"JPEG2000 PSNR: {psnr_jpeg2000}, SSIM: {ssim_jpeg2000}")


def plot_images_and_histograms(original, jpeg, jpeg2000):
    fig, axes = plt.subplots(3, 2, figsize=(12, 9))  # 3 rows for images and histograms, 2 columns

    # Set titles for columns
    axes[0, 0].set_title('Original Image')
    axes[0, 1].set_title('Histogram')
    
    # Show original image and histogram
    axes[0, 0].imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
    axes[0, 0].axis('off')
    axes[0, 1].hist(cv2.cvtColor(original, cv2.COLOR_BGR2RGB).ravel(), bins=256, color='blue', alpha=0.5)
    
    # Show JPEG image and histogram
    axes[1, 0].imshow(cv2.cvtColor(jpeg, cv2.COLOR_BGR2RGB))
    axes[1, 0].set_title('Baseline JPEG')
    axes[1, 0].axis('off')
    axes[1, 1].hist(cv2.cvtColor(jpeg, cv2.COLOR_BGR2RGB).ravel(), bins=256, color='green', alpha=0.5)
    
    # Show JPEG2000 image and histogram
    axes[2, 0].imshow(cv2.cvtColor(jpeg2000, cv2.COLOR_BGR2RGB))
    axes[2, 0].set_title('JPEG2000')
    axes[2, 0].axis('off')
    axes[2, 1].hist(cv2.cvtColor(jpeg2000, cv2.COLOR_BGR2RGB).ravel(), bins=256, color='red', alpha=0.5)
    
    # Show the plot
    plt.tight_layout()
    plt.show()

# Call the function with the original, baseline JPEG, and JPEG2000 images
plot_images_and_histograms(original_image, compressed_baseline, compressed_jpeg2000)
