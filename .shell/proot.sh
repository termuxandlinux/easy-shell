#!/bin/bash

apt install proot-distro

echo "Which distribution would you like to install? (ubuntu/debian/arch/list)"
read distribution

case $distribution in
    ubuntu)
        echo "proot-distro install ubuntu"
        ;;
    debian)
        echo "proot-distro install debian"
        ;;
    arch)
        echo "proot-distro install arch"
        ;;
    list)
        echo "Ubuntu"
        echo "Debian"
        echo "Arch"
        ;;
    *)
        echo "Invalid input. Please choose one of the options: ubuntu, debian, arch, list."
        ;;
esac

echo "proot-distro login $distribution"