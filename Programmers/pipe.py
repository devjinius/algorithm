# 프로그래머스 쇠막대기
# https://programmers.co.kr/learn/courses/30/lessons/42585


def solution(arrangement):
    stack = []
    prevStr = ''
    count = 0

    for word in arrangement:
        if(word == ")"):
            if(prevStr == "("):
                stack.pop()
                count += len(stack)
            else:
                stack.pop()
                count += 1
        else:
            stack.append(word)
        prevStr = word

    return count
