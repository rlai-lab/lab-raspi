"""
Demonstrating the use of the `video_threading.py` script.
"""
import time
import numpy as np
from video_threading import CameraStream


def detect_change(cs):
    prev = cs.frame
    toc = time.time()
    
    while True:
        cur = cs.frame
        tic = time.time()
        if np.any(prev != cur):
            print('Change occured! Interval:', tic - toc)
            print('Pixel difference:', np.sum(prev != cur))
            prev = cur
        toc = tic
        time.sleep(0.00001)
        


if __name__ == "__main__":
    thread = CameraStream()
    try:
        thread.start()
        detect_change(thread)
    except KeyboardInterrupt as e:
        print("Halting stream...")
        thread.halt.set()
    finally:
        print("Exiting...")