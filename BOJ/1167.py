# 백준알고리즘 1167번
# https://www.acmicpc.net/problem/1167

# 문제
# 트리의 지름이란, 트리에서 임의의 두 점 사이의 거리 중 가장 긴 것을 말한다. 트리의 지름을 구하는 프로그램을 작성하시오.

# 입력
# 트리가 입력으로 주어진다.

# 먼저 정점 번호가 주어지고 다음 하나는 정점번호, 다른 하나는 그 정점까지의 거리이다.
# 각 줄의 마지막에는 -1이 입력으로 주어진다. 주어지는 거리는 모두 10,000 이하의 자연수이다.

# 출력
# 첫째 줄에 트리의 지름을 출력한다.

import sys
read = sys.stdin.readline


def dfs(n, visited, count):
    global vs
    global maxC
    visited[n] = 1
    for v, w in vs[n].items():
        if visited[v] == 1:
          if maxC[0] < count:
              maxC = [count, n]
          continue

        count += w
        dfs(v, visited, count)
        count -= w
    visited[n] = 0


vl = int(input())
global vs
global maxC
vs = {}
maxC = [0, 0]

for _ in range(vl):
    v, *l = map(int, read().split(" "))
    newd = {}
    i = 0
    while(1):
        if l[i] == -1:
            break
        newd[l[i]] = l[i+1]
        i += 2
    vs[v] = newd

visited = [0] * (vl+1)
dfs(1, visited, 0)
visited = [0] * (vl+1)
dfs(maxC[1], visited, 0)

print(maxC[0])
