# 백준알고리즘 10974번
# https://www.acmicpc.net/problem/10974

# 문제
# N이 주어졌을 때, 1부터 N까지의 수로 이루어진 순열을 사전순으로 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 8)이 주어진다.

# 출력
# 첫째 줄부터 N!개의 줄에 걸쳐서 모든 순열을 사전순으로 출력한다.

n = int(input())


def permutation(arr, r):
    used = [0] * len(arr)
    choosed = [None] * r

    def gen(choosed, used, depth):
        if depth == r:
            print(" ".join(map(str, choosed)))
            return

        for i in range(len(arr)):
            if not used[i]:
                choosed[depth] = arr[i]
                used[i] = 1
                depth += 1
                gen(choosed, used, depth)
                used[i] = 0
                depth -= 1
                choosed[depth] = None

    gen(choosed, used, 0)


permutation(range(1, n+1), n)
