#!/bin/bash

cd $HOME

apt update && apt upgrade -y
pkg install git -y
git clone https://github.com/termuxandlinux/termux.py
cd termux.py
chmod +x start.sh
./start.sh