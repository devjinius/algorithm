# 백준알고리즘 1158번
# https://www.acmicpc.net/problem/1158

# 문제
# 조세퍼스 문제는 다음과 같다.

# 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-조세퍼스 순열이라고 한다. 예를 들어 (7, 3)-조세퍼스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

# N과 K가 주어지면 (N, K)-조세퍼스 순열을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N과 K가 빈 칸을 사이에 두고 순서대로 주어진다. (1 ≤ K ≤ N ≤ 5,000)

# 출력
# 예제와 같이 조세퍼스 순열을 출력한다.

n, k = list(map(int, input().split(" ")))
results = []
count = 1


class Node:
    def __init__(self, data, prevN, nextN):
        self.data = data
        self.prevN = prevN
        self.nextN = nextN


tail = None
cursor = None

for i in list(range(1, n+1)):
    if i == 1:
        tail = Node(i, None, None)
        cursor = tail
        tail.prevN = tail
        tail.nextN = tail
        continue
    newNode = Node(i, tail, cursor)
    tail.nextN = newNode
    tail = newNode

cursor.prevN = tail


def removeNode(cursor):
    cursor.prevN.nextN = cursor.nextN
    cursor.nextN.prevN = cursor.prevN
    return cursor.nextN


while (cursor.nextN != cursor):
    if count != k:
        cursor = cursor.nextN
        count += 1
        continue
    results.append(cursor.data)
    cursor = removeNode(cursor)
    count = 1

results.append(cursor.data)

resultStr = ", ".join(list(map(str, results)))
print("<"+resultStr+">")
