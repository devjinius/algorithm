# 프로그래머스 소수 찾기
# https://programmers.co.kr/learn/courses/30/lessons/12921

# 문제
# 1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

# 소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
# (1은 소수가 아닙니다.)

# 제한 조건
# n은 2이상 1000000이하의 자연수입니다.

# 입력값
# int n

# 출력값
# -

# 반환값
# int n

# ===========================================================================

# 최초풀이
# 에라토스테네스의 체를 내 나름대로 구현했다.


# def solution(n):
#     markingArr = [0, 0]
#     for i in range(2, n+1):
#         markingArr.append(i)
#     for i in range(2, n+1):
#         if markingArr[i] == 0:
#             continue

#         for j in range(i+i, n+1, i):
#             markingArr[j] = 0

#     return len(list(filter(lambda x: x != 0, markingArr)))

# 모범답
# 에라토스테네스의 체를 사용하는데
# set을 이용한다.
# 엄청나다. 꼭 숙지해서 소수문제에 써먹어보자


def solution(n):
    num = set(range(2, n+1))
    for i in range(2, n+1):
        if i in num:
            num -= set(range(2*i, n+1, i))
    return len(num)


print(solution(10))  # 4
print(solution(5))  # 3
