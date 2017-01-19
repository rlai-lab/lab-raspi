# Lab Image

We have an image pre-built for the Raspberry Pi loaded with the required software and configured for the RLAI lab.

It should be available locally (e.g., on the Lab's Mac, Elmer); if not I have a copy and can produce more images as needed.

```
Image Name:
2016-05-21-rlai-raspbian.img

SHA sum (check with `shasum -a 256 -b 2016-05-21-rlai-raspbian.img`)
0ba118c5aa568640b6b19dac455a0f71859e38ed16883c086aad033949d70049
```

## Why a Custom Image?

The default Raspberry Pi OS (Raspbian) is good but it requires some customization for the lab.
Performing this customization and then preserving it in a custom image saves some time, if you ignore the hour or two it took me to figure out how to make disk images (it was not fun).
It also guarantees that we are working from a common baseline if we all use the same image, which makes our work easier to replicate or recover.

In particular, the image has:

- Some customization to ensure that it connects to the `critterbot` network and is accessible over SSH.
- Continuum's `miniconda`, a Python package manager that works well with the Raspberry Pi
- OpenCV3, a computer vision library (somewhat difficult to compile with Python 3 support)
- Miscellaneous useful packages (`avahi-daemon`, `git`, `htop`, ...)
- Code for interfacing with the iRobot Create (`pyserial`, and my own `cspy3` library)
- Software that was needed to install the above.

# Installing Image to an SD Card

1. Required materials:
    - A OSX or Linux computer with the `dd` utility and an SD card reader
        + These instructions were written and tested with a MacBook Pro in mind; using Linux to create the SD card requires minor changes (see references)
    - An SD card (ideally of with capacity > 8GB)
    - A monitor with an HDMI input
    - A Raspberry Pi (these instructions written for a Raspberry Pi 3)
    - A keyboard
2. Insert the SD card into your computer 
3. Format the SD card to `FAT32` (using disk utility or the command line; see references)
4. Unmount the partition on the SD card
5. Make a note of the disk used:
    - Either take not of it in disk utility or run `diskutil list` in terminal (or the equivalent command on Linux)
    - It should be something like `/dev/disk + a number`, e.g., `/dev/disk9` 
6. Copy the disk image onto the SD card by executing the following command in a terminal:

    ```
    sudo dd bs=1m if=/path/to/raspbian-image.img of=/dev/rdiskN
    ```

    - Note that we are using `/dev/rdisk` instead of `/dev/disk` because it's faster on OSX.
    - Replace `/path/to/raspbian-image.img` with the path to `2016-05-21-rlai-raspbian.img`

    If successful, you should get a message like 

    ```
    2367+0 records in
    2367+0 records out
    2481979392 bytes transferred in 35.437846 secs (70037535 bytes/sec)
    ```
7. Eject the disk; your SD card is ready


# Post Installation

After you've written the image to the SD card, there are some things that are only possible on the Pi itself that have to be done to finish the setup.

1. Insert the SD card into the Pi
2. Attach peripherals (e.g., keyboard & HDMI cable, unless you're configuring things over the network via `ssh`)
3. Connect the Pi to power

At this point the Pi should boot up, and if you've connected it to a monitor, it should drop you into a command prompt shortly.

## Necessary

These actions are necessary in order to get the Pi working properly.

1. Change hostname
    - The default hostname for this image should be `changeme`, which should provide something of a hint. It needs to be altered because it's likely that multiple Pis will be running on the network, and conflicting hostnames can cause problems.
    - On the Pi, run `sudo raspi-config` to open up the Raspberry Pi's built-in configuration wizard.
    - Navigate to `Advanced Options` using keyboard and select it
    - Select the option `Hostname`
    - Enter your desired hostname
2. Expand memory
    - By default, the Raspberry Pi's image doesn't provide access to the entire SD card as usable memory, in order to accomodate different SD card capacities. Once the image has been written to the card, however, this should be changed.
    - On the Pi, run `sudo raspi-config`
    - Select the option `Expand Filesystem`
    - Reboot

## Optional

- Enable Camera
    - It may be necessary to enable support for the RaspiCam if you intend on using one.
    - On the Pi, run `sudo raspi-config`
    - Select `Interfacing Options`
    - Select `Camera`
    - Select `Enable`
- Modify memory split
    - The Raspberry Pi allocates its RAM between the CPU and the GPU; depending on what you're using it for it may be desirable to allocate different amounts of memory than the image's default. 
    - On the Pi, run `sudo raspi-config`
    - Navigate to `Advanced Options` using the keyboard and select it
    - Navigate to `Memory Split`
    - Set it to your desired value (in powers of two, ideally)

- Disable waiting for network at boot
    - By default, the Raspberry Pi may wait during its bootup process until it connects to a network (either WiFi or Ethernet). This is not always desirable, especially if you don't expect a network to be constantly available.
    - On the Pi, run `sudo raspi-config`
    - Navigate to `Boot Options` and select it
    - Navigate to the option `Wait for Network at Boot` and select it
    - Select `Disable`

- Add SSH keys
    + To avoid the password prompt when connecting to the Pi over `ssh`, you can add your computer's SSH key to the `authorized_keys` file.
    + On your personal computer (assuming the Pi is connected to the same network as you), the command for this is
    
        ```bash
        cat /path/to/your/ssh_key.pub | ssh pi@CHANGEME.local "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
        ```

        Where, once again, you should alter `CHANGEME` in the above to the Pi's hostname, and adjust your `/path/to/your/ssh_key.pub` to the reflect the path to your public key.

    + See the references for more explanation if needed.

- Update & Upgrade software
    + The image has not been modified since it was created, and so the software on the Pi may be out of date.
    + If you find it necessary, you can update and upgrade the installed software packages via:
        
        ```bash
        sudo apt-get update && sudo apt-get upgrade -y
        ```

- Adjust wireless settings
    + If you're connecting to a different wireless network than the Lab's `critterbot`, it's necessary to modify some settings to get things to work.
    + See the references for how to do this.

## Shutdown

Please shut down the Pi before removing power. Abruptly disconnecting the power supply can cause errors on the disk.

The command for shutting down the Pi is:

```
sudo halt -p
```


# References

- https://www.raspberrypi.org/documentation/installation/installing-images/mac.md
- https://www.raspberrypi.org/documentation/installation/installing-images/linux.md
- https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md
- http://askubuntu.com/questions/46424/adding-ssh-keys-to-authorized-keys