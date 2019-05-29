# 백준알고리즘 2609번
# https://www.acmicpc.net/problem/2609

# 문제
# 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집들의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

# 입력
# 첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

# 출력
# 첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

n = int(input())

hmap = [[0] * (n+2) for i in range((n+2))]
visited = [[False] * (n+2) for i in range((n+2))]
queue = []

for i in range(n):
    r = input()
    for j in range(len(r)):
        hmap[i+1][j+1] = int(r[j])


def bfs():
    count = 0
    while(len(queue) != 0):
        i, j = queue.pop(0)

        if visited[i][j]:
            continue

        visited[i][j] = True

        if hmap[i][j] == 0:
            continue

        count += 1
        nextbfs = [
            [i-1, j],
            [i, j+1],
            [i, j-1],
            [i+1, j]
        ]

        queue.extend(nextbfs)
    return count


count = []
for i in range(1, n+1):
    for j in range(1, n+1):
        if visited[i][j]:
            continue
        queue.append([i, j])
        count.append(bfs())

answers = sorted(list(filter(lambda x: x != 0, count)))
print(len(answers))
for i in answers:
    print(i)
