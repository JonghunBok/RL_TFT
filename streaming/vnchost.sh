#!/bin/bash

/workspace/noVNC/utils/launch.sh &

/usr/bin/Xvfb :1 -screen 0 1920x1080x24 &

/usr/bin/x11vnc -xkb -noxrecord -noxfixes -noxdamage -display :1 -nopw -wait 5 -shared -permitfiletransfer -tightfilexfer -rfbport 5900 &


python main.py
