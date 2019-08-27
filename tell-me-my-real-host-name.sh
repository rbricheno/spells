#!/bin/sh
# Spell to tell me the fully qualified host name of the box I'm logged in to, as it appears in the DNS.

host `ip addr | grep inet | grep global | head -1 | cut -d " " -f 6 | cut -d "/" -f 1`
