import pytesseract
import cv2
import matplotlib.pyplot as plt
import numpy as np
import linecache

# path pytesseract
pytesseract.pytesseract.tesseract_cmd = r'D:\ProgramData\tesseract.exe'


def contours_img(image):
    # grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

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
        if h > image.shape[0] and w > image.shape[1]:
            continue

    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 4)
    # write original image with added contours to disk
    return cv2.imwrite('contoured.jpg', image)

    # print(contours_img(cv2.imread("b.png")))


def show_image(image):
    # show image

    plt.imshow(image)
    plt.show()


print(show_image(cv2.imread("k.png")))


# read all text with pytesseeract
# txt path
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
