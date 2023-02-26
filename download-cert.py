#!/usr/bin/env python3

# Download and save a *validated* SSL certificate.
# I wrote this but I don't need it.
# Maybe one day I will.

import ssl
import certifi
import os
import argparse
from socket import gaierror
import sys

# I really like this decorator
# https://github.com/bitranox/wrapt_timeout_decorator
from wrapt_timeout_decorator import *

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

@timeout(5)
def dl_cert(host, port, out):
    address = (host,port)
    cert = ssl.get_server_certificate(address, ca_certs=os.path.relpath(certifi.where()));
    if not out:
        print(cert)
    else:
        with open(out,'w') as file:
            file.writelines(cert)

parser = argparse.ArgumentParser(
                    prog = 'download-cert',
                    description = 'Downloads a validated SSL certificate in PEM format.',
                    )

parser.add_argument('hostname', type=str, help='hostname')
parser.add_argument('-p','--port', type=str, default=443, help='TCP port number. Default is 443', required=False)
parser.add_argument('-o','--out', type=str, help='PEM file to output (will be overwritten). Omitting this will cause the PEM to be printed to stdout.', required=False)

args = parser.parse_args()
try:
    dl_cert(args.hostname, args.port, args.out)
except gaierror:
    eprint("Error: gaierror - problem communicating with the hostname/address")
    exit(1)
except TimeoutError:
    eprint("Error: timeout error for " + args.hostname + " on port " + args.port)
except Exception as e:
    eprint("Error: unknown:")
    eprint(e)
    exit(1)
