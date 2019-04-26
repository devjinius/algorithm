# Persistent Bugger. 문제풀이
# https://www.codewars.com/kata/persistent-bugger/train/python

# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence,
# which is the number of times you must multiply the digits in num until you reach a single digit.

# 입력
# int n

# 반환값
# int

# 출력
# 없음

from functools import reduce


def persistence(n):
    strN = str(n)
    count = 0
    while(len(strN) != 1):
        sum = 1
        sum = reduce(lambda x, y: int(x)*int(y), strN)
        strN = str(sum)
        count += 1
    return count
