# 백준알고리즘 1427번
# https://www.acmicpc.net/problem/1427

# 문제
# 배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.

# 입력
# 첫째 줄에 정렬하고자하는 수 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다.

# 반환값
# 없음


def solution(n):
    return "".join(sorted(list(map(lambda x: x, n)), reverse=True))


solution('2143')  # '4321'
