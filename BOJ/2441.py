# 백준알고리즘 2441
# https://www.acmicpc.net/problem/2441

# 문제
# 첫째 줄에는 별 N개, 둘째 줄에는 별 N-1개, ..., N번째 줄에는 별 1개를 찍는 문제

# 하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

# 출력
# 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.

num = int(input())

for i in range(num):
    for j in range(num):
        if j >= i:
            print('*', end='')
        else:
            print(' ', end='')
    print()
