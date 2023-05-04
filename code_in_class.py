import linecache
import matplotlib.pyplot as plt
import pytesseract
import numpy as np
import cv2


class ImageProcesing:
    def __init__(self, first_image_path, cont_file):
        self.first_image = first_image_path
        self.context_file = cont_file

    # rotated image
    def rotated_img(self):

        src = cv2.imread(self.first_image_path)
        # Perform OCR on the image to detect text orientation
        text = pytesseract.image_to_string(gray, lang="eng", config="--psm 0")

        # Check if the text is horizontal or vertical
        horizontal = all(c.isalnum() or c.isspace() for c in text)
        if not horizontal:
        # rotate by 270 degrees clockwise
            rotated_image = cv2.rotate(src, cv2.ROTATE_90_COUNTERCLOCKWISE)
            return rotated_image
        elif horizontal:
            text = pytesseract.image_to_string(Image.fromarray(img_with_contours), lang="eng")
            f.write(text)
        else:
            # Rotate the cropped image by 180 degrees counterclockwise
            crop_img = cv2.rotate(img_with_contours, cv2.ROTATE_180_COUNTERCLOCKWISE)
            text = pytesseract.image_to_string(Image.fromarray(crop_img), lang="eng")
            f.write(text)
    # marked image
    def marked_img(self):
        self.rotated_image = self.rotated_img()
        # grayscale
        gray = cv2.cvtColor(self.rotated_image, cv2.COLOR_BGR2GRAY)
        # threshold
        _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
        kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
        # dilate
        dilated = cv2.dilate(thresh, kernel, iterations=13)
        # get contours
        contours, hierarchy = cv2.findContours(
            dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        # for each contour found, draw a rectangle around it on original image
        for contour in contours:
            # get rectangle bounding contour
            [x, y, w, h] = cv2.boundingRect(contour)
            # discard areas that are too large
            if h > self.rotated_image.shape[0] and w > self.rotated_image.shape[1]:
                continue
            cv2.rectangle(self.rotated_image, (x, y),
                          (x+w, y+h), (0, 0, 255), 4)
        # write original image with added contours to disk
        return cv2.imwrite('contoured.jpg', self.rotated_image)

    # write and read all text with pytesseeract
    def write_text(self):
        with open(self.context_file, "w") as f:

            text = pytesseract.image_to_string("k.png")

            f.write(text)

    def read_text(self):
        # read each line
        with open(self.context_file, "r") as f:
            content = f.readlines()
        i = 0
        while i < len(content):
            if not content[i].strip():
                del content[i]
            i += 1
        for line in range(len(content)):
            count_line = int(input("Enter line_number --> "))
            if count_line > len(content):
                print(f"Please enter num in range(1: {len(content)})")
            print(linecache.getline((self.context_file), count_line))


# path pytesseract
pytesseract.pytesseract.tesseract_cmd = r'D:\ProgramData\tesseract.exe'


if __name__ == "__main__":
    
    rot_i = ImageProcesing("k.png", "saved_data.txt")
    rot_i.write_text()
    rot_i.read_text()
    mark_i = ImageProcesing("path")
    mark_i.marked_img(rot_i.rotated_img())
