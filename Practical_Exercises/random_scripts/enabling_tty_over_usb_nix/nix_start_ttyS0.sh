#!/bin/sh

chmod +x ./readonly_to_write.sh
./readonly_to_write.sh /etc/systemd/system/serial-getty@ttyS0.service

chmod +x ./inject_systemctl.sh
./inject_systemctl.sh status serial-getty@ttyS0.service
./inject_systemctl.sh enable serial-getty@ttyS0.service

sudo systemctl enable serial-getty@ttyS0.service
sudo systemctl status serial-getty@ttyS0.service | cat
