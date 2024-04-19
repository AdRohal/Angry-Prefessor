import math
import os
import random
import re
import sys

def angryProfessor(k, a):
    on_time_students = sum(1 for arrival_time in a if arrival_time <= 0)

    if on_time_students < k:
        return "YES" 
    else:
        return "NO"

if __name__ == '__main__':
    try:
        t = int(input().strip())
        for t_itr in range(t):
            first_multiple_input = input().rstrip().split()
            if len(first_multiple_input) != 2:
                raise ValueError("Expected two values for n and k")
            n = int(first_multiple_input[0])
            k = int(first_multiple_input[1])
            a = list(map(int, input().rstrip().split()))
            if len(a) != n:
                raise ValueError("Number of elements in a should be equal to n")
            result = angryProfessor(k, a)
            print(result)
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
