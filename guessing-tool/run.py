#!/usr/bin/python
# coding: utf-8

from requests import *
import sys
import validators
import os

path = os.path.dirname(os.path.realpath(__file__))

if len(sys.argv) == 1:
    print "[*] usage : {0} http://url.com/".format(sys.argv[0])
    sys.exit(0)

url = sys.argv[1]

if url[-1] != "/":
    url += "/"

if not validators.url(url):
    print "[x] your url is not valid."
    sys.exit(-1)

f = open("{0}/data.txt".format(path), "r")
lines = f.readlines()
for line in lines:
    line = line.replace("\x0a", "")
    r = get(url + line)
    print "[+] requesting..", url + line

    if r.status_code == 404:
        print "[x] not found '{0}'..".format(line)

    elif r.status_code == 200:
        print "[*] found '{0}'!".format(line)
        print "="*10 + " {0} ".format(line) + "="*10
        print r.text
        print "="*len("="*10 + " {0} ".format(line) + "="*10)

    elif r.status_code == 403:
        print "[*] 403 forbidden '{0}'.".format(line)

    print


f.close()
