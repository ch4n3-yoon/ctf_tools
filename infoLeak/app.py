#!/usr/bin/python
# coding: utf-8

from requests import *
import sys

def main():

    if len(sys.argv) < 2:
        print "[*] Usage : {0} [url]".format(sys.argv[0])

    url = sys.argv[1]
    r = get(url)

    check = ['Server', 'Content Security Policy', 'X-Forwarded-For', 'X-Powered-By']
    for c in check:
        try:
            header = r.headers[c]
            if header is not None:
                print "[*] '{0}' found : {1}".format(c, header)

        except KeyError:
            pass


if __name__ == '__main__':
    main()
