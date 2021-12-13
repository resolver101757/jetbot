#!/bin/sh
# copy service file to service location 
# Found this instruction to setup systemd script and permisions here : https://www.raspberrypi-spy.co.uk/2015/10/how-to-autorun-a-python-script-on-boot-using-systemd/ 

cp -v -f stats/jetbot_stats.service /etc/systemd/system/jetbot_stats.service
chmod +x  /home/jetbot/jetbot_ak/stats/stats.py
sudo chmod 644 /etc/systemd/system/jetbot_stats.service
systemctl enable jetbot_stats.service
systemctl start jetbot_stats.service
systemctl status jetbot_stats.service