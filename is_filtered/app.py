#!/usr/bin/python
# coding: utf-8

import string
from pwn import *

remote_host = 'localhost'
remote_port = 1337

filtered = ['fail', 'filtered', 'ban']

def main():
    global filtered

    filtered_list = []
    for s in string.printable:
        p = remote(remote_host, remote_port)
        p.sendline(s)
        res = p.recv(1024)

        for f in filtered:
            if res.lower().find(f) > -1:
                print "[x] '%s' is filtered" % f
                filtered_list.append(f)

    print "[*] the filtered list : "
    print filtered_list



if __name__ == '__main__':
    main()

