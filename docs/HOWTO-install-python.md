# Installing Python on the Raspberry Pi 

## Method 1: Download and Compile

If the Python version/package is available from the distribution's repository, you can install it with `apt-get`.
Otherwise, you will have to compile it-- but that's reasonably easy, although compilation can take awhile.

```
# Download the relevant Python version
wget https://www.python.org/ftp/python/3.6.1/Python-3.6.1.tgz
# Extract the archive
tar xzvf Python-3.6.0.tgz
cd Python-3.6.0/
# Use configuration utility
./configure
# Make, and make install
make
sudo make install
```

Slightly more effort may be required if you're trying to install that version of Python in a specific location, or for a specific user.

## Method 2: Berryconda

Some guy combining qualities of both geniuses and saints has taken it upon himself to keep the `conda` package manager up-to-date for Raspbian.

It's available here: https://github.com/jjhelmus/berryconda

Installing is presumably similar to regular conda, e.g., 

```
wget https://github.com/jjhelmus/berryconda/releases/download/v1.0.0/Berryconda3-1.0.0-Linux-armv7l.sh
bash Berryconda3-1.0.0-Linux-armv7l.sh
# ... do installation stuf ...
conda create -n <new_env_name> python=3.X pip
# install things from the rpi channel if possible, or else use pip
```
