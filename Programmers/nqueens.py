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


print(f"1 : {solution(1) == 1}")
print(f"2 : {solution(2) == 0}")
print(f"3 : {solution(3) == 0}")
print(f"4 : {solution(4) == 2}")
print(f"5 : {solution(5) == 10}")
print(f"6 : {solution(6) == 4}")
print(f"7 : {solution(7) == 40}")
print(f"8 : {solution(8) == 92}")
print(f"9 : {solution(9) == 352}")
print(f"10 : {solution(10) == 724}")
