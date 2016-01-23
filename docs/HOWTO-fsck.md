
# Why Would This Be Necessary?

Sometimes you will see troubling messages during startup, along the lines of 

```
[   10.843066] FAT-fs (mmcblk0p1): Volume was not properly unmounted. Some data may be corrupt. Please run fsck.
```

So clearly, running `fsck` (file system check) is something that your Raspberry Pi wants you to do.

However, the actual process of doing this is complicated by the fact that you might not be able to run it from the Pi itself, since the file system needs to be mounted for the Pi to be running.

# Running fsck on a different machine

A relatively easy solution is to remove the SD card, and mount it on a different computer that is running Linux.
It could even be another Raspberry Pi.

So, assuming it's somehow connected, determine where the SD card is mounted (e.g., using `df -h` or the graphical `Disks` utility on Ubuntu), then unmount the partitions you want to check.

```
df -h # figure out where the SD card is mounted
# Suppose the device is `/dev/sdx` and the partitions are `sdx1` and `sdx2`
umount /dev/sdx1 
umount /dev/sdx2
# now run fsck
fsck -C /dev/sdx1 # follow the instructions and make choices in the prompt
fsck -C /dev/sdx2
```

...and hopefully your Pi will be happy again.

# Running fsck on the Pi itself

Another tutorial suggests a way of doing this without having to involve a separate computer that is already running Linux, but others have cautioned against doing this. 
If you must, the process suggested was:

```
# Take the system down to runlevel one
init 1 
# then follow the same protocol as above
```

