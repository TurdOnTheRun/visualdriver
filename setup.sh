#!/bin/bash
export PYGAME_HIDE_SUPPORT_PROMPT=HIDE
export LIBFREENECT2_LOGGER_LEVEL=None
source env/bin/activate
echo "setting up encoder controller (/dev/ttyACM0)..."
sudo chmod a+rw /dev/ttyACM0
echo "setting up bottom controller (/dev/ttyACM1)..."
sudo chmod a+rw /dev/ttyACM1