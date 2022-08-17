import pytesseract
from PIL import ImageGrab
from time import sleep
import cv2

pytesseract.pytesseract.tesseract_cmd = r"F:\Tesseract\tesseract.exe"

def get_deck_1():
    img = ImageGrab.grab(bbox=(813, 60, 880, 89))
    img.save("test.png")

    img = cv2.imread('test.png', cv2.IMREAD_GRAYSCALE)  

    thresh = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)[1]
    thresh = cv2.resize(thresh, (0,0), fx=0.9, fy=0.9)  # scale image 0.9X

    detected_text = pytesseract.image_to_string(thresh, config = '--psm 6')
    return parse(detected_text)


def parse(num: str) -> float:
    num = num.replace(" ", "").replace("\n", "")
    if len(num) == 4:
        num = num[:3] + "." + num[-1]
    try:
        num = float(num)
    except ValueError:
        pass
    return num



if __name__ == "__main__":
    while True:
        print(get_deck_1())
    #     num = get_deck_1()
    #     print(num)
    #     num = parse(num)
    #     print(num)
    #     sleep(0.3)
