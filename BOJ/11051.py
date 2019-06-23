# 백준알고리즘 11051번
# https://www.acmicpc.net/problem/11051

# 문제
# 자연수 n과 정수 k가 주어졌을 때 이항 계수 를  10,007로 나눈 나머지를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 n과 k가 주어진다. (1 ≤ n ≤ 10, 0 ≤ k ≤ n)

import sys
sys.setrecursionlimit(100000)

n, k = map(int, input().split(" "))

memo = [0] * 1001


def factorial(n):
    if n == 0 or n == 1:
        memo[n] = 1
        return 1
    if memo[n] != 0:
        return memo[n]
    memo[n] = factorial(n-1) * n
    return memo[n]


if k == 0:
    print(1)

else:
    print((factorial(n) // (factorial(k)*factorial(n-k))) % 10007)
