import linecache
import matplotlib.pyplot as plt
import pytesseract
import numpy as np
import cv2
#երկու ֆունկցիան կպցրած է իրար
#  path pytesseract
pytesseract.pytesseract.tesseract_cmd = r'D:\ProgramData\tesseract.exe'


class ImageProcesing:
    def __init__(self, first_image_path):
        self.first_image = first_image_path
        # self.rotated_image=rotated_image

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
        print(rotated_image.shape)
# Displaying the image
        cv2.imshow(window_name, rotated_image)
        cv2.waitKey(0)

    # def marked_img(self,rotated_image):
        # self.rotated_image = rotated_image
        gray = cv2.cvtColor(rotated_image, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
        kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
        dilated = cv2.dilate(thresh, kernel, iterations=13)
    # get contours
        contours, hierarchy = cv2.findContours(
            dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        for contour in contours:
            # get rectangle bounding contour
            [x, y, w, h] = cv2.boundingRect(contour)
# discard areas that are too large
            if h > rotated_image.shape[0] and w > rotated_image.shape[1]:
                continue
        cv2.rectangle(rotated_image, (x, y), (x+w, y+h), (0, 0, 255), 4)
    # write original image with added contours to disk
        print(rotated_image)
        # return cv2.imwrite('contoured.jpg', rotated_image)
        cv2.imwrite('contoured.jpg', rotated_image)
    def show_image(self):
        #show imnage
        plt.imshow(rotated_image)
        plt.show()

        return show_image(cv2.imread(rotated_image))



with open("text_by_photo.txt", "w") as f:

    text = pytesseract.image_to_string("k.png")

    f.write(text)

    # read each line
with open("text_by_photo.txt", "r") as f:
    content = f.readlines()
for line in range(len(content)):
    # print(len(content))
    count_line = int(input("Enter line_number --> "))
    if count_line > len(content):
        print(f"Please enter num in range(1: {len(content)})")
    print(linecache.getline(("text_by_photo.txt"), count_line))

rot_i = ImageProcesing("path")
# mark_i = ImageProcesing("path")
rot_i.rotated_img()
mark_i.marked_img(rot_i.rotated_img())

