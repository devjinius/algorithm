# 백준알고리즘 10872번
# https://www.acmicpc.net/problem/10872

# 문제
# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수 N(0 ≤ N ≤ 12)가 주어진다.

# 출력
# 첫째 줄에 N!을 출력한다.

n = int(input())
num = 1

for i in range(2, n+1):
    num *= i

print(num)
