#!/usr/bin/python
# coding: utf-8

import sys
import os
from pwn import *

def main():
    if len(sys.argv) < 2:
        print "[*] Usage : {0} [url]".format(sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]

    log.info("Running guessing tool")
    os.system("python ./guessing-tool/run.py {0}".format(url))

    log.info("Running info leak tool")
    os.system("python ./infoLeak/app.py {0}".format(url))


if __name__ == '__main__':
    main()
