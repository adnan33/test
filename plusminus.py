#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    p_f = 0
    n_f = 0
    z_f = 0
    for i in arr:
        if i==0:
            z_f +=1
        elif i>0:
            p_f += 1
        elif i<0:
            n_f +=1
    print("{:.6f}".format(p_f/len(arr)))
    print("{:.6f}".format(n_f/len(arr)))
    print("{:.6f}".format(z_f/len(arr)))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
