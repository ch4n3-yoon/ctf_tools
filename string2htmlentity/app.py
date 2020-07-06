#!/usr/bin/env python3
# coding: utf-8

import sys

def main():
    if len(sys.argv) < 2:
        print("[x] argv error!")
        sys.exit(-1)

    data = sys.argv[1]
    result = ''
    for d in data:
        result += '&#'+hex(ord(d)).replace('0x', '')+';'
    print(result)


if __name__ == '__main__':
    main()

