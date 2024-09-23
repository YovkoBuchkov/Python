import cv2
import imutils
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\YovoB\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

img = cv2.imread('fiat.jpg', cv2.IMREAD_COLOR)
img = cv2.resize(img, (488, 480))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 13, 15, 15)
edged = cv2.Canny(gray, 38, 280)

contours = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:18]

screenCnt = None
for c in contours:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.018 * peri, True)
    if len(approx) == 4:
        screenCnt = approx
        break

if screenCnt is None:
    detected = 0
    print("No contour detected")
else:
    detected = 1

if detected == 1:
    cv2.drawContours(img, [screenCnt], -1, (0, 255, 0), 3)

mask = np.zeros(gray.shape, np.uint8)
new_image = cv2.drawContours(mask, [screenCnt], 0, 255, -1)
new_image = cv2.bitwise_and(img, img, mask=mask)

(x, y) = np.where(mask == 255)
(topx, topy) = (np.min(x), np.min(y))
(bottomx, bottomy) = (np.max(x), np.max(y))
Cropped = gray[topx:bottomx + 1, topy:bottomy + 1]

#config --psm 9 read bg numbers / --psm 11 - english
# --oem 3: Автоматичен избор на OCR двигател.
# --psm 6: Третира изображението като единен блок от текст.
text = pytesseract.image_to_string(Cropped, config='--psm 9')
print("Detected License plate Number is:", text)

img = cv2.resize(img, (508, 308))
Cropped = cv2.resize(Cropped, (468, 208))
cv2.imshow('car', img)
cv2.imshow('Cropped', Cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
