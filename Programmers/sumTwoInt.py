# 프로그래머스 두 정수 사이의 합 문제
# https://programmers.co.kr/learn/courses/30/lessons/12912

# 문제
# 두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
# 예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.

# 제한 조건
# a와 b가 같은 경우는 둘 중 아무 수나 리턴하세요.
# a와 b는 -10,000,000 이상 10,000,000 이하인 정수입니다.
# a와 b의 대소관계는 정해져있지 않습니다.

# 입력값
#   int a와 b
#       a > b
# 출력값
#   a부터 b까지의 list생성

# ===========================================================================


def listRange(a, b):
    return list(range(a, b+1))


def solution(a, b):
    if a <= b:
        return sum(listRange(a, b))
    else:
        return sum(listRange(b, a))

# 삼항 연산자 사용
# def solution(a, b):
#     return sum(listRange(a, b)) if a <= b else sum(listRange(b, a))


print(solution(3, 5))
print(solution(3, 3))
print(solution(5, 3))
