# 프로그래머스 약수의 합
# https://programmers.co.kr/learn/courses/30/lessons/12928

# 자연수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.

# 제한 조건
# n은 0 이상 3000이하인 자연수입니다.

# 입력값
# int

# 출력값
# -

# 반환값
# int

# ===========================================================================

# 풀이
# 약수는 나눠서 0이 되는 수다. 따라서 0 : n까지 나누어 떨어지는 모든 수를 구하면 된다.
# 성능 향상을 위해 0 : n/2 까지만 구해도 뒤는 반복이기 때문에 O(n/2)번만 반복하면 된다.


def solution(n):
    divides = set()
    for i in range(1, int(n / 2)+1):
        if (n % i == 0):
            divides.add(i)
            divides.add(int(n / i))
    if n == 1:
        return 1
    else:
        return sum(divides)


print(solution(12))  # 28
print(solution(5))  # 6
