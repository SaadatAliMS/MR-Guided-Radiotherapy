from PIL import Image
import os

# Define the directories containing the input images
input_dir1 = "D:\Reserach_Paper\syntheticCT_Project\data\mri_png"
input_dir2 = "D:\Reserach_Paper\syntheticCT_Project\data\low_dimension_ct"

# Define the directory to save the stitched images
output_dir = "D:\Reserach_Paper\syntheticCT_Project\data\stitched"

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Get a list of files in both input directories
files1 = os.listdir(input_dir1)
files2 = os.listdir(input_dir2)

# Ensure both directories have the same number of images
if len(files1) != len(files2):
    print("Error: Both directories must have an equal number of images.")
    exit(1)

# Loop through each pair of images and stitch them
for i in range(len(files1)):
    # Open the images from both directories
    img1 = Image.open(os.path.join(input_dir1, files1[i]))
    img2 = Image.open(os.path.join(input_dir2, files2[i]))

    # Get the size of the images (assuming they have the same size)
    width, height = img1.size

    # Create a new image with double the width to accommodate both images side by side
    stitched_img = Image.new("RGB", (width *2, height))

    # Paste the images side by side on the new image
    stitched_img.paste(img1, (0, 0))
    stitched_img.paste(img2, (width, 0))

    # Save the stitched image to the output directory
    output_filename = f"stitched_{i}.png"
    stitched_img.save(os.path.join(output_dir, output_filename))

    print(f"Stitched and saved {output_filename}")

print("Stitching completed.")
