# 올바른 괄호 만들기

# 숫자가 주어지면 해당 숫자만큼 괄호를 올바르게 만드는 모든 경우의 수를 반환한다.

# 1 => ()
# 2 => (()), ()()
# 3 => ((())), (()()), (())(), ()(()), ()()()
# ...


# def recursive(resArray, cur, num, openCount, closeCount):
#     if len(cur) == num * 2:
#         resArray.append(cur)
#         return

#     if openCount < num:
#         recursive(resArray, cur + '(', num, openCount + 1, closeCount)

#     if closeCount < openCount:
#         recursive(resArray, cur + ')', num, openCount, closeCount + 1)


# resArray = []
# recursive(resArray, "", 3, 0, 0)

# print(resArray)


def recursive(cur, openCount, closeCount):
    if len(cur) == num * 2:
        resArray.append(cur)
        return

    if openCount < num:
        recursive(cur + '(', openCount + 1, closeCount)

    if closeCount < openCount:
        recursive(cur + ')', openCount, closeCount + 1)


resArray = []
num = 3
recursive("", 0, 0)

print(resArray)
