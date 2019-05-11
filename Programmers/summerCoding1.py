# 택시타기

# 택시를 타야하는데 그룹별로 탄다.
# 택시는 최대 4명이 탈 수 있고, 여러 그룹이 타도 무방하다.
# 한 그룹 당 최대 인원은 4명으로 주어진다.
# 그룹별 인원이 주어졌을 때 타야할 택시의 최솟값을 반환하시오.

# [1,2,3,4,1,2,3] => 4


def solution(group):
    sumGroup = sum(group)
    if(sumGroup % 4 == 0):
        return sumGroup // 4

    return sumGroup // 4 + 1


print(solution([1, 2, 3, 4, 1, 2, 3]))
