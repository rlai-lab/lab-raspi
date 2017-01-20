"""
Demonstrating the use of the `video_threading.py` script.

This time we make a simple motion detector using OpenCV.
It is very hacky, but it demonstrates the possibility of doing real-time
processing on frames from the PiCamera module.
(You may have to alter the thresholds/blur/difference calculation to get it to
work depending on your local environment.)
"""
import time
import numpy as np
import cv2
from video_threading import CameraStream


def detect_motion(a, b, threshold=0.15):
    """Return True if more than some fraction of the images differ."""
    a = cv2.GaussianBlur(a, (15, 15), 0)
    b = cv2.GaussianBlur(b, (15, 15), 0)
    pixels = np.prod(a.shape)
    #diff = np.sum(a != b)
    diff = np.sum(np.abs(a - b) > 4)
    return (diff/pixels > threshold)

def detection_loop(cs):
    """A loop that detects when motion occurs, and prints a message."""
    # Wait for camera to start up
    prev = cs.frame
    while prev is None:
        prev = cs.frame
    
    # Convert to grayscale
    prev = cv2.cvtColor(prev, cv2.COLOR_RGB2GRAY)
    toc = time.time()

    while True:
        cur = cs.frame
        cur = cv2.cvtColor(cur, cv2.COLOR_RGB2GRAY)
        tic = time.time()
        if detect_motion(prev, cur):
            print("Motion detected! Interval:", tic - toc)
        else:
            time.sleep(1e-6)
        prev = cur
        toc = tic
        


if __name__ == "__main__":
    thread = CameraStream()
    try:
        thread.start()
        detection_loop(thread)
    except KeyboardInterrupt as e:
        print("Halting stream...")
        thread.halt.set()
    finally:
        if not thread.halt.is_set(): thread.halt.set()
        
        # Join thread and exit
        thread.join()
        print("Exiting...")