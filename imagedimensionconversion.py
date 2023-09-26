from PIL import Image
import os

# Define the input and output directories
input_dir = "D:\Reserach_Paper\syntheticCT_Project\data\ct_png"
output_dir = "D:\Reserach_Paper\syntheticCT_Project\data\low_dimension_ct"

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Get a list of image files in the input directory
image_files = [f for f in os.listdir(input_dir) if f.endswith(".png")]

# Loop through each image file and resize it
for filename in image_files:
    input_path = os.path.join(input_dir, filename)
    output_path = os.path.join(output_dir, filename)

    # Open the image
    img = Image.open(input_path)

    # Resize the image to 25x256 dimensions
    new_width = 256
    new_height = 256
    resized_img = img.resize((new_width, new_height), Image.ANTIALIAS)

    # Save the resized image to the output directory
    resized_img.save(output_path)

    print(f"Resized and saved: {output_path}")

print("Resizing completed.")
