"""A quick way to check some of the Pi's built in sensors."""
import subprocess

def main():
    # Check CPU usage, most used processes...
    p = subprocess.Popen('top -bn 1|head -12', 
                         shell=True, 
                         stdout=subprocess.PIPE, 
                         stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
        print(line)
    retval = p.wait()
    print(retval)
    p = subprocess.Popen('/opt/vc/bin/vcgencmd measure_temp', 
                         shell=True, 
                         stdout=subprocess.PIPE, 
                         stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
        print(line)
    retval = p.wait()
    print(retval)
    p = subprocess.Popen('/opt/vc/bin/vcgencmd measure_volts', 
                         shell=True, 
                         stdout=subprocess.PIPE, 
                         stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
        print(line)
    retval = p.wait()
    print(retval)
