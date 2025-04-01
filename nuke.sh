#!/bin/bash

# haha this might vaporise my system if i mess up the testing phase

# colors
RED="\e[31m"
GREEN="\e[32m"
YELLOW="\e[33m"
RESET="\e[0m"

echo -e "${RED}"
echo "=========================================="
echo "   ⚠️  WARNING: THIS WILL NUKE A DRIVE  ⚠️  "
echo "=========================================="
echo -e "${RESET}"

# list available drives
echo -e "${YELLOW}Available Drives:${RESET}"
lsblk -o NAME,SIZE,MODEL | grep -E '^sd|^nvme'

# ask the user for drive to nuke
read -p "Enter the drive(yk sda,nvme...bla bla,get out of here script kiddy): " DRIVE

# validate input
if [[ ! -e "/dev/$DRIVE" ]]; then
    echo -e "${RED}Error: Drive /dev/$DRIVE not found! Exiting.${RESET}"
    exit 1
fi

# confirmation
echo -e "${RED}Are you remotely sure you want to wipe /dev/$DRIVE? (yes/no)${RESET}"
read -r CONFIRM
if [[ "$CONFIRM" != "yes" ]]; then
    echo -e "${GREEN}Aborted.${RESET}"
    exit 0
fi

# overwrite passes
read -p "How many overwrite passes? (Default: 3): " PASSES
PASSES=${PASSES:-3}

# the fun part,shred execution..master shredder haha
echo -e "${YELLOW}Starting wipe process...${RESET}"
sudo shred -n "$PASSES" -vz "/dev/$DRIVE"

echo -e "${GREEN}✅ Drive /dev/$DRIVE successfully nuked.${RESET}"