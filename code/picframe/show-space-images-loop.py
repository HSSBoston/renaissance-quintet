import time, sys
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image, ImageDraw, ImageFont

options = RGBMatrixOptions()
options.cols = 64
options.rows = 64
options.parallel = 1
options.gpio_slowdown = 3
options.drop_privileges=False

imageFileNames = ["m51-xray.jpg",
                  "m51-optical.jpg",
                  "m51-ir.jpg",
                  "m51-uv.jpg",
                  "m51-composite.jpg"]

ledPanel = RGBMatrix(options = options)

while True:
    try:
        for i in range(len(imageFileNames)):            
            image = Image.open(imageFileNames[i])
            image.thumbnail((ledPanel.width, ledPanel.height), Image.ANTIALIAS)
            ledPanel.SetImage(image.convert("RGB"))
            time.sleep(3)
    except KeyboardInterrupt:
        break
