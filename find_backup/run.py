#!/usr/bin/python
# coding: utf-8

from requests import *
import sys
import validators

if len(sys.argv) == 1:
    print "[*] usage : {0} http://url.com/".format(sys.argv[0])
    sys.exit(0)

url = sys.argv[1]

if url[-1] != "/":
    url += "/"

if not validators.url(url):
    print "[x] your url is not valid."
    sys.exit(-1)

f = open("data.txt", "r")
lines = f.readlines()
for line in lines:
    # r = get(url + line)
    print "[*] requesting..", url + line


f.close()


