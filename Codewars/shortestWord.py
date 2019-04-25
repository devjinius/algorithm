# shortest word 문제풀이
# https://www.codewars.com/kata/shortest-word/train/python

# Simple, given a string of words, return the length of the shortest word(s).

# String will never be empty and you do not need to account for different data types.

# 입력
# string n

# 반환값
# string

# 출력
# 없음


def find_short(s):
    return min(list(map(len, s.split(" "))))
