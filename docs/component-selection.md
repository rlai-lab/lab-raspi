

# SD Card

The Raspberry Pi's filesystem lives on the SD card; in a number of situations you may experience a bottleneck/lag whenever performing I/O is necessary, so you will want a fast SD card.

[See the SD association's documentation for details](https://www.sdcard.org/developers/overview/speed_class/)

This usually means a card with a "speed class" of 10 or, even better, an "ultra high speed class" of 1 or 3. 
UHS 3 is, as of this writing, the fastest available.

# USB WiFi 

You will almost certainly want a USB Wi-Fi adapter, because having to hook up to ethernet all the time is tedious.
However, this is a bit of a minefield, because some of the adapters don't have the right firmware, or the firmware is subtly broken, or the firmware is available but you will have to compile it yourself.

[The eLinux wiki has a good list of all of the adapters people have tried with the Raspberry Pi](http://elinux.org/RPi_USB_Wi-Fi_Adapters)

# Powered USB Hub

While not strictly necessary (I've been able to run a webcam, wifi, and a couple of other peripherals straight off of the Raspberry Pi's built-in USB ports), it's probably a good idea because of the Pi's tendency to become unstable if you draw too much power.