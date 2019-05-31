# 주식가격
# https://programmers.co.kr/learn/courses/30/lessons/42584

# 문제 설명
# 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때,
# 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

# ===========================================================================


def solution(prices):
    mcArr = []
    for i in range(len(prices)):
        count = 0
        for j in range(i+1, len(prices)):
            count += 1
            if prices[i] <= prices[j]:
                if j == len(prices)-1:
                    mcArr.append(count)
            else:
                mcArr.append(count)
                break
    mcArr.append(0)
    return mcArr


print(solution([1, 2, 3, 2, 3]) == [4, 3, 1, 1, 0])
