# BOJ 11725번 문제
# https://www.acmicpc.net/problem/11725

# 문제
# 루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

# 출력
# 첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.

# 7
# 1 6
# 6 3
# 3 5
# 4 1
# 2 4
# 4 7

import collections
import sys
read = sys.stdin.readline

vlen = int(input())

edges = [list() for _ in range(vlen+1)]
visited = [False] * (vlen+1)
parents = [0] * (vlen+1)

for _ in range(vlen-1):
    v1, v2 = map(int, read().split())
    edges[v1].append(v2)
    edges[v2].append(v1)

queue = collections.deque()
visited[1] = True

for edge in edges[1]:
    queue.append([edge, 1])

while(len(queue) != 0):
    v, p = queue.popleft()
    visited[v] = True
    parents[v] = p
    for edge in edges[v]:
        if visited[edge]:
            continue
        queue.append([edge, v])

for parent in parents:
    if parent != 0:
        print(parent)
