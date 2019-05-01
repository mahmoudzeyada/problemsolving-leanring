#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.


def hourglassSum(arr):
    subset = []
    temp = []
    for i in range(4):
        for j in range(4):
            temp = arr[i][j:j+3]
            temp.append(arr[i+1][j+8], arr[i+2][j:j+3])
            print(sum(temp))

    return(max(subset))


if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
