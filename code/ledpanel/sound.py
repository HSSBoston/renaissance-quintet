import subprocess, os
import kintone, time
from datetime import datetime

sdomain = ""
appId = ""
token = ""

def  turnOnMusic():
    command1 = "vlc -I dummy nasa.mp3 --start-time=0 --stop-time=5 --play-and-exit"
    subprocess.run(command1, shell=True)

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
            turnOnMusic()

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
            turnOnMusic()

        time.sleep(60)
    except KeyboardInterrupt:
        break

