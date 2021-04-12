#!/bin/bash

apt update

#install supporting software
apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libsqlite3-dev libreadline-dev libffi-dev curl libbz2-dev

#install python
wget https://www.python.org/ftp/python/3.9.1/Python-3.9.1.tgz
tar xzf Python-3.9.1.tgz
cd Python-3.9.1
./configure --enable-optimizations
make -j 4
make altinstall
cd ..

#install scapy
git clone https://github.com/secdev/scapy.git
cd scapy
python3.9 setup.py install

echo "All done!" 
python3.9 --version
