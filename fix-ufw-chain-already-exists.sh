#!/bin/sh
# Spell to fix errors like:
# ERROR: initcaps [Errno 2] ip6tables: Chain already exists.
# (Which you might get when frobbing ufw with ansible on older Ubuntu systems.)
# Seems to be caused by a ufw bug, fix is in Ubuntu 18.04
# More info here https://bugs.launchpad.net/ufw/+bug/1204579
ufw disable
sleep 1
iptables -F
sleep 1
iptables -X
sleep 1
ip6tables -F
sleep 1
ip6tables -X
sleep 1
ufw enable
