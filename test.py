import urllib.request
import time
for i in range(12):
    stri = str(i)
    print("test")
    fname = "feed"+stri+".jpg"
    f = urllib.request.urlretrieve("http://10.1.10.147:8000/stream.mjpg", fname)
    print("test")

