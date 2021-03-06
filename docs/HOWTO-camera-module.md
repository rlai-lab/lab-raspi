<!-- 
Author: BB 
Last revised: 2017/01/17 
-->

# Installation

[See the official docs](https://www.raspberrypi.org/documentation/usage/camera/python/README.md) if needed, as well as [this tutorial for some pictures](https://www.raspberrypi.org/learning/getting-started-with-picamera/worksheet/)

- Remove the camera from its packaging
- Prepare to connect the camera to the Pi
  + The camera has a ribbon cable that connects it to the Pi. 
  + The port on the Pi is the thin black plastic connector near the audio and HDMI connections
- Pull up on the black plastic outcropping to allow for the ribbon cable to fit.
- Insert the ribbon cable (with the exposed conductors facing towards the HDMI port)
- Push down on the black plastic tab to lock the cable into place.

## Checking the Hardware

Assuming you've connected the camera and it has been enabled from `raspi-config`, you can now test that it works.

If you've got a monitor attached to the Pi, you can use the following to get a full screen view of the camera's output:

```bash
raspivid -f
```

Alternatively, you take a snapshot with `raspistill`

```bash
raspistill -o test.png
```

After copying the file over to a computer with an attached monitor (e.g., via `scp`), you can verify that the camera is functioning correctly.

# Software

- Install `picamera`
  
  ```bash
  # in terminal
  pip install picamera
  ```

- (If you're working with the lab image) install `OpenCV 3`
  + This required a bit of effort to get it to compile correctly; if needed I can help with compiling it.
- Test that both were installed properly.
  + In a Python interpreter, try `import picamera` and `import cv2`

# References

- Setting up the Camera Module
  - https://www.raspberrypi.org/learning/getting-started-with-picamera/worksheet/
  - https://www.raspberrypi.org/documentation/usage/camera/python/README.md
  - https://www.raspberrypi.org/documentation/usage/camera/raspicam/raspivid.md
  - https://www.raspberrypi.org/documentation/usage/camera/raspicam/raspistill.md
  - http://elinux.org/Rpi_Camera_Module

- Using the camera module
  - http://picamera.readthedocs.io/en/release-1.10/index.html
  - http://picamera.readthedocs.io/en/release-1.11/recipes2.html

- Some posts for PyImageSearch on the camera module
  + http://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/
  + http://www.pyimagesearch.com/2015/12/28/increasing-raspberry-pi-fps-with-python-and-opencv/
  + http://www.pyimagesearch.com/2016/01/04/unifying-picamera-and-cv2-videocapture-into-a-single-class-with-opencv/
  + http://www.pyimagesearch.com/2016/01/18/multiple-cameras-with-the-raspberry-pi-and-opencv/