'''
HackerRank Left Rotation
 문제
https://www.hackerrank.com/challenges/array-left-rotation/problem

문제
A left rotation operation on an array of size n shifts each of the array's elements 1 unit to the left.

For example, if 2 left rotations are performed on array [1,2,3,4,5], then the array would become [3,4,5,1,2].

입력
The first line contains two space-separated integers denoting the respective values of n(the number of integers) and  d(the number of left rotations you must perform). 
The second line contains n space-separated integers describing the respective elements of the array's initial state.

반환값
-

출력
Print a single line of n space-separated integers denoting the final state of the array after performing d left rotations.'''


nd = input().split()

n = int(nd[0])

d = int(nd[1])

a = list(map(int, input().rstrip().split()))

for _ in range(d):
    a.append(a.pop(0))

print(" ".join(map(str, a)))
