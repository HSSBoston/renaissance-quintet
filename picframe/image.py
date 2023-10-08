import epd5in65f, time
from PIL import Image

try:
    display = epd5in65f.EPD()
    display.init()
    print("E-paper initialized (blackened). Now clearing.")
    display.Clear()
    print("E-paper cleared (whitened).")

    imageFileName = "space.jpg"
    image = Image.open(imageFileName)
    display.display(display.getbuffer(image))
    print(imageFileName + " displayed.")
    
    time.sleep(5)
    print("Done with displaying " + imageFileName + ". Now clearing.")
    display.Clear()
    print("E-paper cleared (whitened). Turning off.")
    display.sleep()
    
except IOError as e:
    print(e)

