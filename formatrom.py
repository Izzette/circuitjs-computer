#!/usr/bin/env python3

import sys

data = []
with open(sys.argv[1], 'rb') as f:
    while True:
        b = f.read(1)
        if not b:
            break

        i = int.from_bytes(b, 'little')
        data.append(i >> 4)
        data.append(i & 0xf)

for i in range(0, len(data), 8):
    print("{:d}: {:s}".format(i, ' '.join([str(x) for x in data[i:i+8]])))
