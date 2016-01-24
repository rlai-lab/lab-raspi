The minibian project seems like a nice idea, because it's a stripped down version of the Raspbian OS, which is notoriously bloated.
Installing it is reasonably easy, and configuring it is not particularly difficult, either.

# Get the Image

[Find the current image from the site](https://minibianpi.wordpress.com)

Download it, and extract it.

## Resize the partition beforehand

Some people suggest resizing the partition using GParted to give things like `/boot` the user directories a little more space.
If you're making your own images from a Minibian base, this is probably a good idea.

# Install onto SD Card

If the card has been used before, you should probably delete the partitions and reformat the SD card as FAT32.

## Installing from command line (OS X)

Find out what device/disk the SD card is associated with, e.g. using `df -h` or `diskutil list`.

```
# Unmount the SD card's partitions
sudo diskutil unmount /dev/diskns2 # and all other partitions, too
# Copy the image to disk
sudo dd bs=1m if=/path/to/image-jessie-minibian.img of=/dev/rdiskN
# Eject 
sudo diskutil eject /dev/rdiskN
```

# Post-Installation Configuration

You will somehow need to get the Pi connected to the Internet, and ideally have a monitor + keyboard to interact with it.
If you have multiple Pis with identical hardware, you might want to save the image after you've configured it (but before you've resized the partition) in order to duplicate it across the other ones.

## Packages

```
# Install essential software
apt-get install bzip gcc g++ libncurses5-dev make nano sudo usbutils
# Install other useful software
apt-get install avahi-daemon git htop
```

### Installing Conda Package Manager

You could also install vanilla Python, but conda makes some things substantially easier.

[See the website for more details](https://www.continuum.io/content/conda-support-raspberry-pi-2-and-power8-le)

```bash
# Miniconda3 Linux armv7l (Python 3)
wget http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-armv7l.sh
bash Miniconda3-latest-Linux-armv7l.sh
```

Now you can run, e.g., `conda update` to get the newest version of the tool, and then commands like

```
conda install pip
conda install ipython
# Create some environments
conda create -n py34 python=3.4 numpy ipython
conda create -n py27 python=2.7 numpy ipython
```

## Setting up SSH 

It should be installed and available by default, but you can always check:

```
apt-get install openssh-server
service ssh restart
```

You can also futz with the configuration in `/etc/ssh/sshd_config`.

If you still can't connect, perhaps you need to install `avahi-daemon`

## Setting up Wi-Fi

Figure out which Wireless adapter(s) you need firmware for, and install that.

For example, use `lsusb` and a bit of Googling, or [try to look up the model](http://elinux.org/RPi_USB_Wi-Fi_Adapters)

### Installing and configuring wpasupplicant

Install `wpasupplicant` and wireless related packages

```
apt-get install wpasupplicant
apt-get install iw
apt-get install wireless-tools
```

Edit `/etc/network/interfaces`, e.g., adding the lines

```
allow-hotplug wlan0 
iface wlan0 inet manual 
wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf 

iface default inet dhcp
```

Edit `/etc/wpasupplicant/wpasupplicant.conf`, following the example of

```
# A minimal configuration
network={ ssid="yourssid" psk="yourpassword" }

# Network with no authentication
network={
ssid="__SSID__"
scan_ssid=0
key_mgmt=NONE
}

# Network with WPA/WPA2 authentication
network={
    ssid="__SSID__"
    proto=RSN
    key_mgmt=WPA-PSK
    pairwise=CCMP TKIP
    group=CCMP TKIP
    psk="__PASSWORD__"
}
```

### Wireless Card Firmware

If you have one of those cards that doesn't work out-of-the-box, well, you may be screwed.

#### Building Firmware From Source

But hopefully the drivers are available somewhere, e.g., for TP-Link cards, there's the repository:
https://github.com/lwfinger/rtl8188eu

...but you will need to have the kernel headers, which are not available like you'd expect in real linux. 
Remember, this is Raspberry Pi Land, where everything has to be difficult, except for things that noone wants to do, like run last decade's Minecraft or a lobotomized version of Mathematica.

At this point I would make a joke about U2 suing Wolfram for taking their gimmick of downloading unwanted crap onto people's computers without their consent, but the joke actually fails because Wolfram is far more litigious, especially with regards to ideas that he didn't come up with.

So, anyways, there's a Python script that apparently solves this problem, I haven't really read it so it could be setting up a North Korean botnet for all I know...

```
git clone https://github.com/notro/rpi-source.git
cd rpi-source
python rpi-source # note that it's Python 2.7
```

Speaking of last decade's software, this script wants Python 2.7, so make sure you've installed that, either from the repos or using conda.

#### rtl8188eu

For usb wifi cards with id: `0bda:8179`.

```
git clone https://github.com/lwfinger/rtl8188eu.git
cd rtl8188eu
make all
sudo make install
```

If it fails because there's no `/lib/firmware` directory, you'll have to create one; `mkdir -p /lib/firmware`

## Resizing Partitions

You can modify the partition table with `fdisk`, and it's actually waaaay less dangerous than you might think.

```
fdisk /dev/mmcblk0
```

Delete partitions with `d` and create new ones with `n`.
For this version of minibian, you have to delete partition 2 (the main partition) and then recreate it in a larger form, so:

```
p # see state of current partition
d, 2 # delete the main partition
n p 2 # create a new primary partition (start at the same place the old one started)
w # write the changes to disk
```

Now reboot. 

Then, you have to resize the file system on the partition; thankfully there's a command for this:

```
resize2fs /dev/mmcblk0p2
```

Check that everything worked properly with `df -h`.

# Miscellaneous

## Change Root Password

As the root user, you can just type:

```
passwd
```

## Change Hostname

1. Edit the hosts file via `sudo nano /etc/hosts`

The line beginning with `127.0.1.1` followed by your current hostname is the one you want to edit; replace the current hostname with the new one

```
127.0.1.1   old_hostname 
# replace the above with
127.0.1.1   new_hostname
```

2. Then open another file, `/etc/hostname` which will contain the old hostname as well; edit this and replace it with the new one (as you did in the `/etc/hosts`) file.

3. Finally, run the command 

```
/sudo/etc/init.d/hostname.sh
```

...and then reboot (`sudo reboot`)

## Create User Account

As root, it's simple:

```
adduser MY_NEW_USER # ...and then follow the options.
passwd MY_NEW_USER # set the user's password
groups MY_NEW_USER # see the groups the user is part of
adduser MY_NEW_USER [group] # add the user to a new group
```

The groups you may want to add are things like:

```
# For user `pi`, from the defaults of the Raspbian distribution
adduser pi audio
adduser pi dialout
adduser pi input
adduser pi netdev
adduser pi tty
adduser pi users
adduser pi video
```

[See here for more details](https://wiki.archlinux.org/index.php/users_and_groups)

You may want to give the new user the ability to execute commands via `sudo`.

```
sudo usermod -a -G sudo MY_NEW_USER
```

Alternatively, this can be done via `sudo visudo`, and modify the file so it looks like:

```
# User privilege specification
root  ALL=(ALL:ALL) ALL
MY_NEW_USER   ALL = NOPASSWD: ALL
```

Deleting a user can be done via `sudo userdel -r user_to_delete`

## Set up Passwordless SSH Authentication

## Disable SSH Logins as Root
