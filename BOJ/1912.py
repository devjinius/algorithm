# 백준알고리즘 4673
# https://www.acmicpc.net/problem/4673

# 문제

# n개의 정수로 이루어진 임의의 수열이 주어진다. 우리는 이 중 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합을 구하려고 한다.
# 단, 수는 한 개 이상 선택해야 한다.

# 예를 들어서 10, -4, 3, 1, 5, 6, -35, 12, 21, -1 이라는 수열이 주어졌다고 하자.
# 여기서 정답은 12+21인 33이 정답이 된다.

# 입력
# 첫째 줄에 정수 n(1 ≤ n ≤ 100,000)이 주어지고 둘째 줄에는 n개의 정수로 이루어진 수열이 주어진다. 수는 -1,000보다 크거나 같고, 1,000보다 작거나 같은 정수이다.

# 출력
# 첫째 줄에 답을 출력한다.

# 반환값
# 없음


# def solution():
#     length = int(input())
#     arr = list(map(int, input().split(" ")))
#     sum = [arr[0]]
#     for i in range(length-1):
#         sum.append(max(sum[i] + arr[i+1], arr[i+1]))
#     print(max(sum))


# solution()

n = int(input())
a = list(map(int, input().split(" ")))
dp = [0] * n
dp[0] = a[0]
s = 0
for i in range(1, n):
    dp[i] = max(dp[i-1] + a[i], a[i])

print(max(dp))
