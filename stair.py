#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    temp_output = []
    k = 1
    for i in range(n):
        for j in range(n-k):
            temp_output.append(" ")
        for l in range(k):
            temp_output.append("#")
        print("".join(temp_output))
        temp_output = []
        k+=1

if __name__ == '__main__':
    n = int(input())

    staircase(n)
