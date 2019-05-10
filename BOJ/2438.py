# 백준알고리즘 2438
# https://www.acmicpc.net/problem/2438

# 문제
# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

# 출력
# 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.

num = int(input())

for i in range(num):
    for j in range(num):
        if j <= i:
            print('*', end='')
    print()
