'''
HackerRank Arrays_DS 문제
https://www.hackerrank.com/challenges/arrays-ds/problem

문제
Given an array, A, of Nintegers, print each element in reverse order as a single line of space-separated integers.

입력
The first line contains an integer,  N(the number of integers in A). 
The second line contains N space-separated integers describing A.

반환값
-

출력
Print all N integers in A in reverse order as a single line of space-separated integers.
'''


# input을 정리하여 아래와 같은 코드를 제공한다. reverseArray만 코딩하면 된다.
# input을 reverse해서 return하면 끝

def reverseArray(a):
    return a[::-1]

# arr = list(map(int, input().rstrip().split()))


arr = [1, 4, 3, 2]
res = reverseArray(arr)

print(res)
