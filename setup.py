from PIL import Image
import os

def convert_png_to_jpeg_resolutions(input_png_path, output_directory):
    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Open the PNG image
    with Image.open(input_png_path) as img:
        # Convert the image to RGB mode if it's not
        if img.mode != 'RGB':
            img = img.convert('RGB')

        # Save as Baseline JPEG
        baseline_path = os.path.join(output_directory, 'baseline.jpg')
        img.save(baseline_path, 'JPEG')

        # Save as Progressive JPEG
        progressive_path = os.path.join(output_directory, 'progressive.jpg')
        img.save(progressive_path, 'JPEG', progressive=True)

        # Save multiple resolution images for simulating Hierarchical JPEG
        resolutions = [1, 0.75, 0.5, 0.25]  # Different scales for resolution
        for scale in resolutions:
            width, height = img.size
            resized_img = img.resize((int(width * scale), int(height * scale)), Image.LANCZOS)
            resized_path = os.path.join(output_directory, f'hierarchical_scale_{scale}.jpg')
            resized_img.save(resized_path, 'JPEG')
            print(f'Resized image saved: {resized_path}')

# Usage example
convert_png_to_jpeg_resolutions('static/lossless/Beautiful-landscape.png', 'static')
