# Setup

Setting up the PiCamera module is described in `lab-raspi/docs/HOWTO-camera-module.md`

# PiCamera Demos

There are some examples in this directory demonstrating how to access and use the camera module from Python, using the `picamera` package.

# Video4Linux

First, we have to activate the kernel module, `bcm2835-v4l2`, to allow v4l2 to control the PiCamera module. 
You can either do that by editing `/etc/modules` and rebooting, or load it from a shell by running 

```bash
sudo modprobe bcm2835-v4l2
```

## Listing Information

```bash
v4l2-ctl --list-formats

# More detail
v4l2-ctl --list-formats-ext

# For a specific device, here `/dev/video1`
v4l2-ctl -d /dev/video1 --list-formats
```

## Checking Framerate

I have managed to apparently confirm that the PiCamera module (even V1!) is capable of capturing at 90 frames per second (FPS).

```bash
# Set the frame rate
v4l2-ctl --set-parm 90

# Test the framerate
v4l2-ctl -d /dev/video1 --set-fmt-video=width=640,height=480,pixelformat=YUYV  --stream-mmap --stream-count=1000

# Alternatively, without messing around too much with the options
v4l2-ctl -d /dev/video1 --set-parm=90
v4l2-ctl -d /dev/video1 --stream-mmap --stream-count=1000
```

## OpenCV

Apparently, it's possible to control the PiCamera module from OpenCV once the kernel module is loaded, but I have not confirmed this.

# References