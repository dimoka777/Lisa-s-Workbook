"""
    Lisa's WorkBook Hackerrank Max Score 25

"""
import math
import os
import random
import re
import sys
import numpy

# Complete the workbook function below.
def workbook(n, k, arr):

    attempt = 0
    counter = 0
    result = []
    for i in range(n):
        temp = 0
        new_list = []
        for j in range(arr[i]):
            new_list.append(temp + 1)
            temp += 1
        while len(new_list) >= k:
            result.append(new_list[:k])
            if counter+1 in result[counter]:
                attempt += 1
            del new_list[:k]
            counter += 1
        if len(new_list) < k and len(new_list) != 0:
            result.append(new_list)
            if counter+1 in result[counter]:
                attempt += 1
            counter += 1
    return attempt


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # nk = input().split()
    # n = int(nk[0])
    # k = int(nk[1])
    # arr = list(map(int, input().rstrip().split()))
    result = workbook(5, 3, [4,2,6,1,10])
    print(result)
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
