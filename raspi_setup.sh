# Don't actually run this script!
exit(0)

# Upgrade RasPi 
sudo apt-get update 
sudo rpi-update
sudo reboot

sudo apt-get update 
sudo apt-get dist-upgrade -y
sudo apt-get upgrade -y


# Downloading repositories for setup and robot control
cd ~/git
git clone https://github.com/rldotai/lab-raspi.git
git clone https://github.com/rldotai/lab-irobot.git 

# Build Python3 
sudo apt-get install -y build-essential libncursesw5-dev libgdbm-dev libc6-dev 
sudo apt-get install -y zlib1g-dev libsqlite3-dev tk-dev
sudo apt-get install -y libssl-dev openssl 

# The actual Python version might be higher than indicated here
cd ~/
wget https://www.python.org/ftp/python/3.4.2/Python-3.4.2.tgz
tar -zxvf Python-3.4.2.tgz
cd Python-3.4.2
./configure
make 
sudo make install 

# Install pip
cd ~
wget https://bootstrap.pypa.io/get-pip.py
sudo python3.4 get-pip.py

# Set symlinks
sudo ln -sf /usr/local/bin/python3.4 /usr/local/bin/python3