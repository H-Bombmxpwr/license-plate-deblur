from PIL import Image
import os

def convert_png_to_jpeg_types(input_png_path, output_directory):
    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Open the PNG image
    with Image.open(input_png_path) as img:
        # Convert the image to RGB mode if it's not
        if img.mode != 'RGB':
            img = img.convert('RGB')

        # Define the output paths
        baseline_path = os.path.join(output_directory, 'baseline.jpg')
        progressive_path = os.path.join(output_directory, 'progressive.jpg')
        hierarchical_path = os.path.join(output_directory, 'hierarchical.jpg')  # Note: hierarchical JPEG is not typically supported by PIL

        # Save as Baseline JPEG
        img.save(baseline_path, 'JPEG')

        # Save as Progressive JPEG
        img.save(progressive_path, 'JPEG', progressive=True)

        # Attempt to save as Hierarchical JPEG (not supported, will save as another baseline JPEG)
        img.save(hierarchical_path, 'JPEG')

        print(f'Files saved: {baseline_path}, {progressive_path}, {hierarchical_path}')

# Usage example
convert_png_to_jpeg_types('static/lossless/Beautiful-landscape.png', 'static')