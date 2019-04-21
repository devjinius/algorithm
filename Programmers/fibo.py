# 피보나치 수
# https://programmers.co.kr/learn/courses/30/lessons/12945

# 문제
# 피보나치 수는 F(0) = 0, F(1) = 1일 때, 1 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 수 입니다.

# 2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, solution을 완성해 주세요.

# 제한 조건
# n은 1이상, 100000이하인 자연수입니다.

# 풀이
# n이 굉장히 커지면 기존의 top-down 방식의 피보나치로는 구하기가 힘들다.
# 그래서 반대로 bottom-up 하는 방식을 생각했다
# 또한 수가 너무 커져 1234567로 나눈 나머지를 구하는 문제라 아래와 같이 했다.


def solution(n):
    memo = {0: 0, 1: 1}
    num = 1
    while (num != n):
        num += 1
        memo[num] = (memo[num-2] % 1234567 + memo[num-1] % 1234567) % 1234567

    return memo[n]
