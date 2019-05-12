# 백준알고리즘 2609번
# https://www.acmicpc.net/problem/2609

# 문제
# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.

# 출력
# 첫째 줄에는 입력으로 주어진 두 수의 최대공약수를,둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.


def solution(n, m):
    gcd = findGcd(n, m)
    print(gcd)
    print(n*m//gcd)


def findGcd(u, v):
    while(v != 0):
        temp = u % v
        u = v
        v = temp
    return u


n, m = map(int, input().split(" "))

solution(n, m)
