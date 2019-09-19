#!/bin/sh
# Spell to fix errors like:
# ERROR: initcaps [Errno 2] ip6tables: Chain already exists.
# (Which you might get when frobbing UFW with ansible.)
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
