# 최대공약수와 최소공배수
# https://programmers.co.kr/learn/courses/30/lessons/12940

# 두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요.
# 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다.
# 예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.

# 입력값
# int 2개

# 출력값
# -

# 반환값
# int 배열

# ===========================================================================


def solution(n, m):
    gcd = findGcd(n, m)
    return [gcd, n*m//gcd]


def findGcd(u, v):
    while(v != 0):
        temp = u % v
        u = v
        v = temp
    return u

# 최대공약수(GCD)는 유클리드 호제법을 구현한다.
# 최소공배수(LCM)는 a * b // gcd다.
# 이유는 x = ab, y = bc 라고 할때 최대공약수가 b, 최소공배수는 abc다.
# 그럼 x * y = ab2c이다. 이 때 b를 나누어주면 abc가 나오기 때문
# 이정도는 외워보자
