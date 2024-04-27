import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from PIL import Image

# Load the original image
original_image = cv2.imread('lossless/Beautiful-landscape.png')
if original_image is None:
    print("Error loading image")
    exit()

# Save initial low quality image
initial_quality = 10
cv2.imwrite('temp.jpg', original_image, [int(cv2.IMWRITE_JPEG_QUALITY), initial_quality])
progressive_image = Image.open('temp.jpg')

# Set up the plot
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)  # Adjust bottom to give space for the slider
img_display = plt.imshow(progressive_image)
plt.axis('off')

# Slider setup
ax_quality = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')
quality_slider = Slider(ax_quality, 'JPEG Quality', 10, 100, valinit=initial_quality)

# Update function for the slider
def update(val):
    quality = int(quality_slider.val)
    cv2.imwrite('temp.jpg', original_image, [int(cv2.IMWRITE_JPEG_QUALITY), quality])
    updated_image = Image.open('temp.jpg')
    img_display.set_data(updated_image)
    fig.canvas.draw_idle()

# Call update function on slider value change
quality_slider.on_changed(update)

# Show the plot with slider
plt.show()
