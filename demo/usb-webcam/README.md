# Using a USB Webcam with the Raspberry Pi

The Raspberry Pi is capable of reading video from a USB webcam.

Webcams seem to have higher latency and more expensive processing compared to using the PiCamera module, although it depends on the webcam used.
The larger differences come from the fact that the interface to the various webcams is somewhat more involved, since most webcams are not manufactured with the single-board Linux market in mind.
Also, they tend to have a lower maximum FPS than the PiCamera, because high speed video is not really something the average webcam user requires.

All told, it's generally easiest to access the webcam through something like OpenCV.
As a bonus, OpenCV3 is Python compatible, and pre-compiled and installed on the RLAI Raspbian Images.


# Related

Get a list of video formats supported

```bash
v4l2-ctl --list-formats

# More detail
v4l2-ctl --list-formats-ext

# For a specific device, here `/dev/video0`
v4l2-ctl -d /dev/video0 --list-formats
```

# References

- USB Webcams for the Raspberry Pi
    + http://elinux.org/RPi_USB_Webcams
    + https://www.raspberrypi.org/documentation/usage/webcams/

- OpenCV
    + http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html
    + http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
    + http://stackoverflow.com/questions/32468371/video-capture-propid-parameters-in-opencv
- Miscellaneous
    + http://videos.cctvcamerapros.com/raspberry-pi/ip-camera-raspberry-pi-youtube-live-video-streaming-server.html