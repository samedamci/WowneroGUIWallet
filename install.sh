#!/bin/bash

WORKDIR=.

echo ""
echo -e "\e[95mWownero GUI Wallet Installation Script\e[0m"
echo ""

# Install Dependencies
echo ""
echo -e "\e[93mInstalling dependencies...\e[0m"
echo ""
sudo apt update && sudo apt install -y build-essential cmake pkg-config libboost-all-dev libssl-dev libzmq3-dev libsodium-dev python-pyside python-pip
pip install requests && pip install psutil

# Clone Repository & Submodules
echo ""
echo -e "\e[93mCloning Wownero repository & submodules..\e[0m"
echo ""
git submodule init && git submodule update
cd $WORKDIR/wownero
git fetch && git checkout release-v0.2.1.0

# Build Wownero
echo ""
echo -e "\e[93mBuilding Wownero...\e[0m"
echo ""
make

# Copy binaries
echo ""
echo -e "\e[93mCopying binaries to Resources directory...\e[0m"
echo ""
cp -R $WORKDIR/wownero/build/release/bin $WORKDIR/Resources/bin

# Exit Script
echo ""
echo -e "Installation is complete. You can now start your WOW wallet with"
echo ""
echo -e "command: \e[32m\e[1mpython wallet.py\e[0m"
echo ""
exit 0
