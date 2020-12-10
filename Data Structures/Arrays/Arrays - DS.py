#https://www.hackerrank.com/challenges/arrays-ds/problem

import math
import os
import random
import re
import sys

def reverseArray(a):
    a.reverse()
    return a

if __name__ == '__main__':
    arr_count=4
    arr=list(map(int, "1 4 3 2".rstrip().split()))

    res=reverseArray(arr)