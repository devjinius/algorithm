# 백준알고리즘 1351번
# https://www.acmicpc.net/problem/1351

# 문제
# 무한 수열 A는 다음과 같다.

# A0 = 1
# Ai = A⌊i/P⌋ + A⌊i/Q⌋ (i ≥ 1)
# N, P와 Q가 주어질 때, AN을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 3개의 정수 N, P, Q가 주어진다.

# 출력
# 첫째 줄에 AN을 출력한다.

import sys
sys.setrecursionlimit(100000)
n, p, q = map(int, input().split(" "))
memo = {0: 1}


def dp(n, p, q):
    if n == 0:
        return 1

    if n in memo:
        return memo[n]

    memo[n] = dp(n//p, p, q) + dp(n//q, p, q)

    return memo[n]


print(dp(n, p, q))
