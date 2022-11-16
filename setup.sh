#!/bin/bash
source env/bin/activate
echo "setting up rfcomm0..."
sudo rfcomm bind 0 00:18:E4:40:00:06
sudo chmod a+rw /dev/rfcomm0
echo "setting up uno controller..."
sudo chmod a+rw /dev/ttyACM0
echo "setting up encoder controller..."
sudo chmod a+rw /dev/ttyACM1