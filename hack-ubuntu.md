 # Spell to get a root prompt when you don't know the root password but have physical access
 1. Hold down shift when turning the power on to enter GRUB
 2. Edit the default boot option
 3. Find the line that starts `linux`
 4. At the end of the line add `init=/bin/bash`
 5. When booted, remount the filesystem rw with `mount -rw -o remount /`
Tested on Ubuntu 18.04
