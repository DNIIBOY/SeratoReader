import pytesseract
from PIL import ImageGrab
from time import sleep
import cv2

pytesseract.pytesseract.tesseract_cmd = r"F:\Tesseract\tesseract.exe"

def get_deck_1():
    img = ImageGrab.grab(bbox=(813, 60, 880, 89))
    return pytesseract.image_to_string(img, config="--psm 6")


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
        num = get_deck_1()
        print(num)
        num = parse(num)
        print(num)
        sleep(0.3)
