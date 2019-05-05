# 백준알고리즘 1021번
# https://www.acmicpc.net/problem/1021

# 문제
# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로

# 입력
# 첫째 줄에 단어의 개수 N이 주어진다. (1≤N≤20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 주어지는 문자열의 길이는 50을 넘지 않는다.

# 출력
# 조건에 따라 정렬하여 단어들을 출력한다. 단, 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력한다.

# 반환값
# 없음


qlen, z = map(int, input().split())
printTarget = map(int, input().split())


class Queue:
    def __init__(self, num):
        self.queue = list(range(1, num+1))

    def left(self):
        self.queue.append(self.queue.pop(0))

    def right(self):
        self.queue.insert(0, self.queue.pop(-1))

    def find(self, target):
        return self.queue.index(target)

    def size(self):
        return len(self.queue)

    def front(self):
        return self.queue.pop(0)


queue = Queue(qlen)
count = 0

for target in printTarget:
    targetIndex = queue.find(target)
    if targetIndex <= (queue.size() // 2):
        for _ in range(targetIndex):
            queue.left()
            count += 1
    else:
        for _ in range(queue.size() - targetIndex):
            queue.right()
            count += 1

    queue.front()

print(count)
