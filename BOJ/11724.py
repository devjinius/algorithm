# BOJ 11724번 문제
# https://www.acmicpc.net/problem/11724

# 문제
# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

# 출력
# 첫째 줄에 연결 요소의 개수를 출력한다.


# ===========================================================================

import sys
sys.setrecursionlimit(100000)


def dfs(start, graph, visited):

    if start in visited:
        return visited

    visited.append(start)

    for i in range(len(graph[start])):
        if graph[start][i] == 1:
            graph[start][i] = 0
            visited = dfs(i, graph, visited)

    return visited


v, e = map(int, input().split(" "))

graph = [[0] * (v+1) for _ in range(v+1)]

for _ in range(e):
    x, y = map(int, input().split(" "))
    graph[x][y] = 1
    graph[y][x] = 1

visited = []
queue = list(range(1, v+1))
count = 0

while(len(queue) != 0):
    start = queue.pop(0)

    if start in visited:
        continue

    visited = dfs(start, graph, visited)
    count += 1

print(count)
