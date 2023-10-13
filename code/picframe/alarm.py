import kintone

sdomain = "SUB-DOMAIN-NAME"
appId = "APP-ID-NUMBER"
token = "APP-TOKEN"

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


