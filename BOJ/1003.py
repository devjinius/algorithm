# 백준알고리즘 1003번
# https://www.acmicpc.net/problem/1003

# 문제
# fibonacci(N)을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.

# 각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. N은 40보다 작거나 같은 자연수 또는 0이다.

# 출력
# 각 테스트 케이스마다 0이 출력되는 횟수와 1이 출력되는 횟수를 공백으로 구분해서 출력한다.

import sys
read = sys.stdin.readline

tLen = int(read())
m = [[] for i in range(41)]
m[0] = [1, 0]
m[1] = [0, 1]


def dp(n):
    if len(m[n]) != 0:
        return m[n]
    if len(m[n-1]) == 0:
        dp(n-1)
    if len(m[n-2]) == 0:
        dp(n-2)
    a, b = m[n-1]
    c, d = m[n-2]
    m[n] = [a + c, b + d]
    return m[n]


for _ in range(tLen):
    n = int(read())
    print(" ".join(map(str, dp(n))))
