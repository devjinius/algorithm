# 체육복
# https://programmers.co.kr/learn/courses/30/lessons/42862

# 점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다. 다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다.
# 학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다.
# 예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다.
# 체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.

# 전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost,
# 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때,
# 체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 전체 학생의 수는 2명 이상 30명 이하입니다.
# 체육복을 도난당한 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
# 여벌의 체육복을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
# 여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.
# 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다.
# 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.

# 입력값
# int 배열

# 출력값
# -

# 반환값
# int

# ===========================================================================


# 초기 상태를 만들어줌
# 5명이라면 기본 배열은 [0, 0, 0, 0, 0, 0, 0] n+2의 배열
# 잃어버리지 않은 경우 1
# 잃어버린경우 0
# 잃어버렸는데 여벌이 있는 경우 1
# 잃어버리지 않았는데 여벌이 있는 경우 2
def setting(n, lost, reserve):
    clist = []
    for i in range(n+2):
        if i in lost:
            clist.append(0)
        else:
            clist.append(1)
    clist[0] = 0
    clist[n+1] = 0
    for i in reserve:
        if (clist[i] == 0):
            clist[i] = 1
        elif (clist[i] == 1):
            clist[i] = 2
    return clist


def borrow(n, clist):
    for i in range(1, n+1):
        if (clist[i] == 0):
            if (clist[i+1] == 2):
                clist[i] += 1
                clist[i+1] -= 1
            elif (clist[i-1] == 2):
                clist[i] += 1
                clist[i-1] -= 1
    return clist


def solution(n, lost, reserve):
    clist = setting(n, lost, reserve)
    newClist = borrow(n, clist)
    return len(list(filter(lambda x: x > 0, newClist)))
