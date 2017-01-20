"""
Using threading with the PiCamera.

Employing threads is necessary because otherwise reading from the camera's 
stream is a blocking process, but most of the time we want to run something 
else while the camera is waiting for a new frame.

Usage
-----

```
# Starting the camera
t = CameraStream()
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
from picamera import PiCamera
from picamera.array import PiRGBArray


class CameraStream(threading.Thread):
    """A simple Thread subclass for using the PiCamera module."""
    def __init__(self, res=(640, 480), fps=30, **kwargs):
        super().__init__(**kwargs)
        self.resolution = res
        self.framerate = fps

        # Frame private variable
        self._frame = None

        # Halt flag (when this is set, the loop in `run` stops)
        self.halt = threading.Event()

    def run(self):
        # Open the camera
        camera = PiCamera()
        # Set the options from initialization
        camera.resolution = self.resolution
        camera.framerate = self.framerate

        # Create storage for frames and set up stream
        raw = PiRGBArray(camera, size=self.resolution)
        stream = camera.capture_continuous(raw, 
            format='rgb',
            use_video_port=True)

        try:
            for f in stream:
                self._frame = f.array
                raw.truncate(0)

                if self.halt.is_set():
                    break
            
        except Exception as e:
            raise(e)

        finally:
            raw.close()
            stream.close()
            camera.close()
            return
    
    @property 
    def frame(self):
        """The most recent frame from the camera."""
        return self._frame