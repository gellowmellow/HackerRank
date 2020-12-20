#https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    n=len(arr)

    if len(set(arr))!=n:
        return 0

    s=sorted(arr)

    m=sys.maxsize
    for i in range(n-1):
        m=min(m,abs(s[i]-s[i+1]))

        if m==1:
            return m

    return m

if __name__ == '__main__':
    n = int(5)
    arr=[1,-3,71,68,17]

    result=minimumAbsoluteDifference(arr)
    print(result)