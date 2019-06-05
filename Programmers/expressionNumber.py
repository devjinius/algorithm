# 프로그래머스 숫자의 표현
# https://programmers.co.kr/learn/courses/30/lessons/12924

def solution(n):
    pointer = 1
    count = 0
    halfN = n // 2 
    while pointer <= halfN:
        sumN = 0
        i = pointer
        while sumN < n:
            sumN += i
            if sumN == n:
                count += 1
                break
            i += 1
        pointer += 1
    return count + 1
        