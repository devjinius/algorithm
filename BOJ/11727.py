# BOJ 11727번 문제
# https://www.acmicpc.net/problem/11727

# 문제
# 2×n 직사각형을 2×1과 2×2 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

# 아래 그림은 2×17 직사각형을 채운 한가지 예이다.

# 입력
# 첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)

# 출력
# 첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.


# ===========================================================================

import sys
sys.setrecursionlimit(1500)

memo = [None] * 1001


def dp(num):
    if num == 2:
        return 3
    elif num == 1:
        return 1

    if memo[num] != None:
        return memo[num]

    memo[num] = (dp(num-1) %
                 10007 + (((dp(num-2) % 10007) * 2) % 10007)) % 10007

    return memo[num]


num = int(input())
print(dp(num))
