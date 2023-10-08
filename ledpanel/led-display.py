import time, sys
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image
import kintone, time
from datetime import datetime

sdomain = ""
appId = ""
token = ""

def turnOnDisplay():
    print("Turning on the display...")
    
    options = RGBMatrixOptions()
    options.cols = 64
    options.rows = 64
    options.parallel = 1
    options.gpio_slowdown = 3
    options.drop_privileges=False

    gifFileName = "converted.gif"
    gif = Image.open(gifFileName)
    try:
        num_frames = gif.n_frames
        print("Finished reading a gif.")
    except Exception:
        sys.exit("provided image is not a gif")

    matrix = RGBMatrix(options = options)

    canvases = []
    print("Preprocessing gif...")
    for frame_index in range(0, num_frames):
        gif.seek(frame_index)
        frame = gif.copy()
        frame.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
        canvas = matrix.CreateFrameCanvas()
        canvas.SetImage(frame.convert("RGB"))
        canvases.append(canvas)
    gif.close()
    print("Completed Preprocessing. Displaying gif")

    try:
        print("Press Ctrl-C to stop.")

        # Infinitely loop through the gif
        cur_frame = 0
        while(True):
            matrix.SwapOnVSync(canvases[cur_frame], framerate_fraction=10)
            if cur_frame == num_frames - 1:
                cur_frame = 0
            else:
                cur_frame += 1
    except KeyboardInterrupt:
        sys.exit(0)
    
while True:
    try:
        record = kintone.getRecord(subDomain=sdomain,
                                   apiToken=token,
                                   appId=appId,
                                   recordId="1")
        onNow = record["on_now"]["value"]
        print(onNow)
        schedDaysList = record["schedule"]["value"]
        print(schedDaysList)
        schedTimeList = record["time"]["value"]
        print(schedTimeList)

        if "Yes" in onNow:
            print("Turn On Display On = Yes")
            turnOnDisplay()

        daysOfWeek = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        dt = datetime.now()
        dow = daysOfWeek[dt.weekday()]
        if dt.minute >= 10:
            min = str(dt.minute)
        else:
            min = "0" + str(dt.minute)
        currentTime = str(dt.hour) + ":" + min 
        if dow in schedDaysList and schedTimeList == currentTime:
            print("Current time: " + currentTime + ", " + dow)
            turnOnDisplay()

        time.sleep(60)
    except KeyboardInterrupt:
        break

