"""
This script uses the `picamera` package to take a snapshot with the Raspberry 
Pi camera module.
"""
import time
from picamera.array import PiRGBArray
from picamera import PiCamera

# Initialize the camera
cam = PiCamera()
raw = PiRGBArray(cam)

# Allow camera to warm up
time.sleep(0.1)

# Capture an image from the camera
cam.capture(raw, format='rgb')
img = raw.array

