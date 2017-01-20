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
import cv2 
import numpy as np 


class WebcamStream(threading.Thread):
    """A simple Thread subclass for using a USB webcam."""
    def __init__(self, source=0, res=(640, 480), fps=30, **kwargs):
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
                self._frame = frame 
            
        except Exception as e:
            print(e)
            raise(e)

        finally:
            camera.release()
            cv2.destroyAllWindows()
            return
    
    @property 
    def frame(self):
        """The most recent frame from the camera."""
        return self._frame



if __name__ == "__main__":
    t = WebcamStream()
    t.start()

    try:
        prev = t.frame  
        toc = time.time()
        while True:
            cur = t.frame  
            tic = time.time()
            if not (prev is cur):
                print('Approximate FPS:', 1/(tic - toc))
                toc = tic
                prev = cur 
            else:
                time.sleep(1e-6)
    
    except KeyboardInterrupt as e:
        t.halt.set()

    finally:
        t.join()

