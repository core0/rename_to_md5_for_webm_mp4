import os, sys
import hashlib
import datetime

#ext = [".jpg",".png",".JPG",".JPEG",".PNG",".GIF",".gif"]
ext = [".webm",".WEBM",".mp4",".MP4"]

currentDT = datetime.datetime.now()
print (str(currentDT))


for p,fl,fls in os.walk(os.curdir):
    for i in fls:
        for j in ext:
            if i.endswith(j):
                nw_f =  hashlib.md5(open(i,"rb").read()).hexdigest()+j
                try:
                    os.rename(i,nw_f)
                except WindowsError:
                    os.remove(i)
                break
    break

currentDT = datetime.datetime.now()
print (str(currentDT))