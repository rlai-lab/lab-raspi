"""
Using threading with a USB Webcam and OpenCV.

Employing threads is necessary because otherwise reading from the camera's 
stream is a blocking process, but most of the time we want to run something 
else while the camera is waiting for a new frame.

Requires OpenCV 3.1.0 and numpy.

Usage
-----

```
# Starting the camera
t = WebcamStream()
t.start()

# Getting the most recent frame (note the camera takes a moment to warm up)
f = t.frame()

# Stopping the stream via its halt event (which releases the camera)
t.halt.set()

# Join the thread 
t.join()
```
"""
import threading
import time
import numpy as np 


class WebcamStream(threading.Thread):
    """A simple Thread subclass for using a USB webcam."""
    def __init__(self, source=0, res=(320, 240), fps=30, **kwargs):
        super().__init__(**kwargs)
        self.source = source
        self.resolution = res
        self.framerate = fps

        # Frame
        self._frame = None

        # Halt flag
        self.halt = threading.Event()

    def run(self):
        camera = cv2.VideoCapture(self.source)
        width, height = self.resolution
        camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        camera.set(cv2.CAP_PROP_FPS, self.framerate)

        try:
            while not self.halt.is_set():
                ret, frame = camera.read()
                self._frame = frame # TODO: Check if this needs to be copied
                raw.truncate(0)

            
        except Exception as e:
            raise(e)

        finally:
            camera.release()
            cv2.destroyAllWindows()
            return
    
    @property 
    def frame(self):
        """The most recent frame from the camera."""
        return self._frame