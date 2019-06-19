# 백준알고리즘 2160번
# https://www.acmicpc.net/problem/2160

# 문제
# N(2≤N≤50)개의 그림이 있다. 각각의 그림은 5×7의 크기이고, 두 가지 색으로 되어 있다. 이때 두 가지의 색을 각각 ‘X’와 ‘.’으로 표현하기로 하자. 이러한 그림들이 주어졌을 때, 가장 비슷한 두 개의 그림을 찾아내는 프로그램을 작성하시오.
# 두 개의 그림에서 다른 칸의 개수가 가장 적을 때, 두 개의 그림이 가장 비슷하다고 하자.
# 서로 다른 칸의 개수가 가장 작은 경우를 찾는 것이다.

# 입력
# 첫째 줄에 N이 주어진다. 다음 5×N개의 줄에 7개의 문자로 각각의 그림이 주어진다.

# 출력
# 첫째 줄에 가장 비슷한 두 그림의 번호를 출력한다. 그림의 번호는 입력되는 순서대로 1, 2, …, N이다. 번호를 출력할 때에는 작은 것을 먼저 출력한다. 입력은 항상 답이 한 가지인 경우만 주어진다.

import sys
read = sys.stdin.readline

n = int(input())
ps = [[None, None, None, None, None] for i in range(n)]


def compare(a, b):
    count = 0
    for i in range(5):
        for j in range(7):
            if a[i][j] != b[i][j]:
                count += 1
    return count


for i in range(n):
    for j in range(5):
        ps[i][j] = list(read().rstrip('\n'))

minK = [1, 2]
minV = 0

for i in range(n):
    for j in range(i+1, n):
        if i == 0 and j == 1:
            minV = compare(ps[i], ps[j])
            continue

        v = compare(ps[i], ps[j])
        if v < minV:
            minK[0] = i + 1
            minK[1] = j + 1
            minV = v

print(f'{minK[0]} {minK[1]}')
