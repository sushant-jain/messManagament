import urllib.request
import json
import calendar
from datetime import time,datetime, timedelta

def utc_to_local(utc_dt):
    timestamp=calendar.timegm(utc_dt.timetuple())
    local_dt=datetime.fromtimestamp(timestamp)
    assert utc_dt.resolution>= timedelta(microseconds=1)
    return local_dt.replace(microsecond=utc_dt.microsecond)

def auth(uid):
    string = "http://ediome.com:3001/rfid"
    mystring=""
    meal=""
    for digit in uid :
        mystring +=str(digit)
    print(uid)
    print(" sj_uid "+mystring)
    if(mystring==""):
            return 0,"","";
    string = string + "/check-mess?uid=" + str(mystring)
    print("sj"+string)
    content = urllib.request.urlopen(string).read()
    print(uid)
    content = str(content,'utf-8')
    print(uid)
    content = json.loads(content)
    # print(content["success"])
    if(content["success"]):
        status = 1
        last=content["lastDate"]
        last = datetime.strptime(last, "%Y-%m-%dT%H:%M:%S.%fZ")
        last=utc_to_local(last)
        now=datetime.now()
        nowT=now.time()

        string2 = "http://ediome.com:3001/rfid/mess-data?uid="+mystring+"&type="
        if(nowT>time(8) and nowT<time(10)):
            if(last.date()<now.date() or last.time()<time(8)):
                meal="Breakfast"
                urllib.request.urlopen(string2+"1")
            else:
                status=-1
        elif(nowT>time(13) and nowT<time(15)):
            if(last.date()<now.date() or last.time()<time(13)):
                meal="Lunch"
                urllib.request.urlopen(string2+"2")
            else:
                status=-1
        elif(nowT>time(17) and nowT<time(18)):
            if(last.date()<now.date() or last.time()<time(17)):
                meal="Snacks"
                urllib.request.urlopen(string2+"3")
            else:
                status=-1
        elif(nowT>time(20) and nowT<time(21)):
            if(last.date()<now.date() or last.time()<time(8)):
                meal="Dinner"
                urllib.request.urlopen(string2+"4")
            else:
                status=-1


    
    else:
        status = 0
    print(status)
    return status,mystring,meal



