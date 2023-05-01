import linecache
import matplotlib.pyplot as plt
import pytesseract
import numpy as np
import cv2

#  path pytesseract
pytesseract.pytesseract.tesseract_cmd = r'D:\ProgramData\tesseract.exe'


class ImageProcesing:
    def __init__(self, first_image_path):
        self.first_image = first_image_path

    def rotated_img(self):
        first_image_path = "k.png"
# def rotated_img(first_image):
        src = cv2.imread(first_image_path)

# Window name in which image is displayed
        window_name = 'Image'
 # Using cv2.rotate() method
# Using cv2.ROTATE_90_COUNTERCLOCKWISE
# rotate by 270 degrees clockwise
        rotated_image = cv2.rotate(src, cv2.ROTATE_90_COUNTERCLOCKWISE)

# Displaying the image
        cv2.imshow(window_name, rotated_image)
        cv2.waitKey(0)


rot_i = ImageProcesing("path")
rot_i.rotated_img()
