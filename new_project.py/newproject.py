import cv2
import numpy as np

def detect_orientation(image_path):
    # Load image
    img = cv2.imread(image_path)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to segment text from background
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Apply Hough transform to detect lines
    lines = cv2.HoughLines(thresh, 1, np.pi / 180, 100)

    # Calculate the angle of the line(s) detected
    angle = 0
    for line in lines:
        for rho, theta in line:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))
            angle += np.degrees(np.arctan2(y2 - y1, x2 - x1))

    # Average the angles if multiple lines are detected
    angle /= len(lines)

    # Rotate the image to align text horizontally
    rotated = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    if angle < -45:
        rotated = cv2.rotate(rotated, cv2.ROTATE_180)
    elif angle > 45:
        rotated = cv2.rotate(rotated, cv2.ROTATE_180)

    return rotated
