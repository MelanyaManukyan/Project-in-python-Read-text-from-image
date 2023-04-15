import cv2
import numpy as np

def detect_orientation(image_path):
    img = cv2.imread(image_path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    lines = cv2.HoughLines(thresh, 1, np.pi / 180, 100)

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

    angle /= len(lines)

    rotated = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    if angle < -45:
        rotated = cv2.rotate(rotated, cv2.ROTATE_180)
    elif angle > 45:
        rotated = cv2.rotate(rotated, cv2.ROTATE_180)

    return rotated
