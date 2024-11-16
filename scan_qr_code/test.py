import cv2
import imutils
import numpy as np
import pytesseract

# Конфигурация за пътя на Tesseract OCR (провери пътя, ако е различен при теб)
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\YovoB\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Четене и предварителна обработка на изображението
img = cv2.imread('fiat.jpg', cv2.IMREAD_COLOR)
if img is None:
    raise IOError("Image not found or path is incorrect.")

img = cv2.resize(img, (488, 480))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 13, 15, 15)  # Намаляване на шум
edged = cv2.Canny(gray, 38, 280)  # Ръбове с Canny детектор

# Намерени контури
contours = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:18]  # Най-големите контури

# Откриване на контур с четири точки (вероятен номер на кола)
screenCnt = None
for c in contours:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.018 * peri, True)
    if len(approx) == 4:
        screenCnt = approx
        break

# Проверка дали е намерен контурът на номера
if screenCnt is None:
    print("No contour detected")
else:
    cv2.drawContours(img, [screenCnt], -1, (0, 255, 0), 3)

    # Изрязване на номера от изображението
    mask = np.zeros(gray.shape, np.uint8)
    cv2.drawContours(mask, [screenCnt], 0, 255, -1)
    masked_image = cv2.bitwise_and(img, img, mask=mask)

    # Определяне на координатите на изрязания номер
    x, y = np.where(mask == 255)
    topx, topy = np.min(x), np.min(y)
    bottomx, bottomy = np.max(x), np.max(y)
    Cropped = gray[topx:bottomx + 1, topy:bottomy + 1]

    # OCR конфигурация за четене на регистрационен номер
    text = pytesseract.image_to_string(Cropped, config='--psm 9')
    print("Detected License plate Number is:", text)

    # Промяна на размера за визуализация
    img_resized = cv2.resize(img, (508, 308))
    Cropped_resized = cv2.resize(Cropped, (468, 208))

    # Показване на изображенията
    cv2.imshow('Car', img_resized)
    cv2.imshow('Cropped License Plate', Cropped_resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
