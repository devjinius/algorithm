# 백준알고리즘 11050번
# https://www.acmicpc.net/problem/11050

# 문제
# 자연수 n과 정수 k가 주어졌을 때 이항 계수 를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 n과 k가 주어진다. (1 ≤ n ≤ 10, 0 ≤ k ≤ n)

n, k = map(int, input().split(" "))

memo = [0] * 11


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
    print(factorial(n) // (factorial(k)*factorial(n-k)))
