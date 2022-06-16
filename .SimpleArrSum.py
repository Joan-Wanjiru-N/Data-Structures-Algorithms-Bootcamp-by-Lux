"""My thinking through the problem"""
# ar_count = int(input().strip())
# def simpleArraySum():
#     ar = []
#     for i in range(1,ar_count+1):
#         ar.append(i)
#     total = 0
#     for i in ar:
#         total += i
#     return total
# print(simpleArraySum())     

"""Hackerrank solution"""

import math
import os
import random
import re
import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
    # Write your code here
    additems = 0
    for i in ar:
        additems +=i
    return additems
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()