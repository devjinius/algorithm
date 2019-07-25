def solution(N):
    memo = [0] * 81
    memo[1] = 1
    memo[2] = 1

    def dp(n):
        if memo[n] == 0:
            memo[n] = dp(n-1) + dp(n-2)
        return memo[n]
    return dp(N)


solution(5)
