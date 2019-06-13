# 백준알고리즘 1149번
# https://www.acmicpc.net/problem/1149

# 문제
# RGB거리에 사는 사람들은 집을 빨강, 초록, 파랑중에 하나로 칠하려고 한다. 또한, 그들은 모든 이웃은 같은 색으로 칠할 수 없다는 규칙도 정했다. 집 i의 이웃은 집 i-1과 집 i+1이다.

# 각 집을 빨강으로 칠할 때 드는 비용, 초록으로 칠할 때 드는 비용, 파랑으로 드는 비용이 주어질 때, 모든 집을 칠할 때 드는 비용의 최솟값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 집의 수 N이 주어진다. N은 1,000보다 작거나 같다. 둘째 줄부터 N개의 줄에 각 집을 빨강으로 칠할 때, 초록으로 칠할 때, 파랑으로 칠할 때 드는 비용이 주어진다. 비용은 1,000보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 모든 집을 칠할 때 드는 비용의 최솟값을 출력한다.

import sys
read = sys.stdin.readline

length = int(input())
dp = [[] for i in range(length)]
for i in range(length):
    if i == 0:
        dp[i] = list(map(int, read().split(" ")))
        continue

    costs = list(map(int, read().split(" ")))
    prevC = dp[i-1]
    newC = [0, 0, 0]
    for j in range(3):
        if j == 0:
            newC[j] = min(prevC[1], prevC[2]) + costs[j]
        elif j == 1:
            newC[j] = min(prevC[0], prevC[2]) + costs[j]
        else:
            newC[j] = min(prevC[0], prevC[1]) + costs[j]
    dp[i] = newC

print(min(dp[-1]))
