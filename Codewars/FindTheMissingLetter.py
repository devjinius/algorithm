# codewars Find the missing letter
# https://www.codewars.com/kata/5839edaa6754d6fec10000a2/train/python

# Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

# You will always get an valid array. And it will be always exactly one letter be missing.\
# The length of the array will always be at least 2.
# The array will always contain letters in only one case.

# Example:

# ['a','b','c','d','f'] -> 'e'
# ['O','Q','R','S'] -> 'P'
# (Use the English alphabet with 26 letters!)

# 입력
# string n

# 반환값
# string

# 출력
# 없음


def find_missing_letter(chars):
    asciiArr = list(map(ord, chars))
    rightWord = int(asciiArr[0])
    for word in asciiArr:
        if (rightWord != int(word)):
            return chr(rightWord)
        rightWord += 1
