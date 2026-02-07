import os
import cv2
import pytesseract
from fastapi import HTTPException

# Windows only (OK if already installed)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text_from_image(image_path: str) -> str:
    print("OCR path:", image_path)  # DEBUG

    if not os.path.exists(image_path):
        raise HTTPException(status_code=500, detail="Image not found on disk")

    img = cv2.imread(image_path)
    if img is None:
        raise HTTPException(
            status_code=500,
            detail="OpenCV failed to read image"
        )

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1]

    return pytesseract.image_to_string(gray)
