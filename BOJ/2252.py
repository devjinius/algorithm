# 백준알고리즘 2252번
# https://www.acmicpc.net/problem/2252

# 문제
# N명의 학생들을 키 순서대로 줄을 세우려고 한다. 각 학생의 키를 직접 재서 정렬하면 간단하겠지만, 마땅한 방법이 없어서 두 학생의 키를 비교하는 방법을 사용하기로 하였다. 그나마도 모든 학생들을 다 비교해 본 것이 아니고, 일부 학생들의 키만을 비교해 보았다.

# 일부 학생들의 키를 비교한 결과가 주어졌을 때, 줄을 세우는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N(1≤N≤32,000), M(1≤M≤100,000)이 주어진다. M은 키를 비교한 회수이다. 다음 M개의 줄에는 키를 비교한 두 학생의 번호 A, B가 주어진다. 이는 학생 A가 학생 B의 앞에 서야 한다는 의미이다.

# 학생들의 번호는 1번부터 N번이다.

# 출력
# 첫째 줄부터 앞에서부터 줄을 세운 결과를 출력한다. 답이 여러 가지인 경우에는 아무거나 출력한다.

n, m = map(int, input().split(" "))
students = [[] for _ in range(n+1)]
order = [0] * (n+1)
visited = [False] * (n+1)
queue = []

for _ in range(m):
    a, b = map(int, input().split(" "))
    students[a].append(b)
    order[b] += 1


visited[0] = True

for i in range(len(order)):
    if i == 0:
        continue
    if order[i] == 0:
        queue.append(i)


while len(queue) != 0:
    student = queue.pop(0)

    if visited[student] == True:
        continue

    if order[student] != 0:
        continue

    visited[student] = True

    for i in students[student]:
        order[i] -= 1

    queue.extend(students[student])

    if (len(queue) == 0):
        print(student, end='')
    else:
        print(student, end=' ')
