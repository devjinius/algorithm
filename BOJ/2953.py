# 백준알고리즘 2953번
# https://www.acmicpc.net/problem/2953

# 문제
# 각 참가자가 얻은 점수는 다른 사람이 평가해 준 점수의 합이다. 이 쇼의 우승자는 가장 많은 점수를 얻은 사람이 된다.

# 각 참가자가 얻은 평가 점수가 주어졌을 때, 우승자와 그의 점수를 구하는 프로그램을 작성하시오.

# 입력
# 총 다섯 개 줄에 각 참가자가 얻은 네 개의 평가 점수가 공백으로 구분되어 주어진다. 첫 번째 참가자부터 다섯 번째 참가자까지 순서대로 주어진다. 항상 우승자가 유일한 경우만 입력으로 주어진다.

# 출력
# 첫째 줄에 우승자의 번호와 그가 얻은 점수를 출력한다.

# 반환값
# 없음


def solution():
    score = []
    for _ in range(5):
        score.append(sum(map(int, input().split(" "))))
    maxScore = max(score)
    print(f'{score.index(maxScore)+1} {maxScore}')


solution()
