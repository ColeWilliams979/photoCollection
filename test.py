import cv2
import urllib.request
import numpy as np

'''
for i in range(12):
    stri = str(i)

    fname = "feed"+stri+".jpg"
    while True:
    bytes += stream.read(1024)
    a = bytes.find(b'\xff\xd8')
    b = bytes.find(b'\xff\xd9')
    print("test")
    if a != -1 and b != -1:
        jpg = bytes[a:b+2]
        print("test1")
        bytes = bytes[b+2:]
        i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
        print("test1")
        with open('out.jpg', 'wb') as f:
            f.write(jpg)
        print("test1")
        if cv2.waitKey(1) == 27:
            exit(0)
'''

stream = urllib.request.urlopen('http://10.1.10.147:8000/stream.mjpg')
bytes = b''  # MAKE IT BYTES
x = 0
while True:
    while x != 12:
        bytes += stream.read(1024)
        a = bytes.find(b'\xff\xd8')
        b = bytes.find(b'\xff\xd9')
        print("test")
        if a != -1 and b != -1:
            jpg = bytes[a:b + 2]
            print("test1")
            bytes = bytes[b + 2:]
            i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
            print("test1")
            with open('out.jpg', 'wb') as f:
                f.write(jpg)
            print("test1")
            x += 1
            if cv2.waitKey(1) == 27:
                exit(0)

