import cv2
import pytesseract

# Load the image and convert it to grayscale
img = cv2.imread("input.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Perform OCR on the image to detect text orientation
text = pytesseract.image_to_string(gray, lang="eng", config="--psm 0")

# Check if the text is horizontal or vertical
horizontal = all(c.isalnum() or c.isspace() for c in text)
if not horizontal:
    # Rotate the image by 90 degrees counterclockwise
    img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

# Save the corrected image
cv2.imwrite("output.jpg", img)