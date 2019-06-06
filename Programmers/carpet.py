# 프로그래머스 카펫
# https://programmers.co.kr/learn/courses/30/lessons/42842


def solution(brown, red):
    for i in range(1, red+1):
        total = brown + red
        m, r = divmod(red, i)
        if r != 0:
            continue

        m = m+2
        i = i+2
        if m * i == total:
            return [m, i]
