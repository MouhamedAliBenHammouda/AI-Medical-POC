import os
from PIL import Image as PILImage
import pandas as pd
from pdf2image import convert_from_path
import cv2
import numpy as np

# Specify Poppler path
POPPLER_PATH = r"C:\Users\LENOVO\Downloads\Release-24.08.0-0\poppler-24.08.0\Library\bin"

# Paths
DATA_DIR = "data"
OUTPUT_DIR = "data/processed"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def convert_pdf_to_images(pdf_path, output_dir):
    """Convert PDF to images and save as PNG."""
    images = convert_from_path(pdf_path, poppler_path=POPPLER_PATH)
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    image_paths = []
    for i, image in enumerate(images):
        output_path = os.path.join(output_dir, f"{base_name}_page{i+1}.png")
        image.save(output_path, "PNG")
        image_paths.append(output_path)
    return image_paths

def normalize_image(image_path, output_path, size=(512, 512)):
    """Normalize image size and convert to grayscale."""
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Failed to load image: {image_path}")
    img = cv2.resize(img, size)  # Resize to 512x512
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    cv2.imwrite(output_path, img)
    return output_path

def load_csv(csv_path):
    """Load CSV and return as DataFrame."""
    return pd.read_csv(csv_path)

def display_data():
    """Load and print sample data details."""
    print("=== Sample Data ===")
    
    # PDFs
    pdf_files = [f for f in os.listdir(DATA_DIR) if f.endswith(".pdf")]
    for pdf in pdf_files:
        pdf_path = os.path.join(DATA_DIR, pdf)
        try:
            image_paths = convert_pdf_to_images(pdf_path, OUTPUT_DIR)
            print(f"PDF: {pdf} -> Converted to {len(image_paths)} images: {image_paths}")
            
            # Normalize images
            for img_path in image_paths:
                norm_path = os.path.join(OUTPUT_DIR, f"norm_{os.path.basename(img_path)}")
                norm_path = normalize_image(img_path, norm_path)
                print(f"Normalized: {norm_path}")
        except Exception as e:
            print(f"Error processing PDF {pdf}: {e}")
    
    # X-rays
    xray_files = [f for f in os.listdir(DATA_DIR) if f.endswith((".png", ".jpg", ".jpeg"))]
    for xray in xray_files:
        xray_path = os.path.join(DATA_DIR, xray)
        norm_path = os.path.join(OUTPUT_DIR, f"norm_{xray}")
        try:
            norm_path = normalize_image(xray_path, norm_path)
            print(f"X-ray: {xray} -> Normalized: {norm_path}")
        except Exception as e:
            print(f"Error processing X-ray {xray}: {e}")
    
    # CSVs
    csv_files = [f for f in os.listdir(DATA_DIR) if f.endswith(".csv")]
    for csv in csv_files:
        csv_path = os.path.join(DATA_DIR, csv)
        try:
            df = load_csv(csv_path)
            print(f"CSV: {csv}\n{df.head()}\n")
        except Exception as e:
            print(f"Error processing CSV {csv}: {e}")

if __name__ == "__main__":
    display_data()