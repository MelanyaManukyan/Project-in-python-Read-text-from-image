import pytesseract
import cv2
import numpy as np
import matplotlib.pyplot as plt

pytesseract.pytesseract.tesseract_cmd = r'D:\ProgramData\tesseract.exe'

#  contur arecinq amboxj nkary u texty lriv kardacinq
image = cv2.imread('k.png')
print(image.shape)

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

# discard areas that are too small
    # if h<40 or w<40:
    #     continue

# draw rectangle around contour on original image
cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 4)
print(image)
# arajin toxy nerkec
# image[17:23 , 17:263] = np.array([0,0,255])

# image[1]= np.array([0,0,255])

print(image)
# write original image with added contours to disk
cv2.imwrite('contoured.jpg', image)




#show imnage
plt.imshow(image)
plt.show()

#read all text with pytesseeract
text = pytesseract.image_to_string("k.png")
print(text)

with open("text_by_photo.txt", "w") as f:
    f.write(text)

with open("text_by_photo.txt", "r") as f:
    text_1= f.readline()
    print(text_1)

text_1.shape