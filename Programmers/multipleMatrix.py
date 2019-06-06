def solution(arr1, arr2):
    m3 = len(arr1)
    n3 = len(arr2[0])
    answer = [[0]*n3 for i in range(m3)]

    for i in range(m3):
        row = arr1[i]
        for j in range(n3):
            temp = 0
            for k in range(len(arr2)):
                temp += row[k] * arr2[k][j]
            answer[i][j] = temp

    return answer


# print(solution([[1, 4], [3, 2], [4, 1], [2, 2]], [[3, 3], [3, 3]]))
print(solution([[1, 4, 3], [3, 2, 3], [4, 1, 3],
                [2, 2, 3]], [[3, 3], [3, 3], [1, 2]]))
# print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]],
#                [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))
