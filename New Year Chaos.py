#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.


def minimumBribes(q):
    count = 0
    temp = 0
    expected = 0
    current = 0
    q = [i-1 for i in q]
    for index in range(len(q)):
        default_index = q[index]
        if index != default_index:

            if default_index > index:
                if default_index-index == 1:
                    count += 1
                elif default_index-index == 2:
                    count += 2
                else:
                    return ("Too chaotic")

                expected = default_index-1
                current = q.index(index)
            elif default_index < index:
                if expected = current:
                    pass
                elif expected > current:
                    if expected-current = 1:
                        count += 1

    #         if q[i]-i == 1 :
    #             if abs(q[i]-i) == 1:
    #                 count += 1

    #             elif q[i]-i == 2:
    #                 count+=2
    #                 expected = q[i]
    #                 current = q.index(i)
    #                 count += current-expected

    #         elif q[i] < i+1:
    #             pass

    #         else:
    #             return ("Too chaotic")


    # return count
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))
