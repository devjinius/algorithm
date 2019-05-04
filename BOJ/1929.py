# 백준알고리즘 1929
# https://www.acmicpc.net/problem/1929

# 문제
# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000)

# 출력
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

m, n = map(int, input().split())

primeSet = set(range(2, n+1))

for i in range(2, n+1):
    if i in primeSet:
        primeSet -= set(range(i*2, n+1, i))

for i in sorted(list(primeSet)):
    if i >= m:
        print(i)
