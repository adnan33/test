#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positiveflag = 0
    negativeflag = 0
    zeroflag = 0
    for i in arr:
        if i==0:
            zeroflag +=1
        elif i>0:
            positiveflag += 1
        elif i<0:
            negativeflag +=1
    print("{:.6f}".format(positiveflag/len(arr)))
    print("{:.6f}".format(negativeflag/len(arr)))
    print("{:.6f}".format(zeroflag/len(arr)))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
