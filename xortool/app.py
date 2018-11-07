#!/usr/bin/env python
# coding: utf-8

import sys
import string

def isPrintable(data):
    for d in data:
        if not d in string.printable:
            return 0;
    return 1;

def xor(data, key, printable = True):
    # data: str type
    # key: int type
    result = ''
    for d in data:
        result += chr(ord(d) ^ key)
    if isPrintable(result):
        return result
    else:
        return "Not printable.."

def bruteforce(data):
    isPrintable_option = True
    for i in range(0, 128):
        print "(key : %d) / %s" % (i, xor(data, i, isPrintable_option))

def main():
    if len(sys.argv) == 1 or sys.argv[1] == '-h':
        print "### ch4n3's xortool ###"
        print "Usage : "
        print "\t%s --hex [hex data]" % sys.argv[0]
        print "\t%s --string [string data]" % sys.argv[0]

    elif sys.argv[1] == '--hex':
        data = sys.argv[2].decode('hex')
        bruteforce(data)
    elif sys.argv[1] == '--string':
        data = sys.argv[2]
        bruteforce(data)

    return 0;

if __name__ == '__main__':
    main()


