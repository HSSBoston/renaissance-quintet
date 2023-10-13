import kintone, time
from datetime import datetime

# sdomain = "SUB-DOMAIN-NAME"
# appId = "APP-ID-NUMBER"
# token = "APP-TOKEN"

def turnOnDisplay():
    print("Turning on the display...")
    
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

