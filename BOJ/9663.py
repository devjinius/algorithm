# BOJ 9663번 문제
# https://www.acmicpc.net/problem/9663

# 문제
# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N이 주어진다. (1 ≤ N < 15)

# 출력
# 첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.

# ===========================================================================
def solution(n):
    global count
    count = 0

    if n == 1:
        return 1

    def dp(placed):
        global count
        placing = [1] * n
        depth = len(placed)
        for j in range(len(placed)):
            changingCoulmn = placed[j]
            placing[changingCoulmn] = 0
            ld = changingCoulmn - (depth - j)
            rd = changingCoulmn + (depth - j)

            if -1 < ld < n:
                placing[ld] = 0

            if -1 < rd < n:
                placing[rd] = 0

        if depth == n-1:
            for i in range(n):
                if placing[i]:
                    count += 1
                    return

        for i in range(n):
            if placing[i]:
                newPlaced = placed + [i]
                dp(newPlaced)

    for i in range(n):
        dp([i])

    return count


n = int(input())
print(solution(n))
