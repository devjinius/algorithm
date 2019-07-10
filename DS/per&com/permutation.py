def permutation(arr, r):
    used = [0] * len(arr)
    choosed = [None] * r

    def gen(depth):
        if depth == r:
            print(choosed)
            return

        for i in range(len(arr)):
            if not used[i]:
                choosed[depth] = arr[i]
                used[i] = 1
                depth += 1
                gen(depth)
                used[i] = 0
                depth -= 1
                choosed[depth] = None

    gen(0)


permutation([1, 2, 3], 3)
