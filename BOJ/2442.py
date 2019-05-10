# 백준알고리즘 2442
# https://www.acmicpc.net/problem/2442

# 문제
# 첫째 줄에는 별 1개, 둘째 줄에는 별 3개, ..., N번째 줄에는 별 2×N-1개를 찍는 문제

# 별은 가운데를 기준으로 대칭이어야 한다.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

# 출력
# 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.

num = int(input())

forNum = 2 * num - 1
midNum = num - 1
for i in range(forNum):
    if i >= num:
        index = i - 2 - 2*(i-num)
    else:
        index = i
    for j in range(forNum):
        if midNum - index <= j <= midNum + index:
            print('*', end='')
            continue

        if j < midNum - index:
            print(' ', end='')
            continue
        continue
    print()
