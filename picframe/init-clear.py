import epd5in65f

epd = epd5in65f.EPD()
epd.init()
epd.Clear()
epd.sleep()
print("Display cleared and powered off.")