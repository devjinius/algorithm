# 프로그래머스 전화번호 목록
# https://programmers.co.kr/learn/courses/30/lessons/42577

# 정렬풀이


def solution(phone_book):
    sbook = sorted(phone_book)
    for i in range(1, len(phone_book)):
        if sbook[i].startswith(sbook[0]):
            return False

    return True

# 해쉬 문제이므로 해쉬로도 풀어보도록 하자:
