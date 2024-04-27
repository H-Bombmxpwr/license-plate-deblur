import cv2
import numpy as np
import matplotlib.pyplot as plt

def detect_blur_fft(image_path, size=60, thresh=10, vis=False):
    # Load the image in grayscale
    image = cv2.imread(image_path, 0)
    if image is None:
        raise ValueError("Image not found")
    
    # Resize the image to reduce computation time
    # image = cv2.resize(image, (800, 800))
    
    # Compute the FFT to find the frequency transform
    fft = np.fft.fft2(image)
    fft_shift = np.fft.fftshift(fft)
    
    # Compute magnitude spectrum
    magnitude = 20 * np.log(np.abs(fft_shift))
    
    # Create a mask that is True for high frequencies
    rows, cols = image.shape
    crow, ccol = rows//2, cols//2
    mask = np.zeros((rows, cols), np.uint8)
    mask[crow-size:crow+size, ccol-size:ccol+size] = 1
    fshift = fft_shift * mask
    
    # Inverse FFT to get back to the image
    f_ishift = np.fft.ifftshift(fshift)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)
    
    # Thresholding back image to find regions with significant high frequency
    blur_map = img_back < thresh
    blur_map = blur_map.astype(np.uint8) * 255

    if vis:
        plt.figure(figsize=(12, 6))
        plt.subplot(131), plt.imshow(image, cmap='gray'), plt.title('Original Image')
        plt.subplot(132), plt.imshow(magnitude, cmap='gray'), plt.title('Magnitude Spectrum')
        plt.subplot(133), plt.imshow(blur_map, cmap='gray'), plt.title('Blur Map')
        plt.show()

    return blur_map

# Usage example
blur_map = detect_blur_fft('path_to_your_image.jpg', vis=True)
