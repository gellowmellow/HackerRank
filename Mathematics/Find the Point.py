#https://www.hackerrank.com/challenges/find-point/problem

import os
import sys

def findPoint(px, py, qx, qy):
    return "%s %s" % (qx+(qx-px),qy+(qy-py))

if __name__ == '__main__':
    n = int(10)
    m=["1 1 2 2","4 3 5 2","2 4 5 6","1 2 2 2","1 1 1 1","1 2 2 1","1 8 7 8","9 1 1 1","8 4 3 2","7 8 9 1"]

    for n_itr in range(n):
        pxPyQxQy = m[n_itr].split()

        px = int(pxPyQxQy[0])
        py = int(pxPyQxQy[1])
        qx = int(pxPyQxQy[2])
        qy = int(pxPyQxQy[3])

        result = findPoint(px, py, qx, qy)
        print(result)