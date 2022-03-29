import webbrowser
import pyautogui
from PIL import ImageGrab
import time


def sleep(value):
    time.sleep(value)
    return


def openbrowser():
    webbrowser.open('https://elgoog.im/t-rex/')
    return


def hit(key):
    pyautogui.keyDown(key)
    return


def is_collide(data_value):
    for i in range(1800, 1950):
        for j in range(750, 825):
            print(data_value[i, j])
            if data_value[i, j] < 100:
                hit('up')
                return
    for i in range(1800, 1850):
        for j in range(700, 750):
            print(data_value[i, j])
            if data_value[i, j] < 171:
                hit('down')
                return
    return


# def paint(data_value):
#     for i in range(1700, 1950):
#         for j in range(750, 800):
#             data_value[i, j] = 0
#     for i in range(1800, 1850):
#         for j in range(700, 750):
#             data_value[i, j] = 171
#     return


if __name__ == "__main__":
    openbrowser()
    sleep(5)
    hit('up')
    while True:
        image = ImageGrab.grab().convert('L')
        image_data = image.load()
        is_collide(image_data)
    # paint(image_data)
    # image.show()