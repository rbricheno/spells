#!/usr/bin/env python3
#
# These are the hashes of passwords that Windows likes.
# You might see this type of hash called an "NT Hash" or an "NTLM hash".
# This is the hash you put in your database if you want freeradius to authenticate
# users using NT hashes.

import hashlib
the_password = input()
print(hashlib.new('md4', the_password.encode('utf-16le')).hexdigest())
