#!/bin/bash
echo "setting up serial port..."
sudo rfcomm bind 0 00:18:E4:40:00:06
sudo chmod a+rw /dev/rfcomm0
