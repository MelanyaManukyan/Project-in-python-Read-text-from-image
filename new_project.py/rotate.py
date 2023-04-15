import cv2
import numpy as np
import pytesseract
# Load the image
img = cv2.imread('paper.jpg')
# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Apply adaptive thresholding to the grayscale image
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
# Find the contours of the paper in the thresholded image
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# Find the largest contour (i.e., the paper)
max_contour = max(contours, key=cv2.contourArea)
# Approximate the contour to a polygon and calculate the bounding rectangle
epsilon = 0.05 * cv2.arcLength(max_contour, True)
approx = cv2.approxPolyDP(max_contour, epsilon, True)
rect = cv2.boundingRect(approx)
# Crop the image to the bounding rectangle of the paper
crop_img = img[rect[1]:rect[1]+rect[3], rect[0]:rect[0]+rect[2]]
# Convert the cropped image to grayscale
gray_crop = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
# Perform OCR on the cropped image to detect text orientation
text = pytesseract.image_to_string(gray_crop, lang="eng", config="--psm 0")
# Check if the text is horizontal or vertical
horizontal = all(c.isalnum() or c.isspace() for c in text)
if not horizontal:
    # Rotate the cropped image by 90 degrees counterclockwise
    crop_img = cv2.rotate(crop_img, cv2.ROTATE_90_COUNTERCLOCKWISE)
# Display the original and display cropped image rotated if the text is detected as vertical
cv2.imshow("Original Image", img)
cv2.imshow("Cropped Image", crop_img)
# Save the corrected image
cv2.imwrite("output.jpg", crop_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
