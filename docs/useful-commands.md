
# Raspberry Pi 

Firmware/Kernel Related

```
# list the Raspberry Pi's firmware version
/opt/vc/bin/vcgencmd version

# kernel name and release
uname -sr

# kernel version
uname -v

# Linux distribution
cat /etc/*-release
lsb_release -a
```

## Updating Firmware via a `rpi-update`

Might be good to check to make sure that this is trustworthy/uncompromised.

```
# install tools to upgrade Raspberry Pi's firmware
sudo wget https://raw.github.com/Hexxeh/rpi-update/master/rpi-update -O /usr/bin/rpi-update
sudo chmod +x /usr/bin/rpi-update
```

## Manually set configuration variables (be careful!)

You can edit them directly in the `/boot/config.txt` file; the options are laid out fairly straightforwardly

```
# sudo nano /boot/config.txt
gpu_mem=16
```

## Determine bus speed available for USB devices.

This is important because if you have too many peripherals competing for bandwidth, you can get weird failures that are difficult to diagnose.
For example, more than one webcam may fuck things up.

```
lsusb -t
```

## List the available video modes for a USB webcam.

```
v4l2-ctl --list-formats
# or alternatively,
v4l2-ctl --list-formats-ext
```

# General Linux

## Clean up Temporary Files

```
# Look at the candidates for deletion
find $HOME -type f -name "*~" -print

# Actually delete them
find $HOME -type f -name "*~" -print -exec rm {} \;
```

## Deleted But Open Files

```
# list open but deleted files
sudo lsof -nP | grep '(deleted)'

# total space used by open but deleted files
sudo lsof -nP | awk '/deleted/ { sum+=$8 } END { print sum }'

# process IDs of open but deleted files
sudo lsof -nP | grep '(deleted)' | awk '{ print $2 }' | sort | uniq
```

## Clean Up Old Kernel Packages

```
# Find out the current kernel
uname -r

# USE WITH CAUTION: perminately delete old kernel packages
sudo apt-get remove --purge $(dpkg -l 'linux-*' | sed '/^ii/!d;/'"$(uname -r | sed "s/\(.*\)-\([^0-9]\+\)/\1/")"'/d;s/^[^ ]* [^ ]* \([^ ]*\).*/\1/;/[0-9]/!d')

# USE WITH CAUTION: to remove a specific kernel package, in this case 3.13.0-49
sudo apt-get remove --purge $(dpkg -l 'linux-*' | sed '/^ii/!d;/'"$(uname -r | sed "s/\(.*\)-\([^0-9]\+\)/\1/")"'/d;s/^[^ ]* [^ ]* \([^ ]*\).*/\1/;/[0-9]/!d' | grep 3.13.0-49)
```

# Sources

http://jeffskinnerbox.me/posts/2014/Mar/31/howto-linux-maintenance-and-filesystem-hygiene/