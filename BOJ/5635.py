# 백준알고리즘 5635번
# https://www.acmicpc.net/problem/5635

# 문제
# 어떤 반에 있는 학생들의 생일이 주어졌을 때, 가장 나이가 어린 사람과 가장 많은 사람을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 반에 있는 학생의 수 n이 주어진다. (1 ≤ n ≤ 100)

# 다음 n개 줄에는 각 학생의 이름과 생일이 "이름 dd mm yyyy"와 같은 형식으로 주어진다. 이름은 그 학생의 이름이며, 최대 15글자로 이루어져 있다. dd mm yyyy는 생일 일, 월, 연도이다.

# 이름이 같거나, 생일이 같은 사람은 없다.

# 출력
# 첫째 줄에 가장 나이가 어린 사람의 이름, 둘째 줄에 가장 나이가 많은 사람 이름을 출력한다.


testLen = int(input())
people = []

for _ in range(testLen):
    people.append(input().split(" "))


def cmp(x):
    return int(x[3]), int(x[2]), int(x[1])


people.sort(key=cmp)

print(people[-1][0], people[0][0])
