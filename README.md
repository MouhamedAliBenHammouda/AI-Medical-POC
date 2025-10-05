# AI Medical POC
Prototype for AI-based medical data analysis (Sprint 1).

## Data Sources
- Doctor Notes: [TemplateLab](https://templatelab.com/doctors-note-template)
- Prescriptions: [JotForm](https://www.jotform.com/pdf-templates/prescription-template)
- X-rays: [NIH Chest X-ray Sample](https://www.kaggle.com/datasets/nih-chest-xrays/sample)
- Lab Tests: [Kaggle Healthcare Dataset](https://www.kaggle.com/datasets/prasad22/healthcare-dataset)

## Day 3: Preprocessing
- Script: `scripts/preprocess_data.py`
- Converts PDFs to PNGs using pdf2image (with Poppler at `C:\Users\LENOVO\Downloads\Release-24.08.0-0\poppler-24.08.0\Library\bin`), normalizes images to 512x512 grayscale using OpenCV, loads CSVs with Pandas.
- Output: Processed images in `data/processed/`.
- Dependencies: pdf2image, Poppler.