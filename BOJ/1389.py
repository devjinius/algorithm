# 백준알고리즘 1389번
# https://www.acmicpc.net/problem/1389

# 문제
# 케빈 베이컨의 6단계 법칙에 의하면 지구에 있는 모든 사람들은 최대 6단계 이내에서 서로 아는 사람으로 연결될 수 있다. 케빈 베이컨 게임은 임의의 두 사람이 최소 몇 단계 만에 이어질 수 있는지 계산하는 게임이다.
# BOJ 유저의 수와 친구 관계가 입력으로 주어졌을 때, 케빈 베이컨의 수가 가장 작은 사람을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 유저의 수 N (2 ≤ N ≤ 100)과 친구 관계의 수 M (1 ≤ M ≤ 5,000)이 주어진다. 둘째 줄부터 M개의 줄에는 친구 관계가 주어진다. 친구 관계는 A와 B로 이루어져 있으며, A와 B가 친구라는 뜻이다. A와 B가 친구이면, B와 A도 친구이며, A와 B가 같은 경우는 없다. 친구 관계는 중복되어 들어올 수도 있으며, 친구가 한 명도 없는 사람은 없다. 또, 모든 사람은 친구 관계로 연결되어져 있다.

# 출력
# 첫째 줄에 BOJ의 유저 중에서 케빈 베이컨의 수가 가장 작은 사람을 출력한다. 그런 사람이 여러 명일 경우에는 번호가 가장 작은 사람을 출력한다.

import sys
read = sys.stdin.readline

n, m = map(int, read().split(" "))
INF = 987654321

dp = [[INF] * (n) for i in range(n)]


for _ in range(m):
    a, b = map(lambda x: int(x)-1, read().split(" "))
    dp[a][b] = 1
    dp[b][a] = 1


for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                dp[i][j] = 0
                continue

            if dp[i][k] != INF and dp[k][j] != INF:
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

maxV, p = 0, 0

for i, v in enumerate(map(sum, dp)):
    if i == 0:
        p = i
        maxV = v
        continue
    if v < maxV:
        p = i
        maxV = v

print(p+1)
