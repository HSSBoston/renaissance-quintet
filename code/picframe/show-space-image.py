import time, sys
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image, ImageDraw, ImageFont

options = RGBMatrixOptions()
options.cols = 64
options.rows = 64
options.parallel = 1
options.gpio_slowdown = 3
options.drop_privileges=False

imageFileName = "m51-composite.jpg"

ledPanel = RGBMatrix(options = options)

image = Image.open(imageFileName)
image.thumbnail((ledPanel.width, ledPanel.height), Image.ANTIALIAS)
ledPanel.SetImage(image.convert("RGB"))

while True:
    try:
        time.sleep(100)
    except KeyboardInterrupt:
        break

