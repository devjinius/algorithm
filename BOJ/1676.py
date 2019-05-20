# 백준알고리즘 1676
# https://www.acmicpc.net/problem/1676

# 문제
# N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)

# 출력
# 첫째 줄에 구한 0의 개수를 출력한다.

n = int(input())
f = 1

for i in range(2, n+1):
    f *= i

f = str(f)
num = 0
for i in range(len(f)-1, -1, -1):
    if f[i] == '0':
        num += 1
    else:
        break
print(num)
