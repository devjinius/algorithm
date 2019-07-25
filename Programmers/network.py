def solution(clen, computers):
    visited = [0] * clen
    global count
    count = 0

    def dfs(num, flag):
        global count
        net = computers[num]

        if not visited[num] and not flag:
            visited[num] = 1
            count += 1

        for i in range(clen):
            if i == num:
                continue
            if not visited[i] and net[i]:
                visited[i] = 1
                dfs(i, True)

    for i in range(clen):
        dfs(i, False)

    return count


solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
