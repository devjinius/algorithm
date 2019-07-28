# BOJ 11723번 문제
# https://www.acmicpc.net/problem/11723

# 문제
# 비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.

# add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
# remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
# check x: S에 x가 있으면 1을, 없으면 0을 출력한다.
# toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
# all: S를 {1, 2, ..., 20} 으로 바꾼다.
# empty: S를 공집합으로 바꾼다.

# 입력
# 첫째 줄에 수행해야 하는 연산의 수 M (1 ≤ M ≤ 3,000,000)이 주어진다.

# 둘째 줄부터 M개의 줄에 수행해야 하는 연산이 한 줄에 하나씩 주어진다.

# 출력
# check 연산이 주어질때마다, 결과를 출력한다.

import sys
read = sys.__stdin__.readline

n = int(read())

s = set()


def check(x):
    if x in s:
        print(1)
    else:
        print(0)


def add(x):
    s.add(x)


def remove(x):
    s.discard(x)


def toggle(x):
    if x in s:
        remove(x)
    else:
        add(x)


def allSet(s):
    return set(range(1, 21))


def empty(s):
    s.clear()


for _ in range(n):
    i = read().split(" ")
    if 'check' == i[0]:
        check(int(i[1]))
    elif 'add' == i[0]:
        add(int(i[1]))
    elif 'remove' == i[0]:
        remove(int(i[1]))
    elif 'toggle' == i[0]:
        toggle(int(i[1]))
    elif 'all\n' == i[0]:
        s = allSet(s)
    elif 'empty\n' == i[0]:
        empty(s)
