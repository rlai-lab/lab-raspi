# Installing Python on the Raspberry Pi 

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
