#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    temp = []
    k = 1
    for i in range(n):
        for j in range(n-k):
            temp.append(" ")
        for l in range(k):
            temp.append("#")
        print("".join(temp))
        temp = []
        k+=1

if __name__ == '__main__':
    n = int(input())

    staircase(n)
