# BOJ 13419 문제
# https://www.acmicpc.net/problem/13419

# 문제

# 탕수육 게임에서 1번 플레이어는 탕육수만 말하면 이긴다.
# 2번 플레이어는 수탕육만 말하면 이긴다.
# 이를 ABC로 바꾸었을때 N개의 길이의 알파벳을 말하는 탕수육 게임을 한다.
# 1번과 2번 플레이어가 이기는 공식을 출력하라.

# 입력값
# 4
# ABC
# ABCFXZ
# K
# DY

# 출력값
# ACB
# BAC
# ACX
# BFZ
# K
# K
# D
# Y

# ===========================================================================

testLen = int(input())

for _ in range(testLen):
    targetString = input()
    targetLen = len(targetString)
    player1 = ''
    player2 = ''

    if (targetLen == 1):
        player1 = targetString
        player2 = targetString
    elif (targetLen % 2 == 0):
        for i in range(targetLen):
            if(i % 2 == 0):
                player1 += targetString[i]
            else:
                player2 += targetString[i]
    else:
        for i in range(targetLen):
            if(i % 2 == 0):
                player1 += targetString[i]
            else:
                player2 += targetString[i]
        for i in range(targetLen):
            if(i % 2 == 0):
                player2 += targetString[i]
            else:
                player1 += targetString[i]

    print(player1)
    print(player2)
