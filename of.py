
from PIL import Image
import pytesseract
import cv2
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
        if h > image.shape[0] or w > image.shape[1]:
            continue
        img_rectangle = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 4) #crop
        # Convert the image to grayscale
        gray_img_rectangle = cv2.cvtColor(img_rectangle, cv2.COLOR_BGR2GRAY)       # gray crop
    # write original image with added contours to disk
    cv2.imwrite('contoured.jpg', gray_img_rectangle)
    return gray_img_rectangle
image = cv2.imread("C:\\Users\\User\\PycharmProjects\\pythonImagetoText\\k.png")
img_with_contours = contours_img(image)
text = pytesseract.image_to_string(img_with_contours)
# write all text with pytesseract and if file does not exist, create file
with open("C:\\Users\\User\\PycharmProjects\\pythonImagetoText\\text_by_photo.txt", "w") as f:
    # Check if the text is horizontal or vertical
    horizontal = all(c.isalnum() or c.isspace() for c in text)
    if not horizontal:
        # Rotate the cropped image by 90 degrees counterclockwise
        crop_img = cv2.rotate(img_with_contours, cv2.ROTATE_90_COUNTERCLOCKWISE)
        text = pytesseract.image_to_string(Image.fromarray(crop_img), lang='eng')
        f.write(text)
    elif horizontal:
        text = pytesseract.image_to_string(Image.fromarray(img_with_contours), lang='eng')
        f.write(text)
    else:
        # Rotate the cropped image by 180 degrees counterclockwise
        crop_img = cv2.rotate(img_with_contours, cv2.ROTATE_180_COUNTERCLOCKWISE)
        text = pytesseract.image_to_string(Image.fromarray(crop_img), lang='eng')
        f.write(text)
with open("C:\\Users\\User\\PycharmProjects\\pythonImagetoText\\text_by_photo.txt", "r") as f:
    content = f.readlines()
for line in range(len(content)):
    count_line = input("Enter line_number --> ")
    try:
        count_line = int(count_line)
        if count_line < 1 or count_line > len(content):
            print(f"Please enter a number in the range 1 to {len(content)}")
        else:
            print(
                linecache.getline("C:\\Users\\User\\PycharmProjects\\pythonImagetoText\\text_by_photo.txt", count_line))
    except ValueError:
        print("Please enter a valid number")