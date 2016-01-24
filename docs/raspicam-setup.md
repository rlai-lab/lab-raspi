
## Minibian 

If you don't have `raspi-config` for whatever reason, then you can duplicate what it does by examining the actual Bash script.
I haven't got this working yet, and haven't been able to diagnose the problem.
When I set the GPU memory to 128, it seemed to have issues connecting to the Internet on rebooting, and even then didn't recognize the RaspiCam.
This may be because my camera module is faulty, or the board is not getting enough power with the additional load from the camera.
Everything seemed to work again after I reset the GPU memory split, however, so it looks like this might have something more to do with the GPU memory, or at perhaps Minibian is missing something that the OS expects to find for certain values of GPU memory.

```bash
# $1 is 0 to disable camera, 1 to enable it
set_camera() {
  # Stop if /boot is not a mountpoint
  if ! mountpoint -q /boot; then
    return 1
  fi

  [ -e /boot/config.txt ] || touch /boot/config.txt

  if [ "$1" -eq 0 ]; then # disable camera
    set_config_var start_x 0 /boot/config.txt
    sed /boot/config.txt -i -e "s/^startx/#startx/"
    sed /boot/config.txt -i -e "s/^start_file/#start_file/"
    sed /boot/config.txt -i -e "s/^fixup_file/#fixup_file/"
  else # enable camera
    set_config_var start_x 1 /boot/config.txt
    CUR_GPU_MEM=$(get_config_var gpu_mem /boot/config.txt)
    if [ -z "$CUR_GPU_MEM" ] || [ "$CUR_GPU_MEM" -lt 128 ]; then
      set_config_var gpu_mem 128 /boot/config.txt
    fi
    sed /boot/config.txt -i -e "s/^startx/#startx/"
    sed /boot/config.txt -i -e "s/^fixup_file/#fixup_file/"
  fi
}
```