# 잠금패턴

# 1, 2, 3
# 4, 5, 6
# 7, 8, 9

# 이렇게 휴대폰 잠금화면의 버튼이 있다.

# 정점과 라인 각각을 vertex와 edge라고 하자
# 패턴이 주어졌을 때의 edge가 만나는 다른 edge의 개수를 반환하라.

# 참고자료: https://crazyj.tistory.com/140


def isDivide(x, y):

    f1 = (x[2]-x[0])*(y[1]-x[1]) - (x[3]-x[1])*(y[0]-x[0])
    f2 = (x[2]-x[0])*(y[3]-x[1]) - (x[3]-x[1])*(y[2]-x[0])
    if f1*f2 <= 0:
        return True
    else:
        return False


def isCross(x, y):
    b1 = isDivide(x, y)
    b2 = isDivide(y, x)
    if b1 and b2:
        return True
    return False


def solution(pattern):

    locations = {
        1: [1, 3],
        2: [2, 3],
        3: [3, 3],
        4: [1, 2],
        5: [2, 2],
        6: [3, 2],
        7: [1, 1],
        8: [2, 1],
        9: [3, 1]
    }

    edges = []
    for i in range(len(pattern)-1):
        x1, y1 = locations[pattern[i]]
        x2, y2 = locations[pattern[i+1]]
        edges.append([x1, y1, x2, y2])

    countList = [0] * (len(pattern)-1)
    for i in range(len(edges)):
        count = 0
        for j in range(len(edges)):
            if isCross(edges[i], edges[j]):
                count += 1
        countList[i] = count-1

    return countList


print(solution([1, 2, 5, 8, 9]))
