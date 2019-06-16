# 백준알고리즘 1182번
# https://www.acmicpc.net/problem/1182

# 문제
# N개의 정수로 이루어진 수열이 있을 때, 길이가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수의 개수를 나타내는 N과 정수 S가 주어진다. (1 ≤ N ≤ 20, |S| ≤ 1,000,000) 둘째 줄에 N개의 정수가 빈 칸을 사이에 두고 주어진다. 주어지는 정수의 절댓값은 100,000을 넘지 않는다.

# 출력
# 첫째 줄에 합이 S가 되는 부분수열의 개수를 출력한다.

import sys
import itertools
read = sys.stdin.readline

n, s = map(int, read().split(" "))
l = list(map(int, read().split(" ")))
c = 0

for i in range(n):
    for j in itertools.combinations(l, i+1):
        if sum(j) == s:
            c += 1

print(c)

# 12 100
# 10 10 10 10 10 10 10 10 10 10 10 -10
