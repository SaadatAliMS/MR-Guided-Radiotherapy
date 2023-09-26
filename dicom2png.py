import os
import pydicom
from PIL import Image
import numpy as np

def convert_dicom_to_png(dicom_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all DICOM files in the input folder
    dicom_files = [f for f in os.listdir(dicom_folder) if f.endswith('.dcm')]

    for dicom_file in dicom_files:
        dicom_path = os.path.join(dicom_folder, dicom_file)
        output_path = os.path.join(output_folder, os.path.splitext(dicom_file)[0] + '.png')

        # Read the DICOM file
        dicom_data = pydicom.dcmread(dicom_path)

        # Ensure the pixel data is normalized to 8-bit values
        dicom_image = dicom_data.pixel_array
        dicom_image = dicom_image - np.min(dicom_image)
        dicom_image = (dicom_image / np.max(dicom_image) * 255).astype(np.uint8)

        # Convert DICOM pixel data to a PIL Image
        dicom_image = Image.fromarray(dicom_image)

        # Save the image as PNG
        dicom_image.save(output_path)

        print(f"Converted {dicom_file} to {output_path}")

if __name__ == "__main__":
   # Replace these paths with your DICOM input folder and output folder
    dicom_folder = "D:\Reserach_Paper\syntheticCT_Project\data\ct"
    output_folder = "D:\Reserach_Paper\syntheticCT_Project\data\ct_png"
    convert_dicom_to_png(dicom_folder, output_folder)

    

    convert_dicom_to_png(dicom_folder, output_folder)
